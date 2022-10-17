---Background---

GitLab: CI/CD tool and repository
GitLab Runner: Configurable Docker container to initiate CI/CD pipeline
Docker: Containerization on linux kernals of host
Docker-Compose: Run multiple docker containers together
Flask: Micro web-framework for python applications
Traefik: Reverse-proxy and load balancer

This project is a guide on setting up a local GitLab instance that has a designated GitLab Runner to execute a CI/CD pipeline.
There is a sample front end application using Flask which is hidden behind Traefik's reverse proxy, all of which are built using docker-compose.


---Process---

- Clone this GitHub repo to a local directory
    - We want GitHub to act as the main repo and GitLab will act as a local repo
    - This mirrors the local GitLab repo from the public GitHub repo
    - Check the "Sync GitHub with GitLab" reference below
    - Setup GitHub as both fetch and push, GitLab as just push
- docker-compose build
    - Uses the docker-compose.yml file to build the docker network
    - This executes each Dockerfile to make docker images
- docker-compose up
    - --build option will rebuild the containers before starting
    - -d option will start in detached mode
- docker exec -it <container name> cat /etc/gitlab/initial_root_password
    - Username is "root"
    - This grabs the credentials from the docker container
- docker network ls
    - This shows the networks that containers made with docker-compose can communicate accross
    - Access them using their service names
- docker exec -it <container ID or name> /bin/bash
    - Interactive terminal
- \\wsl$\docker-desktop-data\data\docker\volumes
    - Enter this in Windows File Explorer to access the Docker volumes
- curl gitlab:80
    - Within a docker container I can run these commands to test connection over docker network bridge
- gitlab-runner register
    - Run this on the gitlab-runner docker container
    - Use http://gitlab for the GitLab instance url
- apt-get install -y curl && curl -sSL https://get.docker.com/ | sh
    - This will install docker on a docker container that has the docker socket volume mounted
- curl http://host.docker.internal:801/
    - This will access the localhost through the host.docker.internal alias


---Locations---

- /etc/gitlab-runner/config.toml
    - Inside the gitlab-runner container
    - gitlab-runner reconfigure
- /etc/gitlab/gitlab.rb
    - Inside the GitLab container do modify its configuration


---References---

Local GitLab Runner Install - https://docs.gitlab.com/runner/install/windows.html | https://www.tutorialspoint.com/gitlab/gitlab_installation.htm
Local GitLab Runner Setup - https://www.youtube.com/watch?v=G8ZONHOTAQk
GitLab Using Docker-Compose - https://docs.gitlab.com/ee/install/docker.html#install-gitlab-using-docker-compose
GitLab - https://www.youtube.com/watch?v=qP8kir2GUgo
Docker-Compose - https://www.youtube.com/watch?v=HG6yIjZapSA
Sync GitHub with GitLab - https://everythingshouldbevirtual.com/git/syncing-gitlab-and-github-repos/
Run Docker in Docker - https://www.youtube.com/watch?v=sUy9C1bY3gQ | https://docs.docker.com/engine/install/ubuntu/
Modify GitLab Runner config.toml - https://nagachiang.github.io/gitlab-ci-gitlab-runner-cant-fetch-changes-from-repository/#