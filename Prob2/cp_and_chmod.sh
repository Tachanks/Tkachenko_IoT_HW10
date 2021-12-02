#!/bin/bash

echo "Copies application to CGI bin directory and issues permissions"

sudo cp read_button.cgi /usr/lib/cgi-bin/

sudo chmod +s /usr/lib/cgi-bin/read_button.cgi



