import math
def main():
    #escribe tu código abajo de esta línea
    area = float(input("Area a pintar en metros: "))
    rendimiento = float(input("Rendimiento (m2/l): "))
    litros = int(math.ceil(area/rendimiento))
    print("Litros a comprar: "+str(litros))
if __name__ == '__main__':
    main()
