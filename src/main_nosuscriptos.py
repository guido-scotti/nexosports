# -*- coding: utf-8 -*-
"""
Informe Promocional de Noticias – Versión de Difusión
Objetivo: captar nuevos suscriptores para el servicio mensual de informes de NEXO SPORTS.
Adaptado para envío mediante Brevo (Sendinblue).
"""

import datetime
from config import LISTA_NO_SUSCRIPTOS, EMAIL_ORIGEN, API_KEY_BREVO
from email_construction import email_nosuscriptos
from email_sending import enviar_email

asunto_email = f"Conectamos profesionales. Impulsamos clubes."

# ================================
# LLAMADO A LA FUNCIÓN DE EMAIL
# ================================
mensaje = email_nosuscriptos()

# ================================
# ENVIO POR BREVO
# ================================
enviar_email(LISTA_NO_SUSCRIPTOS, mensaje, asunto_email, EMAIL_ORIGEN, API_KEY_BREVO)