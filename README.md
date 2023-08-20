# PingCo_repo

## Коллеги! Без лишних слов расскажу как запустить приложение:

  1. Для начала создайте папку для проекта, затем создайте виртуальное окружение и активируйте его:
  
   ```python3 -m venv venv```
   
   ```source ven/bin/activate```
     
  3. ﻿﻿﻿Установите все зависимости из файла requirements.txt (обязательно при активном виртуальном окружении) :

   ```
   pip install -r requirements. txt
   ```

  5. Установите PostgreSQL, если у вас его нет, для линуксоидов (пример для Ubuntu, копипаст) : 
 
   ```
   sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
   wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
   sudo apt-get update
   sudo apt-get -y install postgresql
   ```
   
   Для виндоводов: разбирайтесь сами :)
   
﻿﻿﻿  4. Откройте psql:
    
  ```sudo -i -u postgres psql```
     
  5. ﻿﻿﻿Создайте базу (тут можно копипастуть):

  ```
 CREATE DATABASE ping_co_db;
 CREATE ROLE masha_pinguin WITH PASSWORD 'Napoleon';
 ALTER ROLE masha_pinguin WITH LOGIN;
 GRANT ALL PRIVILEGES ON DATABASE ping_co_db to masha_pinguin;
 ALTER USER MashaNapoleon CREATEDB;
  ```
     
  6. ﻿﻿﻿Сделайте миграции:

  ```
  python3 manage.py migrate
  ```

  8. Если все прошло без ошибок:
  
  ```
  python3 manage. py runserver
  ```
     

## Trouble shooting:

  1.При ошибке " Unable to create the django migrations table ":
  
  ```
  ALTER DATABASE ping_co_db OWNER TO masha_pinguin;
  ```

  И снова попытайтесь провести миграции

  2. При ошибке "That port is already in use":

  ```
  sudo fuser -k 8000/tcp
  ```

  4. Если возникла ошибка при установке psycopg2:

   ```sudo apt install libpq-dev python3-dev```

   И перезапустите установку зависимостей (requirements.txt)


### P.S. Если вы столкнулись с ошибками, которые здесь не описаны, то пишите мне в ТГ (со скринами).

### P.S. ReadMe будет постепенно меняться, так что будьте внимательны!





__________________________________________________________________________________________________









