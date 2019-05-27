import turtle
import random

class Circuito():
    corredores=[]
    __posStartY = (-60,-20,20,60)
    __colorTurtle = ('red','green','blue','orange')
    
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
        self.__screen = turtle.Screen()
        self.__screen.setup(width,height)
        self.__screen.bgcolor('lightgray')
        self.__starline = -width/2 +60
        self.__finisline = width/2 -60
        
        self.__createRunners()
      
    def __createRunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__starline, self.__posStartY[i])
            
            
            self.corredores.append(new_turtle)
            
    def Competir(self):
        
        hayGanador = False
        
        while not hayGanador:
            for tortuga in self.corredores:
                avance =random.randint(1,6)
                tortuga.forward(avance)
                
                if tortuga.position()[0] >= self.__finisline:
                    hayGanador = True
                    print("La tortuga de color {} ha ganado".format(tortuga.color()[0]))
        
if __name__ == '__main__':
    circuito=Circuito(640,480)
    circuito.Competir()