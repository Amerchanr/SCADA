import ntptime
import time

# Sincronizar hora desde Internet
try:
    ntptime.settime()  # Obtiene la hora desde un servidor NTP
    print("Hora sincronizada desde NTP")
except:
    print("Error obteniendo la hora")

# Ajustar la zona horaria (GMT-5 por ejemplo para Colombia, México, Perú)
TIMEZONE_OFFSET = -5 * 3600  # Ajuste en segundos

# Obtener fecha y hora formateada
def obtener_hora():
    t = time.localtime(time.time() + TIMEZONE_OFFSET)
    fecha_hora = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(*t[:6])
    return fecha_hora
