# kenwin
Esta es una aplicacion creada para el challenge de Kenwin.
La misma consta de una simple app que sirva como lista de contactos donde se puede tanto crear y eliminarlos.
Utilice Django para todo lo que es web, y django-rest-framework para la construccion de la API. Esta ultima
la hice mediante clases, utilizando "APIView" para poder controlar bien cada uno de los verbos HTTP que queria
realizar. El proyecto esta dividido en dos aplicaciones que interactuan entre ellas (app y user). La primera,
"app" contiene todo lo que es la api y aplicacion web para el manejo de los contactos. Y la aplicacion "user"
se encarga de todo lo que es el login y el registro de usuarios.


Condiciones de instalacion de app:
    -instalar docker
    -instalar pgadmin4 (para la base de datos postgresql)


*Se deja visible el archivo .env en el proyecto para facilidad de la prueba con las variables de entorno.


Crear database:
    -Crear database llamada kenwin con password '1234'
    -Restaurar database desde archivo "database-backup"


Construir y ejecutar app:
    -Comando: "docker-compose up"


Acceso a la app desde browser:
    http://localhost:8000/

    Login user: augusto
           pwd: 1234



Se dispone de los siguientes endpoints:
    -(POST) API Register: http://localhost:8000/api/register/
    -(POST) API Login: http://localhost:8000/api/login/
    -(GET) API Contats: http://localhost:8000/api/contacts/
    -(POST) API Contacts: http://localhost:8000/api/contacts/

*Se creo el archivo "Kenwin.postman_collection.json" para importar desde Postman para mayor comodidad.

------TESTS-----

Se encuentran dentro de la aplicacion "app". Ejecutar con el comando "python kenwinproject/manage.py tests"
