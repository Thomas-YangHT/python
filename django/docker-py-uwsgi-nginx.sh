docker run --name django \
-v /opt/python/django:/uwsgi \
--restart=always \
--dns=192.168.100.222 \
-e TZ='Asia/Shanghai' \
-p 8102:80 \
-d 192.168.100.222:5000/python:django \
sh /uwsgi/startpython.sh
