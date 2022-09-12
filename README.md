## Pasos a seguir

1. Clonar repositorio

## Configuración backend

#### 1. cd alpha-test-backend 
#### 2. Crear virtual env:
- correr python3 -m venv env en la terminal
#### 3. Activar virtual env:
- source env/bin/activate
#### 4.Instalar requirements.txt:
- pip3 install -r requirements.txt
#### 5. python manage.py migrate
#### 6.Crear superuser para django admin:
- correr python3 manage.py createsuperuser 
- agregar usuario
- agregar contrasena

Esto le dara acceso a el administrador de django.

### 7. Correr el servidor

- python manage.py runserver

### 8. Acceder al administrador y agregar uno o varios usuarios y uno o varios productos. 

- Agregar usuario: Para agregar un usuario debe dar click a Users que se encuentra  debajo de API. 

<img width="1500" alt="image" src="https://user-images.githubusercontent.com/38991514/189585084-5a686bde-186e-41ee-970f-040574b55de1.png">

- Agregar un producto: Para agregar un producto da click a productos --> add producto --> llenar campos correspondientes

<img width="1500" alt="image" src="https://user-images.githubusercontent.com/38991514/189585696-ea028751-380a-40f6-8b0f-16c064f79632.png">

Ya estamos listos para configurar el front end.

## Configuración Front end

### Realizar la configuración en una terminal nueva (dejando corriendo el backend)

#### 1. Dirigirse a la carpeta correspondiente
- cd alpha-test-front

#### 2. Instalar paquetes necesarios
- npm install

#### 3. Correr proyecto
- ng serve

#### 4. Login

- Para poder loggearse debe de utilizar el usuario y clave creado en el paso #8 de la configuración del backend

#### 5. Utilizar calculadora
