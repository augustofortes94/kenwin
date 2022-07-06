# kenwin
Esta es una aplicacion creada para el challenge de Kenwin.
La misma consta de una simple app que sirva como lista de contactos donde se puede tanto crear y eliminarlos.


Condiciones de instalacion de app:
    -instalar docker
    -instalar pgadmin4 (para la base de datos postgresql)


*Se deja visible el archivo .env en el proyecto para facilidad de la prueba con las variables de entorno.


Create database:
    -Crear database llamada kenwin con password '1234'
    -Restaurar database desde archivo "database-backup"


Construir y ejecutar app:
    -Comando: "docker-compose up"


Acceso a la app desde browser:
    http://localhost:8000/


Se dispone de una api con los siguientes endpoints:
    -(POST) API Register: http://localhost:8000/api/register/
    -(POST) API Login: http://localhost:8000/api/login/
    -(GET) API Contats: http://localhost:8000/api/contacts/
    -(POST) API Contacts: http://localhost:8000/api/contacts/

*Se creo el archivo "Kenwin.postman_collection.json" para importar desde Postman para mayor comodidad.

------TESTS-----

Se encuentran dentro de la aplicacion "app". Ejecutar con el comando "python kenwinproject/manage.py tests"
