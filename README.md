# Gestión de Camiones

Este módulo de Odoo permite administrar paquetes, camiones y el seguimiento de cada envío.
Incluye los modelos solicitados en la tarea, vistas listas para usar y la documentación de las
funciones clave para que otro desarrollador pueda ampliarlo sin dificultad.

## Dependencias

- `base`: proporciona los partners que actúan como remitente y destinatario.
- `hr`: habilita el modelo `hr.employee` utilizado para los conductores.

## Modelos disponibles

- `transport.truck`
  - **Campos**: matrícula, conductor actual, antiguos conductores (Many2many), fecha de última ITV,
    notas de mantenimiento y la lista de paquetes que lleva el camión (One2many).
  - **Función `_add_former_driver`**: evita duplicados al almacenar conductores anteriores.
  - **Función `write`**: se sobrescribe para que, al cambiar de conductor, el anterior se añada de
    forma automática al histórico `former_driver_ids`.

- `transport.package`
  - **Campos**: número de seguimiento (representado como código de barras CODE128 en la vista),
    remitente, destinatario, dirección completa de entrega, camión actual y lista de actualizaciones
    (One2many con `transport.tracking`).

- `transport.tracking`
  - **Campos**: paquete relacionado, fecha/hora, estado (selección con los hitos del envío) y notas.
  - **Ordenación**: se muestran primero las actualizaciones más recientes.

## Vistas y menús

- Menú raíz **Gestión de Camiones**.
- Submenús: **Paquetes**, **Camiones** y **Seguimientos**.
- Cada formulario incluye las listas en árbol solicitadas: actualizaciones del envío dentro del
  paquete y paquetes transportados dentro del camión.

## Instalación y uso

1. Copia la carpeta `gestion_camiones` dentro de una ruta de `extra-addons` (en este entorno ya está
   en `/home/jcg/odoo_addons`).
2. Reinicia el servicio de Odoo y, desde *Aplicaciones*, pulsa **Actualizar lista de aplicaciones**.
3. Instala **Gestión de Camiones**.
4. Crea primero los camiones y conductores (desde el módulo de Empleados).
5. Registra paquetes y añade sus actualizaciones desde el cuaderno "Actualizaciones".
6. Asigna paquetes a camiones desde la vista del camión o del paquete; al cambiar un conductor, el
   histórico se completa automáticamente.

## Publicar el módulo en GitHub

1. Abre una terminal en `/home/jcg/odoo_addons/gestion_camiones`.
2. Inicializa el repositorio: `git init` y añade un `.gitignore` si lo necesitas.
3. Configura Git si es la primera vez: `git config user.name "Tu Nombre"` y
   `git config user.email "tu@email"`.
4. Añade los archivos y crea un commit: `git add .` seguido de `git commit -m "Add transport module"`.
5. En GitHub, crea un repositorio vacío y copia la URL (HTTPS o SSH).
6. Conecta el remoto y sube el código:
   ```bash
   git remote add origin <URL_del_repo>
   git branch -M main
   git push -u origin main
   ```
7. Comparte la URL del repositorio en la entrega para que el profesor pueda revisarlo.

Con estos pasos otro desarrollador puede entender el funcionamiento del módulo y continuar su
extensión sin necesidad de revisar el código completo.
