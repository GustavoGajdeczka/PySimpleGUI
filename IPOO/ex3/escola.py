import ast
class aluno:
    def __init__(self):
        self.nome = None
        self.endereco = None
        self.nota = []
        self.Media = None
    
    def cadastra(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def verifica(self):
        if not self.nome:
            if not self.Media:
                return False, False
        else:
            if not self.Media:
                return True, False
            else:
                return True, True
    def setNota(self, nota):
        self.nota.append(nota)
    def media(self):
        self.Media = 0
        for x in self.nota:
            self.Media = self.Media + x
        self.Media = self.Media / 4
        return self.Media
    def imprimeDados(self):
        return self.nome, self.endereco, self.Media