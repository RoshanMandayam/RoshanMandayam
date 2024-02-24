# are-we-there-yet
Are We There Yet? - a single player map-based guessing game!

Below are a list of steps to get the site running:
This project was built using Docker 4.26.1, may or may not work with later versions.

1. Clone the repo 
2. Replace the api keys for the Google Map API Key (line 74 of app.py, session['key'] = "YOUR_API_KEY")
3. Download Docker (download the desktop app: https://www.docker.com/products/docker-desktop/)
4. Build the Docker Image using the terminal ( 'docker build -t nameOfYourImage .' ), after navigating to the current project folder
5. Run the container( 'docker run -p 8080:8080 -v /host/directory:/container/directory nameOfYourImage' ), changing the file paths accordingly (my example is /Users/roshanmandayam/are-we-there-yet:/app) 


If the leaderboard.db does not exist, or if you want to recreate a new leaderboard, use the following commands in terminal(after navigating to the current project folder):
Note: the docker container must be running before you use these commands
>>> docker exec -it NAME_OF_YOUR_CONTAINER python3
>>> from app import db
>>> db.create_all()
>>> exit()
