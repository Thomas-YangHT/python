docker run --name uwsgi \
-v /opt/uwsgi:/uwsgi \
--restart=always \
--dns=192.168.254.251 \
-e TZ='Asia/Shanghai' \
-p 8101:80 \
-d python \
sh /uwsgi/startpython.sh
