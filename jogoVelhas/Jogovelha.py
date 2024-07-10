from teste import Velha
from utils import isNumber
import random
class Jogo(Velha):
    def __init__(self):
        super().__init__()
        self.escolha=None
       
      
     
    def jogadorX(self):
        print('escolha uma casa')
        for linha in self.tab:
            print(" |  ".join(linha))
       
        while True:
            try:
                linha=int(input('linha:'))
                coluna=int(input('coluna: '))
 
                if 0 <=linha <3 and 0<= coluna < 3 :
                
                    if self.tab[linha][coluna] ==' ':
                        self.tab[linha][coluna]='x'
                        self.validar()
                        if self.fim:
                            print(f'FIM DE JOGO! JOGADOR (X) VENCEU')
                            return
                        else:   
                            self.maquina()
                            return
                    
                    print('casa nao disponivel')
                
                print('escolha um numero de entre 0 e 2')
                           
            except ValueError:
                print('favor digite um numero Valido')
            
                

    def jogadorO(self):
        for linha in self.tab:
            print(" |  ".join(linha))
        print('escolha uma casa jogador "O"')
       
        while True:
            try:
                linha=int(input('linha:'))
                coluna=int(input('coluna: '))
                if 0 <=linha <3 and 0<= coluna < 3:
                    self.casa_escolhida=self.tab[linha][coluna]
                
                    if  self.isempty(self.casa_escolhida):
                        self.tab[linha][coluna] ='o'
                        self.validar()
                        if self.fim:
                            print(f'FIM DE JOGO! JOGADOR (O) VENCEU')
                            return
                        else:

                            self.jogadorX()
                            return
                    
                    print('casa nao disponivel')
                
                print('escolha um numero de entre 0 e 2')
            except ValueError:
                print('favor digitar um Numero Valido')
    def maquina(self):
     
         while True:
            try:
                linha=random.randint(0,2)
                coluna=random.randint(0,2)
                if 0 <=linha <3 and 0<= coluna < 3:
                    self.casa_escolhida=self.tab[linha][coluna]
                
                    if  self.isempty(self.casa_escolhida):
                        self.tab[linha][coluna] ='o'
                        self.validar()
                        if self.fim:
                            print(f'FIM DE JOGO! JOGADOR (MAQUINA) VENCEU')
                            return
                        else:
                            self.jogadorX()
                            return
                    
            except ValueError:
                print('favor digitar um Numero Valido')
    
        
    
if __name__=="__main__":
    jogo=Jogo()
    
    
   
    menu={'O':jogo.jogadorO,
          'X': jogo.jogadorX
        }
    while True:
        print('O, jogadorO')
        print('X, jogadorX')
        escolha= input(' Escolha X ou O: ')
        if escolha in menu:
            menu[escolha]()
            break
        else:
            print('opçao invalida')

        
    
    

