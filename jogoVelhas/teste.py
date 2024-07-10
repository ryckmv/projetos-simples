
class Velha:
    def __init__(self):
        self.tab=[[' ',' ',' '],
                  [' ',' ',' '],
                  [' ',' ',' ']]
    
        self.fim=False
        for linha in self.tab:
            print("  |  ".join(linha))
        

    def isempty(self,string:str):
        return string==' '

    def validar(self):
        n=len(self.tab)
        for j in range(len(self.tab)-1):
            if not self.isempty(self.tab[j][j]):
                if self.tab[j][j] == self.tab[j+1][j+1]==self.tab[j-1][j-1]:
                    self.fim=True
                    return
        for i in range(n):
            self.diag_contraria=self.tab[i][n-1-i]
            if not self.isempty(self.diag_contraria):
                if self.tab[0][2] == self.tab[1][1]==self.tab[2][0]:
                    self.fim=True
                    print('s')
                    return
                
        
              
        for linha in self.tab:
            for j in range(len(linha)-1):
                
                if not self.isempty(linha[j]):
                 if linha[j] == linha[j+1] == linha[j-1]  :
                    self.fim=True
                    print('s')
                    return
                
        for i in range(len(self.tab)):
         for j in range(len(self.tab)):
            if not self.isempty(self.tab[i][j]):
                if self.tab[0][j] == self.tab[1][j]== self.tab[2][j]:
                    print(self.tab[i][j])
                    return
        
                
                
                    
                    
                   
                      
                
             
                        
                               
                    
                        
                    


if __name__=="__main__":
        velha=Velha()
        velha.validar()