# Use an official Python runtime as a parent image
FROM python:3.9.2

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./requirements.txt /app

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

COPY . .
#ENV FLASK_APP=my_flask.py

EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "app.py","--host", "0.0.0.0"]




#CMD ["flask", "run", "--host", "0.0.0.0"]