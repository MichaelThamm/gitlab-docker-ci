GitLab: CI/CD tool for coding, testing, building, deploying
Docker: Containerization on linux kernals of host
Docker-Compose: Run multiple docker containers together
Flask: Micro web-framework for python applications


References:
Local GitLab Runner Install - https://docs.gitlab.com/runner/install/windows.html | https://www.tutorialspoint.com/gitlab/gitlab_installation.htm
Local GitLab Runner Setup - https://www.youtube.com/watch?v=G8ZONHOTAQk
GitLab Using Docker-Compose - https://docs.gitlab.com/ee/install/docker.html#install-gitlab-using-docker-compose
GitLab - https://www.youtube.com/watch?v=qP8kir2GUgo
Docker-Compose - https://www.youtube.com/watch?v=HG6yIjZapSA
Sync GitHub with GitLab - https://everythingshouldbevirtual.com/git/syncing-gitlab-and-github-repos/
Run Docker in Docker - https://www.youtube.com/watch?v=sUy9C1bY3gQ | https://docs.docker.com/engine/install/ubuntu/
Modify GitLab Runner config.toml - https://nagachiang.github.io/gitlab-ci-gitlab-runner-cant-fetch-changes-from-repository/#

Notes:
- JSON is more efficient so it is used for data exchange.
- YAML is often used for configuration for readability.
- Since gitlab-Runner exec clones the current state of the local Git repository,
    be sure to have committed any changes you want to test beforehand.
- Traefik acts as a reverse-proxy and a load balancer. It also allows all the
    unsecure protocols to hide behind the reverse-proxy and secure ones are sent to the reverse-proxy


Process:
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

Locations:
- /etc/gitlab-runner/config.toml
    - Inside the gitlab-runner container
    - gitlab-runner reconfigure
- /etc/gitlab/gitlab.rb
    - Inside the GitLab container do modify its configuration