# <h1> Downloader Task </h1>

Install Python and PIP
```sh
sudo apt-get install python3 python3-pip
sudo apt-get install python3.7-dev 
```
Install additional soft
```sh
sudo apt-get install celery

sudo apt-get install rabbitmq-server
```

Setting up RabbitMQ
```sh
$ sudo rabbitmqctl add_user user password
$ sudo rabbitmqctl add_vhost myvhost
$ sudo rabbitmqctl set_user_tags user tag
$ sudo rabbitmqctl set_permissions -p vhost user
```

Run Celery 
