docker rm `docker stop uwsgi`
docker run --name uwsgi \
--restart=always \
--dns=114.114.114.114 \
-e TZ='Asia/Shanghai' \
-p 8101:80 \
-v $PWD/testflk.py:/uwsgi/testflk.py \
-d python \
sh /uwsgi/startpython.sh
