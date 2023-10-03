FROM gitlab/gitlab-runner:latest

#prerequisites
RUN apt update \
    && apt --yes install apt-utils nano
    
#docker
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - \
    && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
    && apt update \
    && apt -yf --no-install-recommends install docker-ce docker-compose-plugin docker-buildx-plugin \
    && groupmod -g 1003 gitlab-runner \
    && gpasswd -a gitlab-runner docker \
    && usermod -aG docker gitlab-runner

#buildx builder
RUN docker buildx install
