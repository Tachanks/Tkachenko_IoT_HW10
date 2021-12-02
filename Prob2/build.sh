#!/bin/bash

echo "Builds read_button and GPIO and configures pin 46"

g++ read_button.cpp GPIO.cpp -o read_button.cgi -l cgicc -pthread

config-pin -a p8.16 in+ 
