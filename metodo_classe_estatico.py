class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data_nascimento(cls, ano, mes, dia, nome): # Desta forma, não preciso instanciar o obj na chamada dele, ver exemplo abaixo
        idade = 2026 - ano
        return cls(nome, idade)


    @staticmethod
    def maior_de_idade(idade):
        return idade >= 18

pessoa = Pessoa.criar_data_nascimento(1995, 4, 15, "Junior")
print(pessoa.nome, pessoa.idade, f"=> {'Maior de idade' if pessoa.maior_de_idade(pessoa.idade) else 'Menor de idade'}")