#!/bin/bash

# Set GitHub as an import source in the settings
curl --request PUT \
  --header "Host:gitlab.docker.localhost" \
  --header "content-type: application/json" \
  --header "PRIVATE-TOKEN: $GITLAB_PAT" \
  --data '{"personal_access_token":"'"$GITHUB_PAT"'","repo_id":516925150,"target_namespace":"root"}' \
  "http://127.0.0.1/api/v4/application/settings?import_sources=github"

# Import the GitHub website repo into the GitLab instance
curl --request POST \
  --header "Host:gitlab.docker.localhost" \
  --header "content-type: application/json" \
  --header "PRIVATE-TOKEN: $GITLAB_PAT" \
  --data '{"personal_access_token":"'"$GITHUB_PAT"'","repo_id":516925150,"target_namespace":"root"}' \
  "http://127.0.0.1/api/v4/import/github"

# Create the GitLab runner
create_runner_response=$(curl -s --request POST \
  --header "Host:gitlab.docker.localhost" \
  --header "content-type: application/json" \
  --header "PRIVATE-TOKEN: $GITLAB_PAT" \
  --data '{"runner_type": "instance_type"}' \
  "http://127.0.0.1/api/v4/user/runners" | jq -r '.token')

docker compose exec gitlab-runner gitlab-runner register \
  --non-interactive \
  --url "http://gitlab" \
  --token "$create_runner_response" \
  --executor "docker" \
  --docker-image "alpine:latest"