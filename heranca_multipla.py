class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas

    def __str__(self):
        return f"============================\n{self.__class__.__name__}:\n{', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}\n============================\n"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

    def __str__(self):
        return "ave 42"

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, num_patas):
        # Como o python lida com a ordem das classes superiores (pais, avós etc)
        # print(Ornitorrinco.__mro__)
        # print(Ornitorrinco.mro())

        super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, num_patas=num_patas)

gato = Gato(num_patas=4, cor_pelo="Preto")
# print(gato)

ornitorrinco = Ornitorrinco(num_patas=4, cor_pelo="Marrom", cor_bico="Laranja")
print(ornitorrinco)