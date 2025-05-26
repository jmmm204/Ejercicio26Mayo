class Pila:
    def __init__(self):
        # Arreglo fijo para simular la pila
        self.items = [None] * 100
        self.tope = 0 # Marca el siguiente espacio libre

    def apilar(self, elemento):
        # Agrega un elemento en la parte superior
        if self.tope < len(self.items):
            self.items[self.tope] = elemento
            self.tope += 1

    def desapilar(self):
        # Elimina y retorna el elemento del tope si no esta vacia
        if self.esta_vacia():
            return None
        self.tope -= 1
        return self.items[self.tope]

    def esta_vacia(self):
        # Verifica si la pila esta vacia
        return self.tope == 0

    def obtener_elementos(self):
        # Retorna los elementos en orden LIFO
        resultado = []
        i = self.tope - 1
        while i >= 0:
            resultado += [self.items[i]]
            i -= 1
        return resultado