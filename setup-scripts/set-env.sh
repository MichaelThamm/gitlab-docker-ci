#!/bin/bash

echo "IMPORTANT: Make sure the .env file is set to LF line endings"
export $(grep -v '^#' ./.env | xargs -d '\n')