# NexoSports – Email Automation System (Python)

NexoSports es un sistema en desarrollo pensado para automatizar comunicaciones para clubes, academias e instituciones deportivas.  
Actualmente, el módulo principal funcional es el **envío de correos electrónicos** usando Python y la API de Brevo, con plantillas HTML atractivas y adaptables.

El objetivo del sistema es evolucionar hacia una plataforma completa de gestión, perfiles y notificaciones.

---

## 🚀 Estado del Proyecto

El proyecto **está en desarrollo**, pero ya incluye:

- ✔️ Envío de emails totalmente funcional  
- ✔️ Integración con la API de Brevo  
- ✔️ Construcción automática del cuerpo HTML del correo  
- ✔️ Plantillas con diseño atractivo + imágenes embebidas  
- ✔️ Manejo básico de errores en el envío  

---

## 🛠️ Tecnologías Utilizadas

- **Python 3**
- **Brevo API (Sendinblue)** para el envío de correos
- Email programming con HTML/CSS incrustado
- Librerías:
  - `requests`
  - `dotenv`
  - `json`
  - `os`

---

## 📁 Estructura del Proyecto

/nexosports
│
├── .env # Variables de entorno (API Key Brevo)
├── .gitignore # Archivos ignorados en el repo
├── src/
│ ├── config.py # Manejo de claves, paths y configuraciones
│ ├── email_sending.py # Lógica de comunicación con la API de Brevo
│ ├── email_construction.py # Construcción del cuerpo HTML del email
│ ├── main_nosuscriptos.py # Script actual para enviar correos a no suscriptos
│ └── img/ # Imágenes utilizadas dentro de las plantillas
└── README.md

---

## 📩 Funcionalidad Actual

### Envío de Emails con Brevo

El sistema puede enviar correos personalizados a uno o varios destinatarios.

Incluye:

- Asunto configurado dinámicamente  
- Plantilla HTML generada desde Python  
- Imágenes incluidas mediante rutas internas o base64  
- Validación de respuestas de la API  
- Manejo básico de errores (status codes, keys inválidas, etc.)

---

## ▶️ Cómo Ejecutarlo

### 1. Clonar el repositorio
git clone https://github.com/tuusuario/nexosports.git
cd nexosports

### 2. Crear un archivo `.env`
BREVO_API_KEY=tu_api_key_aquí

### 3. Instalar dependencias
pip install -r requirements.txt

### 4. Ejecutar el script principal
python src/main_nosuscriptos.py

---

## 📬 Contacto

Si querés aportar, colaborar o sumar ideas:  
**scottigui@gmail.com**

---

## 📄 Licencia

Proyecto de uso personal.  
Las instituciones interesadas pueden contactarse para implementaciones personalizadas.
