#!/bin/bash
# check if the script is run with exactly one argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <username>"
    exit 1
fi

# Run the 'whoami' command under the user passed as an argument
sudo -u "$1" whoami
