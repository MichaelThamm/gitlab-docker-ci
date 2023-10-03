#!/bin/bash

if docker-compose exec gitlab test -f /etc/gitlab/initial_root_password; then
    echo "Here is your initial_root_password:"
    docker-compose exec gitlab cat /etc/gitlab/initial_root_password
else
    echo -e "If you need help logging in:\nhttps://docs.gitlab.com/omnibus/installation/index.html#set-up-the-initial-password"
fi