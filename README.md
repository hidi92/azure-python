# ADMINISTRAR RECURSOS DE AZURE CON PYTHON
Esto es un pequeño Script hecho con Python, cuya función es la de administrar algunos de los recursos más básicos de Azure con Python, por el momento únicamente dispone de 3 funcionalidades:
- Crear un grupo de Recursos.
- Eliminar un Grupo de Recursos.
- Crear una máquina virtual (son su red, subnet, etc.).

###### La utilización es bastante sencilla y amigable.

El menú principal conta de estas 3 opciones comentadas más una para limpiar la consola:

#### Crear un grupo de Recursos:
- Te saca una lista de las diferentes regiones donde puedes crear el Grupo de recursos.
- Solamente indicas el nombre que le vas a dar al grupo de recursos y el nombre de la región donde deseas crearla.

#### Eliminar un Grupo de recursos:
- Te lista los grupos de recursos que tienes.
- Solamente tienes que poner el nombre del grupo de recursos que quieres eliminar y se te eliminara con todos los recursos que tengas dentro de este.
- Te saldrá una ventana advirtiendo que este proceso lleva algo de tiempo.

#### Crear una máquina virtual:
- Te lista los grupos de recursos que tienes.
- Solamente tienes que indicar el nombre de la VM a crear, un nombre de usuario y una password (de mínimo 8 caracteres con Mayúsculas, números y símbolos especiales ya que si no dará error).
- Te saldrá una ventana advirtiendo que este proceso lleva algo de tiempo.

> En todas las opciones, por consola te dice el comando que se ha utilizado, para así aprender cuales son estos.

------------


###### Se ira actualizando con más utilidades en la medida de lo posible, quien quiera puede colaborar en la mejora de esta herramienta.
