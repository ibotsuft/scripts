#!/bin/bash

cd "/home/kali/rc/teams/helios-base/src"
./start.sh &>> /home/kali/ibots/statsfile/terminal/${1}.txt -t ${1}
