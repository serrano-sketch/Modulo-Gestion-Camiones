from odoo import api, fields, models


class TransportTruck(models.Model):
    """Representa un camión y conserva el histórico de conductores."""

    _name = 'transport.truck'
    _description = 'Camión de transporte'
    _rec_name = 'license_plate'

    license_plate = fields.Char(string='Número de matrícula', required=True)
    current_driver_id = fields.Many2one('hr.employee', string='Conductor actual')
    former_driver_ids = fields.Many2many(
        'hr.employee',
        'transport_truck_driver_rel',
        'truck_id',
        'employee_id',
        string='Antiguos conductores'
    )
    last_inspection_date = fields.Date(string='Fecha última ITV')
    maintenance_notes = fields.Text(string='Notas de mantenimiento')
    package_ids = fields.One2many('transport.package', 'truck_id', string='Paquetes transportados')

    _sql_constraints = [
        ('license_plate_unique', 'unique(license_plate)', 'La matrícula debe ser única.'),
    ]

    def write(self, vals):
        """Guarda el conductor saliente en el histórico cuando se reasigna."""
        previous_drivers = {}
        if 'current_driver_id' in vals:
            for truck in self:
                if truck.current_driver_id:
                    previous_drivers[truck.id] = truck.current_driver_id.id
        result = super().write(vals)
        if 'current_driver_id' in vals:
            for truck in self:
                previous_driver_id = previous_drivers.get(truck.id)
                current_driver_id = truck.current_driver_id.id if truck.current_driver_id else False
                if previous_driver_id and previous_driver_id != current_driver_id:
                    truck._add_former_driver(previous_driver_id)
        return result

    def _add_former_driver(self, driver_id):
        """Añade el conductor indicado al histórico evitando duplicados."""
        if driver_id and driver_id not in self.former_driver_ids.ids:
            self.former_driver_ids = [(4, driver_id)]


class TransportPackage(models.Model):
    """Contiene la información del paquete y su entrega."""

    _name = 'transport.package'
    _description = 'Paquete'
    _rec_name = 'tracking_number'

    tracking_number = fields.Char(string='N.º de seguimiento', required=True)
    sender_id = fields.Many2one('res.partner', string='Remitente')
    recipient_id = fields.Many2one('res.partner', string='Destinatario')
    delivery_country_id = fields.Many2one('res.country', string='País de entrega')
    delivery_state_id = fields.Many2one('res.country.state', string='Región')
    delivery_city = fields.Char(string='Municipio')
    delivery_street = fields.Char(string='Calle')
    delivery_street_number = fields.Char(string='Número')
    delivery_extra_info = fields.Text(string='Datos adicionales')
    truck_id = fields.Many2one('transport.truck', string='Camión actual')
    update_ids = fields.One2many('transport.tracking', 'package_id', string='Actualizaciones del envío')

    _sql_constraints = [
        ('tracking_number_unique', 'unique(tracking_number)', 'El número de seguimiento debe ser único.'),
    ]


class TransportTracking(models.Model):
    """Registra cada estado del envío del paquete."""

    _name = 'transport.tracking'
    _description = 'Actualización de envío'
    _order = 'entry_date desc'

    package_id = fields.Many2one('transport.package', string='Paquete', required=True, ondelete='cascade')
    entry_date = fields.Datetime(string='Fecha', default=fields.Datetime.now, required=True)
    state = fields.Selection(
        [
            ('created', 'Creado'),
            ('in_transit', 'En tránsito'),
            ('hub', 'En centro logístico'),
            ('incident', 'Incidencia'),
            ('delivered', 'Entregado'),
            ('returned', 'Devuelto'),
        ],
        string='Estado',
        default='created',
        required=True,
    )
    notes = fields.Text(string='Notas adicionales')
