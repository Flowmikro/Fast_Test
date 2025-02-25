## Установка 
Установить репозиторий  
```commandline
https://github.com/Flowmikro/project.git
```
Перейти в директорию
```commandline
cd project
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
