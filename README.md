Celery + Redis + Django
=========================================

> Aplicacion DEMO para demostrar el envío de emails de forma asincrónica
> usando Celery y redis


Configuración
--------------------------
La configuración se realiza a través del archivo `.env` situado en el root
del proyecto

```.env
    # configuracion para el envio de emails
    EMAIL_HOST=smtp.example.com
    EMAIL_HOST_PASSWORD=passw0rd
    EMAIL_HOST_USER=user
    EMAIL_HOST_PORT=587
    DEFAULT_FROM_EMAIL=user@example.com

    # configuracion de celery
    CELERY_BROKER_URL=redis://redis
```


Uso
-------------------------

```
docker-compose up --build
```