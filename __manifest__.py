# -*- coding: utf-8 -*-
{
    'name': 'Gestion de Camiones',
    'version': '1.0',
    'category': 'Operations/Logistics',
    'summary': 'Gestión de paquetes, camiones y actualizaciones de envío.',
    'description': 'Permite controlar paquetes, camiones y el seguimiento detallado de envíos.',
    'author': 'Tu Nombre',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/transport_menu.xml',
        'views/transport_package_views.xml',
        'views/transport_tracking_views.xml',
        'views/transport_truck_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
