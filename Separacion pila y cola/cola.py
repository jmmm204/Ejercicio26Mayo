class Cola:
    def __init__(self):
        # Creamos un arreglo fijo con 100 elementos
        self.items = [None] * 100
        self.frente = 0 # Inicio de la cola
        self.final = 0 # Final de la cola

    def encolar(self, elemento):
        # Agrega un elemento al final si hay espacio
        if self.final < len(self.items):
            self.items[self.final] = elemento
            self.final += 1

    def desencolar(self):
        # Elimina el elemento de enfrente si no esta vacia
        if self.esta_vacia():
            return None
        elemento = self.items[self.frente]
        self.items[self.frente] = None
        self.frente += 1
        return elemento

    def esta_vacia(self):
        # Verifica si la cola esta vacia
        return self.frente == self.final

    def obtener_elementos(self):
        # Retorna los elementos validos en la cola
        resultado = []
        i = self.frente
        while i < self.final:
            resultado += [self.items[i]]
            i += 1
        return resultado