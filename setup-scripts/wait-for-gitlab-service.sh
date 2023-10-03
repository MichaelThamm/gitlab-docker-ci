#!/bin/bash

check_health() {
    # Use docker inspect to check service health
    docker inspect --format='{{.State.Health.Status}}' "$1"
}

# Capture the IDs as a string
service_ids=$(docker ps -aq --filter name=gitlab-docker-ci-gitlab)
echo "$service_ids"

# Convert the string into an array
service_ids_array=($service_ids)
# Wait for the service to become healthy
for service_id in "${service_ids_array[@]}"; do
  while [[ $(check_health "$service_id") != "healthy" ]]; do
      current_status=$(check_health "$service_id")
      echo "$service_id: Current status is: $current_status, please continue waiting"
      sleep 5
  done
done