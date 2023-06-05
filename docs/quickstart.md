## QuickStart

### Prepare python runtime

```shell
git clone https://github.com/luohu1/drf-apiserver.git
cd drf-apiserver

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv --copies venv
source venv/bin/activate
python3 -m pip install --upgrade pip setuptools
python3 -m pip install -r requirements.txt
```

### Prepare MySQL database

```sql
CREATE DATABASE `drf_apiserver` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'admin'@'127.0.0.1' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'127.0.0.1' WITH GRANT OPTION;
```

### Run django server

```shell
source venv/bin/activate
cd apiserver
python manage.py migrate
python manage.py runserver
```
