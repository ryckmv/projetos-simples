import random

class Forca:

    def __init__(self):

        self.palavras_aleatoria= ["python", "javascript", "frontend", "backend", "java"]
        self.tentativas=3
        self.chut=3
        self.rodada=0
    
    def escolher_palavra(self):
        self.escolha=random.choice(self.palavras_aleatoria)
        self.palavra=[]
        self.palavra.append(self.escolha)
        self.forca2 = ['_'] * len(self.palavra[0])

     
    def jogo_forca(self):

        while self.tentativas > 0 and '_' in self.forca2:

            self.a=input('digite um letra:')
            self.letra_encontra=False
            for i in self.palavra:
                if  self.a in i:
                    self.letra_encontra=True
                    self.inserir()
                    if  self.fimdejogo():
                        print('FIM DE JOGO !!')
                    break
                if not self.letra_encontra:
                    self.tentativas-=1
                    print(f'Nao temos essa Letra restam {self.tentativas} tentativas')
                if self.tentativas ==0:
                    print(f'Tentativas = {self.tentativas}, Você Perdeu')
                    return
                    

    def fimdejogo(self):
  
        if '_' not in  self.forca2:
                return True
        return False
                    
 
    def inserir(self):
        for i in self.palavra:
            for j in range(len(i)):
                if self.a in i[j]:
                    self.forca2[j]=self.a
        
        self.rodada+=1   
        print(self.forca2)
        if self.rodada > 2:
            self.chute=input('deseja arriscar a qual a palavra?...')
            if self.chute== "sim":
                self.chutes()
                
       
        
    def chutes(self):
        self.joga=input('chute uma palavra:')
        if  self.fimdejogo():
            print('FIM DE JOGO !!')
        if self.chut ==0:
            print(f'Chutes = {self.chut}, Você Perdeu')
            return
            
        else:
            self.chut-=1
            print(f"voce errou!! {self.chut} chutes restantes ")
            
if __name__=='__main__':

    fuerca=Forca()
    fuerca.escolher_palavra()
    
    while True:
        fuerca.jogo_forca()