'''
Jose Manuel Arango 74863
Juan Esteban Alzate 64852
Jhoan Sebastian Ortiz 
Juan Esteban Castillo 68234
'''

class Nodo:
    def __init__(self,matriz,pos_robot,estado,recorrido,marcados):
        """
        matriz = Estado actual del juego
        pos_robot= posición actual del robot x,y (enteros)
        estado = estado de los objetivos nemo, marlin, dori (booleanos)
        """
        self.matriz = matriz
        self.x = pos_robot[0] 
        self.y = pos_robot[1] 
        self.nemo = estado[0] 
        self.marlin = estado[1] 
        self.dori = estado [2]
        self.recorrido = recorrido
        self.marcados = marcados


    def verificar_perdi(self):
        return self.matriz[self.y,self.x] == 3 or self.matriz[self.y,self.x] == 4 or  self.matriz[self.y,self.x] == 8 #Se verifica si colisiona con alguno de los 3 enemigos
    

    def verificar_ganar(self):
        return self.nemo and self.marlin and self.dori #Verificar que encontré los tres objetivos

    def marcar_objetivos(self):
        if  not(self.nemo) and self.matriz[self.y,self.x]==7:
            self.nemo = True
            self.marcados = []
        
        if  self.matriz[self.y,self.x]==6 and not (self.marlin) and self.nemo:
            self.marlin = True
            self.marcados = []

        if self.matriz[self.y,self.x]==5 and self.nemo and self.marlin and not(self.dori):
            self.dori = True
            self.marcados = []


    def generar_hijos(self):
        #Hijo de arriba
        hijos = []
        x = self.x
        y = self.y-1
        
        if y >= 0 and not((x,y) in self.marcados) and self.matriz[y,x]!=1: #Verificar que estoy en el tablero
            recorrido = self.recorrido.copy() #Garantizar que sea independiente
            recorrido.append((x,y)) #Agregar la posición actual
            marcados = self.marcados.copy() #Nodos ya visitados
            marcados.append((x,y)) 
            hijo = Nodo(
                self.matriz,
                (x,y),
                (self.nemo,self.marlin,self.dori),
                recorrido,   
                marcados   
            )
            hijo.marcar_objetivos()
            hijos.append(hijo)            
        #Hijo de abajo

        x = self.x
        y = self.y+1
        
        if y < self.matriz.shape[0]  and not((x,y) in self.marcados) and self.matriz[y,x]!=1: #Verificar que estoy en el tablero
            recorrido = self.recorrido.copy() #Garantizar que sea independiente
            recorrido.append((x,y)) #Agregar la posición actual
            marcados = self.marcados.copy() #Nodos ya visitados
            marcados.append((x,y)) 
            hijo = Nodo(
                self.matriz,
                (x,y),
                (self.nemo,self.marlin,self.dori), 
                recorrido,   
                marcados    
            )
            hijo.marcar_objetivos()
            hijos.append(hijo)



        #Hijo de la izquierda

        x = self.x-1
        y = self.y
        
        if x >= 0 and not((x,y) in self.marcados) and self.matriz[y,x]!=1: #Verificar que estoy en el tablero
            recorrido = self.recorrido.copy() #Garantizar que sea independiente
            recorrido.append((x,y)) #Agregar la posición actual
            marcados = self.marcados.copy() #Nodos ya visitados
            marcados.append((x,y)) 
            hijo = Nodo(
                self.matriz,
                (x,y),
                (self.nemo,self.marlin,self.dori), 
                recorrido,       
                marcados
            )
            hijo.marcar_objetivos()
            hijos.append(hijo)
       #Derecha
        x = self.x+1
        y = self.y
        
        if x < self.matriz.shape[1] and not((x,y) in self.marcados) and self.matriz[y,x]!=1: #Verificar que estoy en el tablero
            recorrido = self.recorrido.copy() #Garantizar que sea independiente
            recorrido.append((x,y)) #Agregar la posición actual
            marcados = self.marcados.copy() #Nodos ya visitados
            marcados.append((x,y)) 
            hijo = Nodo(
                self.matriz,
                (x,y),
                (self.nemo,self.marlin,self.dori),  
                recorrido,
                marcados

            )
            hijo.marcar_objetivos()
            hijos.append(hijo)
 
        return hijos