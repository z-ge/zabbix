#!/bin/bash 

export PATH=$PATH:/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/opt/nginx/sbin:/opt/php/bin
export LANG=en_US.UTF-8
HOST="127.0.0.1"
PORT="1080" 

# Functions to return nginx stats 
HOST="127.0.0.1"
PORT="1080"

function check() {
    /sbin/pidof nginx | wc -l 
}

function active() {
    /usr/bin/curl -s "http://$HOST:$PORT/nginx_status/" 2>/dev/null| grep 'Active' | awk '{print $NF}'
}
function accepts() { 
    /usr/bin/curl -s "http://$HOST:$PORT/nginx_status/" 2>/dev/null| awk NR==3 | awk '{print $1}'
}
function handled() { 
    /usr/bin/curl -s "http://$HOST:$PORT/nginx_status/" 2>/dev/null| awk NR==3 | awk '{print $2}'
}
function requests() {
    /usr/bin/curl -s "http://$HOST:$PORT/nginx_status/" 2>/dev/null| awk NR==3 | awk '{print $3}'
}
function reading() { 
    /usr/bin/curl -s "http://$HOST:$PORT/nginx_status/" 2>/dev/null| grep 'Reading' | awk '{print $2}'
}
function writing() { 
    /usr/bin/curl -s "http://$HOST:$PORT/nginx_status/" 2>/dev/null| grep 'Writing' | awk '{print $4}'
}
function waiting() { 
    /usr/bin/curl -s "http://$HOST:$PORT/nginx_status/" 2>/dev/null| grep 'Waiting' | awk '{print $6}'
}

case "$1" in
    active)
        active
        ;;
    check)
        check
        ;;
    accepts)
        accepts
        ;;
    handled)
        handled
        ;;
    requests)
        requests
        ;;
    reading)
        reading
        ;;
    writing)
        writing
        ;;
    waiting)
        waiting
        ;;

    *)
        echo $"Usage $0 {active|accepts|handled|requests|reading|writing|waiting}"
        exit        
esac
