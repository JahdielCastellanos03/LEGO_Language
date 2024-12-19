# Código generado desde LEGO
def main():
    x = 7
    if (x < 10):
        contador_externo = 0
        for _ in range(2):
            print("Inicio del bucle externo.")
            contador_medio = 0
            for _ in range(3):
                print("Inicio del bucle medio.")
                contador_interno = 0
                while (contador_interno < 4):
                    print("Bucle interno:")
                    print("Externo:")
                    print(contador_externo)
                    print("Medio:")
                    print(contador_medio)
                    print("Interno:")
                    print(contador_interno)
                    contador_interno = (contador_interno + 1)
                print("Fin del bucle interno.")
                contador_medio = (contador_medio + 1)
            print("Fin del bucle medio.")
            contador_externo = (contador_externo + 1)
        print("Fin del bucle externo.")
        print("x no es menor que 10")
    else:
        if (x == 7):
            print("x es igual a 7")

if __name__ == '__main__':
    main()