docker run --name uwsgi \
--restart=always \
--dns=192.168.30.1 \
-e TZ='Asia/Shanghai' \
-p 8101:80 \
-d 192.168.100.222:5000/python \
sh /uwsgi/startpython.sh
