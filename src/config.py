import os # importa el módulo os para manejar variables de entorno
from dotenv import load_dotenv
load_dotenv()

# ================================
# CONFIGURACIÓN EMAIL / BREVO
# ================================
API_KEY_BREVO = os.getenv("BREVO_API_KEY") # trae la API key desde el archivo .env
EMAIL_ORIGEN = os.getenv("EMAIL_ORIGEN", "info.nexosports@gmail.com") # trae el email origen desde el archivo .env 

#LISTA_SUSCRIPTOS = obtener_suscriptos(API_KEY_BREVO, lista_id=3)

LISTA_SUSCRIPTOS = [
    "scottigui@gmail.com",
    "guido_scotti@hotmail.com",
    #"kiaraagustinatort@gmail.com"
    #"alejandroraul.maldonado@gmail.com",
    #"mariano.swidzinski@gmail.com",
    #"aleciojoel@gmail.com"
    #"joel.alecio@catapultsports.com"
]

LISTA_NO_SUSCRIPTOS = [
    "scottigui@gmail.com",
    "guido_scotti@hotmail.com"
]
