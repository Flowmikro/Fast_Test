## Установка 
Установить репозиторий  
```commandline
https://github.com/Flowmikro/Fast_Test.git
```
Перейти в директорию
```commandline
cd Fast_Test
```
#### Запустить проект можно двумя способами  
#### Первый способ через docker
```commandline
docker build . -t fastapi_app:latest
```
```commandline
docker run -p 8000:8000 fastapi_app 
```
Перейти по адресу
```commandline
http://localhost:8000/docs
```
#### Второй способ
Активировать виртуальную среду на Mac/Linux
```commandline
python3 -m venv venv
source venv/bin/activate
```
Активировать виртуальную среду на Windows
```commandline
python -m venv venv
.\venv\Scripts\activate 
```
Установить пакеты
```commandline
pip install -r requirements.txt
```
Выполнить alembic миграцию
```commandline
alembic upgrade head             
```
Запустить
```commandline
uvicorn main:app --reload
```
