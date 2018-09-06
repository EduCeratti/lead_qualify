* Usuário de Teste

url: localhost:8000/admin

user: ceratti
pass: ceratti

<<<<<<< HEAD
* Django REST FRAMEWORK in 
    localhost/touchpoint
=======
>>>>>>> 0e2901b95ffb5790488b1fa33f7c9277b532c451

* Start celery scheduler - periodic tasks
    celery -A lead_qualify beat -l info


* View celery worker
    celery -A lead_qualify worker -l info