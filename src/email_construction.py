
from email.message import EmailMessage
from config import EMAIL_ORIGEN
# ==============================
asunto_email = f"Conectamos profesionales. Impulsamos clubes."

# ===================================
# ARMADO DEL MAIL PROMOCIONAL
# ===================================
def email_nosuscriptos():

    mensaje = EmailMessage()
    mensaje["Subject"] = asunto_email
    mensaje["From"] = EMAIL_ORIGEN
    mensaje.set_content("Newsletter de Nexo Sports – Conectamos profesionales. Impulsamos clubes.")

    mensaje.add_alternative(f"""
    <html>
    <body style="margin: 0; padding: 0; font-family: 'Trebuchet MS', 'Verdana', 'Arial', sans-serif; background-color: #ffffff;">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #ffffff; padding: 20px 0;">
        <tr>
            <td align="center">
            <table width="600" cellpadding="0" cellspacing="0" style="width:100%; background-color: #ffffff;">
                        <!-- Header -->
                <tr>
                <td style="background-color: #17664B; padding: 0; text-align: center;">
                    <img src="https://guido-scotti.github.io/nexosports/src/img/bannerNexo.png"
                        alt="Banner Nexo Sports"
                        style="width: 100%; display: block; border: 0;">
                </td>
                </tr>
                    <table width="100%" cellpadding="0" cellspacing="0">
                        <tr>
                        <td style="padding-left: 30px; padding-top: 30px; padding-bottom: 30px;">
                            <h3 style="margin: 0; font-size: 18px; font-weight: light; color: #000000; font-family: 'Verdana';">Bienvenido a</h3>
                            <h1 style="margin: 0; font-size: 38px; font-weight: 800; color: #1E40AF; font-family: 'Trebuchet MS';">NEXO SPORTS</h1>
                            <p style="margin: 0; font-size: 18px; font-weight: bold; color: #17A3D0; font-family: 'Trebuchet MS';">Conectamos profesionales. Impulsamos clubes.</p>
                        </td>
                        </tr>
                    </table> 
                            
                <tr>
                <td style="padding: 30px;">
                    <h2 style="margin: 0 0 12px 0; font-size: 18px; font-weight: 600; color: #000000; font-family: 'Verdana';">Hola!</h2>
                    <p style="margin: 0; font-size: 16px; line-height: 1.6; color: #000000; font-family: 'Verdana';">
                    Bienvenido a <span style="color: #17A3D0; font-weight: bold;">NEXO SPORTS</span>, el punto de encuentro entre los profesionales 
                    del deporte y los clubes que los necesitan. Nuestro objetivo es impulsar el crecimiento del sector conectando talento con 
                    oportunidades: <strong>si buscás dar el próximo paso en tu carrera o fortalecer el equipo de tu club</strong>, este espacio es para vos.
                    Suscribite para recibir oportunidades laborales, historias inspiradoras y tendencias de la industria deportiva.
                    </p>
                </td>
                </tr>  
                
                    <tr>
                        <td align="center" style="padding: 20px 0;">
                            <table width="80%" cellpadding="0" cellspacing="0" border="0">
                                <tr>
                                    <td style="border-top:1px solid #000000; font-size:0; line-height:0;">&nbsp;</td>
                                </tr>
                            </table>
                        </td>
                    </tr>   

                    <tr>
                        <td align="center" style="padding: 0 30px 30px 30px;">
                            <h1 style="margin: 20px 0 10px 0; font-size: 28px; font-weight: 600; color: #000000; font-family: 'Trebuchet MS';">
                            ¡La suscripción es gratuita!
                            </h1>

                            <a href="https://4c9caead.sibforms.com/serve/MUIFABbYSgP18fasIENUcwcDDnI89HEis5gHeny8Qx5A2g2aH5SL-axPFvL9yzAgHofT8EwQEzvNpMbNsJ3emsWTlUuDlDldJtOsf72wNmjsy7gQU70vyINhhhdP-j7v4cBLHByqkPsdJ65l3R5s7lCx7-lKQFY3hpNLutyAnoZA5zl8E7Fc2Ln2YA-0Tb38FLzHoppC3q9Nm50_tg=="
                            style="display:inline-block; background-color:#17A3D0; color:white; padding:15px 30px;
                            text-decoration:none; border-radius:22px; font-size:18px; margin-top:15px; margin-bottom:15px; font-family: 'Trebuchet MS';">
                            <strong>SUSCRIBIRME AHORA</strong>
                            </a>
                        </td>
                    </tr>              
               <tr>
                <td style="padding: 30px; background-color: #07264F; color: #ffffff; text-align: center;">
                    <table width="100%" cellpadding="0" cellspacing="0" style="margin: 0 auto;">
                    <tr>
                        <td align="center">
                        <h1 style="margin: 0 0 16px 0; font-size: 24px; font-weight: 700; font-family: 'Trebuchet MS';">
                            ¡Contáctanos!
                        </h1>

                        <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0">
                            <tr>
                                <td align="center" style="padding: 0 9px;">
                                <a href="https://www.instagram.com/nexosportshr/" target="_blank" style="display:inline-block;">
                                    <img src="https://guido-scotti.github.io/nexosports/src/img/instagramlogo.png" width="28" height="28" alt="Instagram"
                                        style="display:block; border:0; background-color:#07264F;">
                                </a>
                                </td>
                                <td align="center" style="padding: 0 4px;">
                                <a href="https://www.facebook.com/profile.php?id=61583495402971" target="_blank" style="display:inline-block;">
                                    <img src="https://guido-scotti.github.io/nexosports/src/img/facebook.png" width="32" height="32" alt="Facebook"
                                        style="display:block; border:0;">
                                </a>
                                </td>
                                <td align="center" style="padding: 0 6px;">
                                <a href="https://www.linkedin.com/company/infototalcripto/" target="_blank" style="display:inline-block;">
                                    <img src="https://guido-scotti.github.io/nexosports/src/img/linkedinblanco.png" width="36" height="36" alt="LinkedIn"
                                        style="display:block; border:0;">
                                </a>
                                </td>
                            </tr>
                            </table>

                        <!-- derechos -->
                        <p style="margin: 12px 0 6px 0; font-size: 13px; color: #ffffffcc; font-family: Verdana, sans-serif;">
                            © 2025 <strong>Info Total Cripto</strong>. Todos los derechos pertenecen a sus respectivas fuentes.
                        </p>

                        <!-- link suscripción -->
                        <a href="https://4c9caead.sibforms.com/serve/MUIFABbYSgP18fasIENUcwcDDnI89HEis5gHeny8Qx5A2g2aH5SL-axPFvL9yzAgHofT8EwQEzvNpMbNsJ3emsWTlUuDlDldJtOsf72wNmjsy7gQU70vyINhhhdP-j7v4cBLHByqkPsdJ65l3R5s7lCx7-lKQFY3hpNLutyAnoZA5zl8E7Fc2Ln2YA-0Tb38FLzHoppC3q9Nm50_tg=="
                            style="color: #17A3D0; text-decoration: none; font-size: 13px; font-family: Verdana, sans-serif;">
                            Suscribirse ahora
                        </a>
                        </td>
                    </tr>
                    </table>
                </td>
                </tr>
            </table>
        </td>
        </tr>
        </table>
    </body>
    </html>
    """, subtype='html')
    return mensaje
