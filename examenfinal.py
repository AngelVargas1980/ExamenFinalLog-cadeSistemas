#Logica de sistemas
#primer Semestre
#Angel Antonio Vargas Lazaro
#carnet 0907 13 2335

from tkinter import ttk
from tkinter import *

class Desk:
    def __init__(self, window):
        # Initializations
        
        #ancho
        ancho = 800
        
        #alto
        alto = 600
        
        # asignamos la ventana a una variable de la clase llamada wind
        self.wind = window

        #le asignamos el ancho y el alto a la ventana con la propiedad geometry
        self.wind.geometry(str(ancho)+'x'+str(alto))

        #centramos el contenido 
        self.wind.columnconfigure(0, weight=1)
        
        #le damos un titulo a la ventana
        self.wind.title('Aplicación con interface gráfica Angel Vargas')
        
        # creamos un contenedor
        frame = LabelFrame(self.wind, text = 'Ingreso de datos')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        # creamos un etiqueta
        Label(frame, text = 'Valor 1: ').grid(row = 1, column = 0)
        
        #creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)
        
        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'Valor 2: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)
        
        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'Valor 3: ').grid(row = 3, column = 0)
        self.var3 = Entry(frame)
        self.var3.grid(row = 3, column = 1)

        
        #Creamos un boton para ejecutar las operaciones       
        Button (frame, text = 'Respuesta 1', command = self.funcion1).grid(row = 6, columnspan = 5, sticky = W + E)

         #Creamos un segundo boton para ejecutar las operaciones       
        Button (frame, text = 'Respuesta 2', command = self.funcion2).grid(row = 7, columnspan = 5, sticky = W + E)
    
        #designamos un área para mensajes
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        
    # creamos una función para validar que los campos no esten en blanco
    
   
    # esta es la función que ejecuta la operación
   
    def funcion1(self):
            
           #def dividir(self):
                       
            x=float(self.var1.get())
            y=float(self.var2.get())
            z=float(self.var3.get())

            if x < y:
                resultado=x*y*z
                self.message['text'] = 'se multiplicaron los valores el resultado es: {}'.format(resultado)
         
            if x == z:
                resultado=x+y+z
                self.message['text'] = 'se sumaron los valores el resultado es: {}'.format(resultado)

            if  y==0 and x > z:
                 resultado=z-x
                 self.message['text'] = 'se resto el tercero menos el primero resultado es: {}'.format(resultado)
            elif y==0 and z > x:
                resultado=x-z
                self.message['text'] = 'se resto  el primero menos el tercero resultado es: {}'.format(resultado)  
        
    def funcion2(self):   

        x=str(self.var1.get())
        y=str(self.var2.get())
        z=str(self.var3.get())

        x1=float(self.var1.get())
        y1=float(self.var2.get())
        z1=float(self.var3.get())
        r1=x,y,z
        self.message['text'] = 'el mesaje  es: {}'.format(r1)
        resultado=x1+(y1*z1)
        i=0
        while i != resultado :
            self.message['text'] = '{}'.format(r1)
            i=i+1




    
#validamos si estamos en la aplicación inicial
if __name__ == '__main__':
    
    #asignamos la propiedad de tkinter a la variable window
    window = Tk()
    
    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = Desk(window)

    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()
