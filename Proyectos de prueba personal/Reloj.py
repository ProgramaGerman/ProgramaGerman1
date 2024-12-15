import time, datetime

try:
    while True:
        ahora = datetime.datetime.now().strftime("%H:%M:%S")
        print("\rHora actual: {}".format(ahora), end="")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nReloj detenido")

