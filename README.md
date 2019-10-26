SWAPI-simple tests
===========

#### Для запуска необходим установленный Python Version 3.7.x

## Преднастрйока окружения 
устанавливаем пакет virtualevn windows/unix (если не установлена)
```
pip install virtualenv / sudo pip3.7 install virtualenv
```
разворачиваем виртуальную среду 
```
python -m venv venv / python3.7 -m venv venv
```

Запуск виртуальной среды Windows / unix 
```
venv\Scripts\activate / source venv/bin/activate

```

Установка зависимостей
```
pip install -r requirements.txt
```

## Запуск тестов

для запуска тестов  
```
pytest -v
```
для запуска по нескольким тегам 
```
pytest -v -m 'smoke and body'
```
