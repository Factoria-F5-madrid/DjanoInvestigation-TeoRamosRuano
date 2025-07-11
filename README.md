# **Djano Investigation-TeoRamosRuano**
---
---
# Investigación y Desarrollo de un CRUD con Django

## Parte 1: Aplicación CRUD y Django

---

### 1. ¿Qué es un CRUD y cuál es su propósito en el desarrollo de aplicaciones web?

**CRUD** es el acrónimo de:
- **C**reate (Crear)
- **R**ead (Leer)
- **U**pdate (Actualizar)
- **D**elete (Eliminar)

Estas operaciones son fundamentales en cualquier aplicación que gestione datos. Permiten a los usuarios interactuar con los registros de la base de datos de forma dinámica y controlada.

#### Ejemplo: **GitHub**

- **Crear:** El usuario crea repositorios y.
- **Leer:** Los visitantes pueden ver todas las entradas del blog.
- **Actualizar:** El autor puede editar el contenido de una entrada.
- **Eliminar:** El autor puede eliminar entradas que ya no desea mostrar.

Cada operación corresponde directamente a una acción del CRUD y se realiza sobre un modelo, por ejemplo, `Post`.

---

### 2. ¿Qué son los patrones de arquitectura en desarrollo de software?

Los **patrones de arquitectura** son estructuras organizativas que definen cómo se divide y organiza el código de una aplicación. Ayudan a separar responsabilidades y mejorar el mantenimiento, la escalabilidad y la colaboración.

#### ¿Qué es el patrón MVC (Modelo–Vista–Controlador)?

**MVC (Model–View–Controller)** es uno de los patrones más utilizados en el desarrollo web.

- **Modelo (Model):** Representa la estructura de los datos y la lógica de negocio. Se encarga de acceder a la base de datos.
- **Vista (View):** Es la interfaz gráfica que ve el usuario. Muestra la información proveniente del modelo.
- **Controlador (Controller):** Recibe las entradas del usuario (como formularios), las procesa, interactúa con el modelo, y determina qué vista mostrar.

**Ejemplo:**
Un usuario envía un formulario para actualizar su perfil:
- El **controlador** recibe el formulario.
- El **modelo** guarda los datos actualizados en la base de datos.
- La **vista** muestra un mensaje de confirmación.


#### ¿Qué es el patrón MVT (Modelo–Vista–Template)?

**MVT (Model–View–Template)** es el patrón de arquitectura que utiliza Django, muy similar a MVC, pero con diferencias clave:

- **Modelo (Model):** Igual que en MVC, maneja los datos y las reglas del negocio.
- **Vista (View):** Contiene la lógica de la aplicación. Toma decisiones, accede al modelo, y renderiza templates.
- **Template:** Es el HTML que el usuario ve. Contiene etiquetas dinámicas para mostrar datos del modelo.

En Django, la vista (`views.py`) **actúa como el "controlador"** de manera implícita. El sistema de enrutamiento (urls.py) también participa en ese control.

---

#### Diferencias entre MVC y MVT

| Elemento      | MVC                         | MVT (Django)                 |
|---------------|------------------------------|------------------------------|
| Modelo        | `Model` (datos)              | `Model` (datos)              |
| Vista         | `View` (interfaz visual)     | `Template` (interfaz visual) |
| Controlador   | `Controller` (lógica)        | `View` (lógica)              |
---
En resumen:
- En **MVC**, el desarrollador define un **controlador** explícitamente.
- En **MVT**, **Django maneja el controlador internamente** y el desarrollador define la lógica en las vistas (`views.py`).

#### ¿Cuál de estos dos patrones se usa en Django?

Django utiliza el patrón **MVT (Modelo–Vista–Template)**, el cual está diseñado para simplificar el desarrollo al encargarse del "controlador" internamente. Los desarrolladores solo se enfocan en los modelos, las vistas (con lógica) y los templates (interfaz visual).

---

### 3. ¿Cómo se estructura un proyecto en Django?

Un proyecto Django está compuesto por una o más aplicaciones. Cada aplicación sigue una estructura típica:

- **Modelos (`models.py`):** Definen la estructura de los datos (campos, tipos, relaciones).
- **Vistas (`views.py`):** Contienen funciones o clases que responden a solicitudes HTTP.
- **Templates (`.html`):** Archivos que definen cómo se presentan los datos en el navegador.
- **URLs (`urls.py`):** Asocian rutas específicas del navegador con vistas correspondientes.

#### ¿Para qué se usa el signo `{{ }}` y `{% %}` en los templates?

- `{{ variable }}`: Inserta el valor de una variable dentro del HTML.
- `{% tag %}`: Ejecuta lógica de plantilla, como bucles (`for`) o condicionales (`if`).

**Ejemplo:**
```html
<h1>{{ titulo }}</h1>
{% for post in posts %}
  <div>{{ post.contenido }}</div>
{% endfor %}
```
### 4. ¿Cuál es el flujo de datos entre un formulario HTML y la base de datos en Django?

1. El usuario llena un formulario en el navegador.
2. Al enviarlo, Django recibe los datos mediante la solicitud `POST`.
3. La vista procesa esos datos usando las clases `Form` o `ModelForm`.
4. Si los datos son válidos, se guardan en la base de datos a través del modelo.
5. Django redirige al usuario o muestra una página de confirmación.

**Ejemplo:**
```python
from django.shortcuts import render, redirect
from .forms import PostForm

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo post (Create)
            return redirect('listar_posts')  # Redirige a la lista (Read)
    else:
        form = PostForm()
    return render(request, 'crear.html', {'form': form})
```
### 5. ¿Qué herramientas o comandos ofrece Django para facilitar el desarrollo de un CRUD?

| Herramienta / Comando         | Descripción                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| `django-admin startproject`   | Crea un nuevo proyecto Django con la configuración inicial.                |
| `python manage.py startapp`   | Crea una nueva aplicación dentro del proyecto (estructura modular).        |
| `python manage.py makemigrations` | Detecta los cambios en los modelos y genera archivos de migración.        |
| `python manage.py migrate`    | Aplica las migraciones para crear o modificar las tablas en la base de datos. |
| `python manage.py runserver`  | Inicia el servidor de desarrollo local (por defecto en http://127.0.0.1:8000). |
| `ModelForm`                   | Clase que permite generar formularios basados en modelos automáticamente. |
| `admin`                       | Interfaz web incluida que permite realizar operaciones CRUD sobre los modelos registrados. |

---

### 6. ¿Cómo funciona el Admin de Django?

El **Admin de Django** es una interfaz de administración automática que permite a los desarrolladores y administradores gestionar los modelos registrados sin necesidad de escribir código adicional para las operaciones CRUD.

#### ¿Cómo se configura?

1. **Registrar el modelo en `admin.py`:**

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```
---
## Conclusión

Implementar un CRUD con Django es perfecto para gestionar datos en aplicaciones web. Gracias a su arquitectura MVT y herramientas, Django facilita la creación, lectura, actualización y eliminación de información de forma rápida y organizada.
Esto hace que las bases de desarrollo de proyectos web sean robustas y escalables.
