
Welcome, this is a repo to host a website using Python, JavaScript, HTML.

# Steps
The implementation of this website was tested using Windows OS but can be done using Linux or macOS as well since the Docker container works in any OS by using the hosts Linux kernal. However, the batch files in the root directory are intended for Windows users and to replicate them in another OS you will have to find the equivalent operations per your OS. To begin, clone this repo to a local directory.

## Hosted Locally
To host the web page locally, run [DevelopeEnvironment.bat](https://github.com/MichaelThamm/Flask-Docker/blob/main/DevelopeEnvironment.bat) and then [StartApp.bat](https://github.com/MichaelThamm/Flask-Docker/blob/main/StartApp.bat) once complete. These two batch files will create a clean developement environment by creating a virtual environment and installing dependancies. Then the app is started using Flask and a browser to the correct local port is opened which is the website.

## Hosted on the Web
To host the application on the web, Heroku was used which uses Git to manage the implementations. Follow the Heroku-Flask link in the Supporting References section to create on for yourself. This page can be found at [michaelthamm.com](http://www.michaelthamm.com)

# Conclusion
Flask was used to create a web application using the HTML/JavaScript templates from w3schools which serve as good portfolio websites. The use of Docker and Git streamlines the maintainance process for the web application environment making it a robust workflow.

# Supporting References
- [Docker-Flask](https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/)
- [Flask-Web-App](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)
- [Heroku-Flask](https://realpython.com/flask-by-example-part-1-project-setup/)
- [Website-Templates](https://www.w3schools.com/w3css/w3css_templates.asp)
- [This-Website-Templates](https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_parallax&stacked=h)
- [Youtube-Heroku-Custom-Domain1](https://www.youtube.com/watch?v=xWyaV_ZtLS0)
- [Youtube-Heroku-Custom-Domain2](https://www.youtube.com/watch?v=_tzkF68ZjVE)
