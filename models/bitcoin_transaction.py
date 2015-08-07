# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging
#Get the logger
_logger = logging.getLogger(__name__)

# Importamos la api de bitcoin, debe estar ya instalada en el sistema.
# En caso contrario loggeamos el error.
# Se incluye la api como dependencia externa en el manifiesto. 
try:
    from bitpay.bitpay_client import Client
except ImportError:
    # Aquí deberíamos usar el log de error de odoo
    _logger.error("Dependency missing, couldn't find bitpay-py2. Make sure your sysadmin installs it.")
    


class BitcoinTransaction(models.Model):
    """
    Objeto transacción de bitcoin. 
    No es un objeto que queramos editar a mano.
    """
    _name = 'bitcoin.transaction'

    _rec_name = 
    # bitpay api (2.3.3) returns a unicode string
    btc_due = fields.Float(compute='_compute_transaction')
    btc_paid
    btc_price
    currency
    current_time
    exchange_rate
    exception_status
    expriation_time
    transaction_id
    invoice_time
    payment_url_21
    payment_url_72
    price
    rate
    status 
    token
    url 

    # Realizamos la transacción. De momento sin tener en cuenta la moneda
    @api.depends('price')
    def _compute_transaction(self):
