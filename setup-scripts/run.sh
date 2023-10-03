#!/bin/bash

. ./setup-scripts/set-env.sh
docker compose up -d
. ./setup-scripts/wait-for-gitlab-service.sh
. ./setup-scripts/get-initial-gitlab-pswd.sh
. ./setup-scripts/provision-gitlab.sh

