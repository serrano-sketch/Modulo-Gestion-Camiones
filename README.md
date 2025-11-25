Gestion de Camiones

Este módulo de Odoo permite administrar paquetes, camiones y el seguimiento de cada envío.
Incluye los modelos solicitados en la tarea, vistas listas para usar y la descripción de las
funciones clave para que otro desarrollador pueda ampliarlo sin dificultad.

Dependencias:
- base, que proporciona los partners usados como remitentes y destinatarios.
- hr, que habilita el modelo hr.employee utilizado para los conductores.

Modelos disponibles:
- transport.truck: matrícula, conductor actual, antiguos conductores (Many2many),
  fecha de última ITV, notas de mantenimiento y lista de paquetes que lleva el camión.
  La función _add_former_driver evita duplicados en el histórico y el método write guarda
  automáticamente al conductor anterior cuando se reasigna el camión.
- transport.package: número de seguimiento (se muestra como código de barras CODE128
  en la vista), remitente, destinatario, dirección completa de entrega, camión actual y
  lista de actualizaciones (One2many con transport.tracking).
- transport.tracking: paquete relacionado, fecha y hora, estado (selección con los hitos
  del envío) y notas. Las actualizaciones se muestran con orden descendente por fecha.

Vistas y menús:
- Menú raíz Gestion de Camiones.
- Submenús Paquetes, Camiones y Seguimientos.
- Cada formulario incluye las listas solicitadas: actualizaciones del envío dentro del paquete
  y paquetes transportados dentro del camión.

Instalación y uso:
1. Copiar la carpeta gestion_camiones a la ruta extra-addons (en este entorno es /home/jcg/odoo_addons).
2. Reiniciar Odoo y actualizar la lista de aplicaciones desde el menú Aplicaciones.
3. Instalar Gestion de Camiones.
4. Crear primero los camiones y los conductores (desde el módulo Empleados).
5. Registrar paquetes y añadir sus actualizaciones desde el cuaderno Actualizaciones.
6. Asignar paquetes a camiones desde la vista del camión o del paquete; al cambiar un conductor,
   el histórico se completa automáticamente.
