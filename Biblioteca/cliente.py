class Clientes:
    def __init__(self,nome, idade) -> None:
        self.nome=nome
        self.idade=idade
        
    def __repr__(self) -> str:
        return f'Clientes({self.nome}, {self.idade})'

if __name__=='__main__':

    cliente=Clientes('joao',23)
    