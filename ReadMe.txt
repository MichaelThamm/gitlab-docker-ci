GitLab: CI/CD tool for coding, testing, building, deploying
Docker: Containerization on linux kernals of host
Docker-Compose: Run multiple docker containers together
Flask: Micro web-framework for python applications


References:
GitLab - https://www.youtube.com/watch?v=qP8kir2GUgo
Docker-Compose - https://www.youtube.com/watch?v=HG6yIjZapSA
Sync GitHub with GitLab - https://everythingshouldbevirtual.com/git/syncing-gitlab-and-github-repos/


Notes:
- JSON is more efficient so it is used for data exchange.
- YAML is often used for configuration for readability.


Process:
- docker-compose build
    - Uses the docker-compose.yml file to build the docker network
    - This executes each Dockerfile to make docker images
- docker-compose up
    - --build option will rebuild the containers before starting
    - --d option will start in detached mode
- docker network ls
    - This shows the networks that containers made with docker-compose can communicate accross
    - Access them using their service names

- docker exec -it <container ID> sh
    - Interactive terminal