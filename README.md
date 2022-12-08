# Task Manager
タスク管理ツール。

## install

Python 3.10.8 (選定理由適当)

### venv

#### poetry

```
$ pip install poetry
```

#### activate

```
$ poetry shell
```


### run server

```
$ python task_manager/manage.py runserver 8000
```

### install postgresql

```
sudo apt install -y python3-pip python3-dev libpq-dev postgresql postgresql-contrib
```

### create database

```
python manage.py makemigrations
```



### link

* http://localhost:8000/dashboard/
* https://getbootstrap.jp/
* https://bootstrap-datepicker.readthedocs.io/en/latest/
    * date picker
    * license は Apache

