
from datetime import datetime, timedelta, timezone

 

now = datetime.now()
print(f"fecha y hora actual: {now}")

# crear una fecha y hora especifica
specific_date = datetime(2026, 1, 14, 15, 30)
print(f"mi cumpleaños es en: {specific_date}")

# formatear fechas
# metodo strftime ()
# pasarle el objeto datetime y el formato especificado
# formato: https://docs.python.org/es/3.9/library/datetime.html#strftime-and-strptime-behavior

format_date = now.strftime("%d/%m/%y")
print(f"fecha formateada: {format_date}")

format_date = now.strftime("%d-%m-%y %H:%M:%S")
print(f"fecha formateada: {format_date}")

# operaciones con fechas (sumar/restar días, minutos, horas, meses)
# timedelta representa un intervalo de tiempo, es la "cantidad" de dias, horas, meses, que le vamos a restar/sumar a otra fecha

yesterday = datetime.now() - timedelta(days=1)
print(f"Ayer: {yesterday}")

last_Week = datetime.now() - timedelta(weeks=1, hours=2)
print(f"semana pasada: {last_Week}")

one_hour_after = datetime.now() + timedelta(hours=1)
print(f"una hora después: {one_hour_after}")

# diferencia entre dos fechas

fecha1 = datetime(2026, 2, 1)
fecha2 = datetime(2026, 2, 4)

diferencia = fecha2 - fecha1 # el tipo es timedelta
print(diferencia)

# obtener valores especificos (porque son objetos)

t = timedelta(days=1, hours=5, minutes=30)

print(t.days)          # solo días
print(t.seconds)       # segundos restantes del día
print(t.total_seconds()) 


# traducir

import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') # español españa

format_date = now.strftime("%A %B %Y %H:%M:%S")
print(f"fecha formateada: {format_date}")