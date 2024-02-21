from datetime import datetime

fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('res/test.txt', "a") as archivo:
	archivo.write(f'Tarea finalizada a las {fecha_actual}')


