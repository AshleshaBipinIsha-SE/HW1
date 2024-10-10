#!/bin/bash
proc_id=$(ps -ef | awk '/[i]nfinite/{print $2}')
if [ -n "$proc_id" ]; then
    kill "$proc_id"
    echo "Killed infinite.sh with PID =  $proc_id"
fi
