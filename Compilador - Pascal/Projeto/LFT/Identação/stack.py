class Stack:
    def __init__(self):
        self.items = []

    def vazia(self):
        return self.items == []

    def topo(self):
        return self.items[len(self.items)-1]

    def tamanho(self):
        return len(self.items)

    def empilha(self, e):
        self.items.append(e)
        #print(e)
    
    def desempilha(self):
        return self.items.pop()
    
     