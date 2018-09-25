docker run --name uwsgi \
-v /opt/uwsgi:/uwsgi \
--restart=always \
--dns=192.168.32.1 \
-e TZ='Asia/Shanghai' \
-p 8102:80 \
-d python \
sh /uwsgi/startpython.sh
