from cola import Cola
from pila import Pila
from separador import Separador

def main():
    cola = Cola()
    pila = Pila()

    # Solicita al usuario los elementos de entrada
    print("Ingrese los elementos de la cola (escriba 'fin' para terminar):")
    while True:
        dato = input("Elemento: ")
        if dato.lower() == 'fin':
            break
        cola.encolar(dato)

    # Procesa los elementos separando pares/impares
    separador = Separador(cola, pila)
    separador.procesar()

    # Muestra el resultado
    print("Cola (elementos en posiciones pares):", cola.obtener_elementos())
    print("Pila (elementos en posiciones impares):", pila.obtener_elementos())

if __name__ == "__main__":
    main()