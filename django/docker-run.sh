docker rm `docker stop django`
docker run --name django \
--restart=always \
--dns=192.168.100.222 \
-e TZ='Asia/Shanghai' \
-p 8102:80 \
-d 192.168.100.222:5000/python:django #\
#sh /uwsgi/startpython.sh
