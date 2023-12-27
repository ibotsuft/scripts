#!/bin/bash

teamName1=$1
teamName2=$2

parallel -u ::: 'bash ./quickStartServer.sh 1' "bash ./quickStartPlayer1.sh $teamName1 2" "bash ./quickStartPlayer2.sh $teamName2 3" 'bash ./quickStartMonitor.sh 4'
