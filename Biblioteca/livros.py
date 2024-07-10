from cliente import Clientes
from bibilioteca import Bibilioteca

class Livros(Bibilioteca):

    def __init__(self,*args,**kwargs):
        super().__init__(args,kwargs)
        
            
        self.emprestarLivro(self.clientes,self.livro)
       

    def __repr__(self) -> str:
        return f'Livros({self.clientes!r})'
               
       

    
    def checardisponiveis(self,c,l):
            
            while True:
                self.escolha=input('escolha um Livro... ')
                for i in range(len(self.todos)):
                    if self.escolha  in self.todos[i]['titulo']:
                            self.livro_escolhido=False

                if  self.livro_escolhido:
                    print('Desculp, mas nao possuimos esse livro no momento')
              
                if self.escolha== 'sair':
                    break
                for i in self.todos:
                    
                    if self.escolha == i['titulo']:
                        livro_escolhido=i
                        self.livro_escolhido=True

                    
                        if  livro_escolhido in self.emprestado:
                            print(f'{livro_escolhido['titulo']}:livro nao disponivel')
                    
                        if livro_escolhido not in self.emprestado:
                            self.emprestado.append(livro_escolhido)
                            self.livro.append(livro_escolhido)
                            self.disponiveis.remove(livro_escolhido)
                            print(self.emprestado)
            self.devolverLivro(c,l)


        
                        
                        
                        
    def checarCliente(self, cliente):
        if cliente in self.clientes:
            print('chekin on')
            return True
        print('chek_clientes', False)
        return False
    def checarLivro(self, livro):
        if livro in self.livros:
            print('chekin on')
            return True
        print('chek_clientes', False)
        return False

    def emprestarLivro(self,c,l):
        nome=input('digite seu Nome: ')
        idade=int(input('digite sua Idade: '))
        c1=Clientes(nome,idade)
        self.clientes.extend([c1])
       
        for i, opçao in enumerate(self.disponiveis):
            opçoes=opçao['titulo']
            print(f"{i}) {opçoes}")
        self.checardisponiveis(c,l)
        
    def autenticar(self,cliente,livro):
        return self.checarCliente(cliente) and self.checarLivro(livro)
        
       

    def devolverLivro(self,c,l):
        nome=input('digite seu Nome: ')
        idade=int(input('digite sua Idade: '))
        for cliente in self.clientes:
            if cliente.nome == nome and cliente.idade == idade:
                self.autenticar(c,l)
                print('Olá Henrique')
                print()
                print('Digite o nome do Livro que deseja Devolver')
                livro=input('')
                for i in self.livro:
                  if livro in i['titulo']:
                    self.disponiveis.append(i)
                    self.emprestado.remove( i)
                    self.livro.remove(i)
                    print(self.livro)
                    
        
      
      
 

if __name__=='__main__':

    book=Livros()


  
   
    c2=Clientes('j',24)
    
