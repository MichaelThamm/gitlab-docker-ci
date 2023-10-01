# Background

This project is a guide on setting up a local GitLab instance that has a designated GitLab Runner to execute a CI/CD pipeline.
There is a sample front end application using Flask which is hidden behind Traefik's reverse proxy, all of which are built using docker-compose.

* GitLab: CI/CD tool and repository
* GitLab Runner: Configurable Docker container to conduct CI/CD pipeline jobs
* Docker: Containerization of services on a host
* Docker-Compose: Run multiple docker services together
* Flask: Micro web-framework for python applications
* Traefik: Reverse-proxy and load balancer

# Process

* Clone this GitHub repo to a local directory
  * We want GitHub to act as the main repo

- Use the docker-compose.yml file to build the docker network
    - Execute "docker-compose build"
    - This executes each service config or a specified Dockerfile to make docker images

- Start the containers
    - Execute "docker-compose up -d"
    - -d option will start containers in detached mode

- On initial login of local GitLab instance, obtain the initial root password
    - Navigate to a browser and enter "gitlab.docker.localhost"
    - Execute "docker exec -it <container name> cat /etc/gitlab/initial_root_password"
    - This grabs the credentials from the docker container
    - Username is "root"
    - Make sure to add a user and make yourself an admin

- Mirror the GitHub repo with GitLab's repo
    - Check the "Sync GitHub with GitLab" reference below
    - Create a blank project in the local GitLab instance
    - Copy the URL of this GitLab project
    - Setup GitHub as both fetch and push, GitLab as just push

- Register a gitlab runner for this project
    - In the local GitLab instance, navigate to the project's settings
    - Navigate to CI/CD > Runners > Specific Runners
    - Copy the registration token
    - Get the gitlab-runner container id with "docker ps"
    - Execute "docker exec -it <gitlab-runner container id> bash"
    - Execute "gitlab-runner register"
    - Register the runner using the URL "http://gitlab:80/" and registration token copied earlier
    - For the executor select "shell"


---References---

Local GitLab Runner Install - https://docs.gitlab.com/runner/install/windows.html | https://www.tutorialspoint.com/gitlab/gitlab_installation.htm
Local GitLab Runner Setup - https://www.youtube.com/watch?v=G8ZONHOTAQk
GitLab Using Docker-Compose - https://docs.gitlab.com/ee/install/docker.html#install-gitlab-using-docker-compose
GitLab - https://www.youtube.com/watch?v=qP8kir2GUgo
Docker-Compose - https://www.youtube.com/watch?v=HG6yIjZapSA
Sync GitHub with GitLab - https://everythingshouldbevirtual.com/git/syncing-gitlab-and-github-repos/
Run Docker in Docker - https://www.youtube.com/watch?v=sUy9C1bY3gQ | https://docs.docker.com/engine/install/ubuntu/
Modify GitLab Runner config.toml - https://nagachiang.github.io/gitlab-ci-gitlab-runner-cant-fetch-changes-from-repository/#
Simple Traefik Setup - https://doc.traefik.io/traefik/getting-started/quick-start/
