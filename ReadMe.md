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

* :computer: -> On your host device
* :fox_face: -> In GitLab service
* 

1. :computer: Clone this GitHub repo to a local directory
2. :computer: Use the docker-compose.yml file to serve the docker services
   1. Execute "docker-compose up -d"

3. :computer: On initial login of local GitLab instance, obtain the initial root password
   1. TLDR; Execute "docker compose exec gitlab cat /etc/gitlab/initial_root_password"
      1. More info -> [set-up-the-initial-password](https://docs.gitlab.com/omnibus/installation/index.html#set-up-the-initial-password)
4. :fox_face: Create a [personal access token (PAT)](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) in GitLab

5. :computer: Mirror the GitHub repo with GitLab's repo
    1. [Sync GitHub with GitLab](https://everythingshouldbevirtual.com/git/syncing-gitlab-and-github-repos/)
    2. Create a blank project in the local GitLab instance
    3. Copy the URL of this GitLab project
    4. Setup GitHub as both fetch and push, GitLab as just push

- Register a gitlab runner for this project
    - In the local GitLab instance, navigate to the project's settings
    - Navigate to CI/CD > Runners > Specific Runners
    - Copy the registration token
    - Get the gitlab-runner container id with "docker ps"
    - Execute "docker exec -it <gitlab-runner container id> bash"
    - Execute "gitlab-runner register"
    - Register the runner using the URL "http://gitlab:80/" and registration token copied earlier
    - For the executor select "shell"


# References

Local GitLab Runner Install - https://docs.gitlab.com/runner/install/windows.html | https://www.tutorialspoint.com/gitlab/gitlab_installation.htm
Local GitLab Runner Setup - https://www.youtube.com/watch?v=G8ZONHOTAQk
GitLab Using Docker-Compose - https://docs.gitlab.com/ee/install/docker.html#install-gitlab-using-docker-compose
GitLab - https://www.youtube.com/watch?v=qP8kir2GUgo
Docker-Compose - https://www.youtube.com/watch?v=HG6yIjZapSA
Sync GitHub with GitLab - https://everythingshouldbevirtual.com/git/syncing-gitlab-and-github-repos/
Run Docker in Docker - https://www.youtube.com/watch?v=sUy9C1bY3gQ | https://docs.docker.com/engine/install/ubuntu/
Modify GitLab Runner config.toml - https://nagachiang.github.io/gitlab-ci-gitlab-runner-cant-fetch-changes-from-repository/#
Simple Traefik Setup - https://doc.traefik.io/traefik/getting-started/quick-start/
