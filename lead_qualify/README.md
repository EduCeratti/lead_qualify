* Usuário de Teste

url: localhost:8000/admin

user: ceratti
pass: ceratti

* Django REST FRAMEWORK in 
    localhost/touchpoint

* Start celery scheduler - periodic tasks
    celery -A lead_qualify beat -l info


* View celery worker
    celery -A lead_qualify worker -l info