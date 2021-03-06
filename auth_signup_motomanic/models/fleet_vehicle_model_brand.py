# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class FleetVehicleModelBrand(models.Model):
    _name = 'fleet.vehicle.model.brand'
    _inherit = 'fleet.vehicle.model.brand'

    active = fields.Boolean(default=True)
