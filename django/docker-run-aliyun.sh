docker rm `docker stop django`
docker run --name django \
--restart=always \
--dns=192.168.100.222 \
-e TZ='Asia/Shanghai' \
-p 8102:80 \
-d registry.cn-hangzhou.aliyuncs.com/yanghaitao/django:1.0 #\
#sh /uwsgi/startpython.sh
