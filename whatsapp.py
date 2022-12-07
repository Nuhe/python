import pywhatkit

#Enviar mensaje a un solo contacto. Hora y minutos.
pywhatkit.sendwhatmsg("+54 9 11 6940-4994", "Este es un mensaje programado en python para enviar un mensaje a las 10:31", 22, 31)

#Enviar mensaje a un contacto y cerrar tab luego de 2 segundos:
#Sintaxis: numero, mensaje, wait_time, tab_close and close_time
pywhatkit.sendwhatmsn("+1xxxxxxx", "Mensaje", 22, 40, 15, True, 15)

#Enviar mensaje a un grupo
#Sintaxis: id de grupo, mensaje, hora y minutos (Tenes que ser admin del grupo y copiar la ultima parte del link de compartir.) 
pywhatkit.sendwhatmsg_to_group("escribe-id-aqui", "mensaje", 19, 2)