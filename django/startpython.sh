#!/usr/bin/bash
sh /uwsgi/version.sh
/usr/sbin/nginx -c /uwsgi/nginx.conf
uwsgi /uwsgi/student/student/wsgi.ini
while [[ true ]]; do 
    sleep 1 
done
