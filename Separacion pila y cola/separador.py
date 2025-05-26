class Separador:
    def __init__(self, cola, pila):
        self.cola = cola
        self.pila = pila

    def procesar(self):
        # Calculamos la cantidad de elementos iniciales
        longitud = self.cola.final - self.cola.frente
        i = 0
        while i < longitud:
            elemento = self.cola.desencolar()
            if elemento is not None:
                if i % 2 == 0:
                    self.cola.encolar(elemento) # Si es posicion par, regresa a la cola
                else:
                    self.pila.apilar(elemento) # Si es impar, va a la fila
            i += 1