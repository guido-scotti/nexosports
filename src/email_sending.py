import time
import schedule
from sib_api_v3_sdk import Configuration, ApiClient, ContactsApi
from sib_api_v3_sdk.api.transactional_emails_api import TransactionalEmailsApi
from sib_api_v3_sdk.models import SendSmtpEmail
from email.message import EmailMessage
import datetime

# =============================
# CONFIGURACIÓN
# =============================
API_KEY_BREVO = "TU_API_KEY"  
EMAIL_ORIGEN = "info.nexosports@gmail.com"
LISTA_ID = 3  # ID de lista de Brevo
hoy = datetime.datetime.today().strftime("%d/%m/%Y")
asunto_email = f"Conectamos profesionales. Impulsamos clubes."


# =============================
# FUNCIÓN DE ENVÍO DE EMAIL
# =============================
def enviar_email(destinatarios, mensaje, asunto_email, EMAIL_ORIGEN, API_KEY_BREVO):
    configuration = Configuration()
    configuration.api_key['api-key'] = API_KEY_BREVO
    api_instance = TransactionalEmailsApi(ApiClient(configuration))

    html_email = mensaje.get_body(preferencelist=('html')).get_content()
    texto_plano = mensaje.get_body(preferencelist=('plain')).get_content()

    for i, destinatario in enumerate(destinatarios, start=1):
        email_data = SendSmtpEmail(
            to=[{"email": destinatario}],
            sender={"name": "NEXO SPORTS", "email": EMAIL_ORIGEN},
            subject=asunto_email,
            html_content=html_email,
            text_content=texto_plano,
            reply_to={"email": EMAIL_ORIGEN, "name": "NEXO SPORTS"}
        )
        try:
            response = api_instance.send_transac_email(email_data)
            print(f"✅ Email {i} enviado a {destinatario}")
        except Exception as e:
            print(f"❌ Error al enviar a {destinatario}: {e}")