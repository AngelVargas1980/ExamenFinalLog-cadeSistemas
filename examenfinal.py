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
        Button (frame, text = 'Respuesta 1', command = self.data).grid(row = 6, columnspan = 5, sticky = W + E)

         #Creamos un segundo boton para ejecutar las operaciones       
        Button (frame, text = 'Respuesta 2', command = self.data).grid(row = 7, columnspan = 5, sticky = W + E)
    
        #designamos un área para mensajes
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        
    # creamos una función para validar que los campos no esten en blanco
    
   
    # esta es la función que ejecuta la división
   
    def data(self):
            
           def dividir(self):
            
           
            
            x=float(self.var1.get())
            y=float(self.var2.get())
            z=float(self.var3.get())

            # esta es la función que ejecuta la operación
            def dividir(self):
                if x<=z:
                    resultado = float( self.var1.get() ) * float( self.var2.get() ) * float(self.var3.get())
                    self.message['text'] = 'Se multiplicaron los 3 valores: {}'.format(dividir)
            
                else:
                    self.message['text'] = 'El segundo numero es mayor : {}'.format(dividir)



            #self.message['text'] = 'Son iguales'
                  


            #elif  x>y:
                #self.message['text'] = 'El segundo numero es mayor : {}'.format(x)
            #else:                               
                #self.message['text'] = 'El primer numero es mayor : {}'.format(y)

            
                

            #if  resultado==0:
                 #self.message['text'] = 'Es exacto el resultado es : {}'.format(divi)
            #else:                               
                #self.message['text'] = 'No es exacto el resultado es : {}'.format(divi)

        #nombre = input ('Ingrese el nombre:')
        #edad = int(input('Ingrese la edad:'))
        #estatura = float(input('Ingrese la estatura:'))
        
    
    
#validamos si estamos en la aplicación inicial
if __name__ == '__main__':
    
    #asignamos la propiedad de tkinter a la variable window
    window = Tk()
    
    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = Desk(window)

    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()
