

class Clientes:
    def __init__(self,nome, idade) -> None:
        self.nome=nome
        self.idade=idade
        
    def __repr__(self) -> str:
        return f'Clientes({self.nome}, {self.idade})'
class Book:
    def __init__(self,livro=dict) -> None:
        self.livro=livro
        
        
    def __repr__(self) -> str:
        return f'Book({self.livro})'

class Bibilioteca(Clientes,Book):

    def __init__(self,clientes: list[Clientes]|None= None,livro: list[Book]|None= None):
        self.clientes=clientes or []
        self.livro=livro or []
        self.escolha=None
        
        self.todos=[ {'titulo': 'Os miseraveis', 'autor': 'Victor Hugo'},
            {'titulo': 'A teoria de Tudo', 'autor': 'stephen hawking'},
            {'titulo': 'Homem aranha', 'autor': 'autor2'},
            {'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien'}]
        
     
        self.disponiveis=[ {'titulo': 'Os miseraveis', 'autor': 'Victor Hugo'},
            {'titulo': 'A teoria de Tudo', 'autor': 'stephen hawking'},
            {'titulo': 'Homem aranha', 'autor': 'autor2'},
            {'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien'}]
        
        self.emprestado= []
        self.livro_escolhido= True
        
        self.menu={
                '1': {'nome': 'ListaLivros', 'funcao':self.menuBibiliotaca },
                '2': {'nome': 'checarDisponiveis', 'funcao':self.checardisponiveis},
                '3': {'nome': 'Devolver L', 'funcao':self.devolverLivro}
                }
        self.opcoes=['1','2','3']

       
    def exibirMenu(self):
        for opcao in self.opcoes:
           print(f"{opcao}. {self.menu[opcao]['nome']}")
        escolha = input("Digite a função desejada: ")
        return escolha
    def menuBibiliotaca(self):
        
       
        for i, opçao in enumerate(self.disponiveis):
            opçoes=opçao['titulo']
            print(f"{i}) {opçoes}")

    def checardisponiveis(self,c,l):
            
        while True:
            self.escolha=input('escolha um Livro... ')
            for i in range(len(self.todos)):
                if self.escolha  in self.todos[i]['titulo']:
                        self.livro_escolhido=False
            if self.escolha== 'voltar':
                break
            if  self.livro_escolhido:
                print('Desculpe, mas nao possuimos esse livro no momento...')
                print()
                print('Escolha outro Livro ou digite "VOLTAR", Para retornar Menu anterior') 
            
            for i in self.todos:
                
                if self.escolha == i['titulo']:
                    livro_escolhido=i

                    self.livro_escolhido=True
                
                    if  livro_escolhido in self.emprestado:
                        print(f'{livro_escolhido['titulo']}:livro nao disponivel')
                        return
                
                    if livro_escolhido not in self.emprestado:
                        print(f'{livro_escolhido['titulo']}:livro disponivel')
                        return
                    
    

    def devolverLivro(self,c,l):
                
        self.autenticar(c,l)
        print('Olá Henrique')
        print()
        print('Digite o nome do Livro que deseja Devolver...')
        escolha = input('digite o nome do LIVRO:\n')
        for i in self.livro:
            s=i.livro['titulo']
            
            if s == escolha:
                l1=i.livro
                self.disponiveis.remove(l1)
                self.emprestado.append(l1)
                self.livro.remove(i)
                print(self.livro,self.disponiveis,self.emprestado)


    
    def checarCliente(self, cliente):
        if cliente in self.clientes:
            return True
        print('chek_clientes', False)
        return False

    # checar livros
    def checarLivro(self, livro):
        if livro in self.livro:
            print('ok')
            return True
        print('chek_livro', False)
        return False 

    # checar se o livro foi pego pelo cliente
    def verificar_livrocliente(self,cliente,livro):
             if livro in cliente.livro:
                  print("verificar_livrocliente",True)
                  return True
             return False

    def autenticar(self,cliente,livro):
        return self.checarCliente(cliente) and self.checarLivro(livro)\
        and self.verificar_livrocliente(cliente,livro)

if __name__=='__main__':
    biblioteca=Bibilioteca()
    c1=Clientes('henrique',23)
    l1= Book({'titulo': 'Os miseraveis', 'autor': 'Victor Hugo'})
    l2= Book({'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien'})
    c1.livro=[l1]

    biblioteca.clientes.extend([c1])
    biblioteca.livro.extend([l1])
    

    while True:
        escolha = biblioteca.exibirMenu()

        if escolha in biblioteca.menu:
            funcao = biblioteca.menu[escolha]['funcao']
            if escolha=='2' or'3' :
             funcao(c1,l1)
            else:
                funcao()
        elif escolha == 'sair':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
        

 
    