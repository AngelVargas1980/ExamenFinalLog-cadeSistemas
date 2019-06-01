import random
from tkinter import*

raiz= Tk()

aux=10

Contador=0

auxi=[]
Pregunta=StringVar()
miFrame=Frame(raiz,width=500,height=300,background="green")
miFrame.pack()


            
Cajadetex=Entry(miFrame)
Cajadetex.place(x="15", y="100")
def PreguntasHistoria():
    LabelPre=Label(miFrame,text="                                                                                                                                                                                       ",fg="red",font="15",background="skyblue")
    LabelPre.place(x="10", y="25")
    global val
    L=["¿Quién descubrió América?","¿En que año fue que Guatemala se independizo?","¿Cómo se llama el personaje de la biblia que abrió el mar rojo?","¿Cuál se llama el ave nacional de Guatemala?","¿Cómo se llamaba el padre del Alejandro Magno?","¿Quién fue el primer emperador romano?","En que país nació Adolfo Hitler","¿En que fecha se firmo la paz en Guatemala?","¿Por qué se condeno a Galileo Galilei?","¿Quién fue el primer presidente de Guatemala?"]
    valor2=random.randint(0,9)
    
    global Contador
    Contador=0
    Contador=Contador+1
    for i in range(0,10):
        if i==valor2:
            val=L[i]
            LabelPre=Label(miFrame,text=val,fg="red",font="15",background="skyblue")
            LabelPre.place(x="10", y="25")
            

def PreguntasDeportes():
    LabelPre=Label(miFrame,text="                                                                                                                                                                                       ",fg="red",font="15",background="skyblue")
    LabelPre.place(x="10", y="25")
    global val
    global Contador
    L=["¿Quién gano el mundial de Rusia 2018?","¿Cuántos puntos anoto Michel Jordán en su Carrera?","¿Cuántos Mundiales gano Pele?","¿En que equipo fue le mayor esplendor de Babe Ruth?","¿En que equipo juega actualmente Lebrón James ?","¿Quién gano la Eurocopa del 2016?","¿Quién gano el Balón de Oro del 1999?","¿En donde nació Erick Barrondo?","¿En que posición jugaba Peyton Manning?","¿Selección que fue la primera campeona del mundo?"]
    valor2=random.randint(0,9)
    Contador=0
    Contador=Contador+3
    for i in range(0,10):
        if i==valor2:
            val=L[i]
            LabelPre=Label(miFrame,text=val,fg="red",font="15",background="skyblue")
            LabelPre.config(justify="left")
            LabelPre.place(x="5", y="25")
def PreguntaArte():
    LabelPre=Label(miFrame,text="                                                                                                                                                                                       ",fg="red",font="15",background="skyblue")   
    LabelPre.place(x="10", y="25")
    global val
    L=["¿Cuál es la obra artística mexica más grande?","¿Cuántas pinturas se conocen de Da Vinci?","¿En que ciudad se encuentra la capilla sixtina?","¿Quién hizo la escultura de David?","¿Quién pinto la Mona Lisa?","¿Qué ciudad está plasmada en la noche estrellada de van Gogh?","¿Qué artista hizo un holograma de Alice Cooper?","¿Qué pintor intentó matar a Trotsky?","¿Quién escribió la Quinta Sinfonia?","¿En que año nació Freddie Mercury?"]
    valor2=random.randint(0,9)
    
    global Contador
    Contador=0
    Contador=Contador+2
    for i in range(0,10):
        if i==valor2:
            val=L[i]
            LabelPre=Label(miFrame,text=val,fg="red",font="15",background="skyblue")
            LabelPre.place(x="10", y="25")
def PreguntaCiencia():
    
    LabelPre=Label(miFrame,text="                                                                                                                                                                                       ",fg="red",font="15",background="skyblue")   
    LabelPre.place(x="10", y="25")
    global val
    L=["¿Con que respira una ballena?","¿Por qué están formados los cromosomas?","¿Conversión un miligramo a gramos?","¿Raíz de 144?","¿La velocidad con la que viaja la luz es?","¿Partícula subatómica con carga negativa?","¿Partícula subatómica con carga positiva?","¿El sol es una estrella, planeta o satélite?","¿Cuál es la principal función de los glóbulos rojos?","¿Quién desarrollo la ley de la gravedad?"]

    valor2=random.randint(0,9)
    
    global Contador
    Contador=0
    Contador=Contador+4
    for i in range(0,10):
        if i==valor2:
            val=L[i]
            LabelPre=Label(miFrame,text=val,fg="red",font="15",background="skyblue")
            LabelPre.place(x="10", y="25")




    
def Comparaciones():

  
 global aux
 global Contador
 global val

 if not aux<=0:
   if Contador==1:
    
    auxi=["¿Quién descubrió América?","¿En que año fue que Guatemala se independizo?","¿Cómo se llama el personaje de la biblia que abrió el mar rojo?","¿Cuál se llama el ave nacional de Guatemala?","¿Cómo se llamaba el padre del Alejandro Magno?","¿Quién fue el primer emperador romano?","En que país nació Adolfo Hitler","¿5En que fecha se firmo la paz en Guatemala?","¿Por qué se condeno a Galileo Galilei?","¿Quién fue el primer presidente de Guatemala?"]
    if val== auxi[0] and Cajadetex.get()=="Cristobal Colon" or val==auxi[1] and Cajadetex.get()=="1821" or val==auxi[2] and Cajadetex.get()=="Moises"or val==auxi[3] and Cajadetex.get()=="Quetzal" or val==auxi[4] and Cajadetex.get()=="Filipo II de Macedonia" or val==auxi[5] and Cajadetex.get()=="Cesar Augusto" or val==auxi[6] and Cajadetex.get()=="Austria" or val==auxi[7] and Cajadetex.get()=="29 de Diciembre de 1996" or val==auxi[8] and Cajadetex.get()=="Por decir que la tierra giraba alrededor del sol" or val==auxi[9] and Cajadetex.get()=="Mariano Rivera Paz" :                          

             LabelPre2=Label(miFrame,text="                                            ",fg="green",background="black",font="15")
             LabelPre2.place(x="10", y="250")
             aux=aux+2
            
             LabelPre2=Label(miFrame,text="PUNTOS:   "+str(aux),fg="green",background="black",font="15")
             LabelPre2.place(x="10", y="250")
    else:
        
             LabelPre2=Label(miFrame,text="                                            ",fg="green",background="black",font="15")
             LabelPre2.place(x="10", y="250")
             aux=aux-2
            
             LabelPre2=Label(miFrame,text="PUNTOS:   "+str(aux),fg="green",background="black",font="15")
             LabelPre2.place(x="10", y="250")

    
   if Contador==2:
    
    auxi=["¿Cuál es la obra artística mexica más grande?","¿Cuántas pinturas se conocen de Da Vinci?","¿En que ciudad se encuentra la capilla sixtina?","¿Quién hizo la escultura de David?","¿Quién pinto la Mona Lisa?","¿Qué ciudad está plasmada en la noche estrellada de van Gogh?","¿Qué artista hizo un holograma de Alice Cooper?","¿Qué pintor intentó matar a Trotsky?","¿Quién escribió la Quinta Sinfonia?","¿En que año nació Freddie Mercury?"]
    if val== auxi[0] and Cajadetex.get()=="monolito de Tlaltecuhtli" or val==auxi[1] and Cajadetex.get()=="15" or val==auxi[2] and Cajadetex.get()=="En el Vaticano"or val==auxi[3] and Cajadetex.get()=="Miguel Angel" or val==auxi[4] and Cajadetex.get()=="Leonardo Da Vinci" or val==auxi[5] and Cajadetex.get()=="Saint Remy de Provence" or val==auxi[6] and Cajadetex.get()=="Salvador Dali" or val==auxi[7] and Cajadetex.get()=="David Alfaro Siqueiros" or val==auxi[8] and Cajadetex.get()=="Ludwig van Beethoven" or val==auxi[9] and Cajadetex.get()=="1946" :    
             LabelPre2=Label(miFrame,text="                                           ",fg="green",background="black",font="15")
             LabelPre2.place(x="10", y="250")
             aux=aux+2
            
             LabelPre2=Label(miFrame,text="PUNTOS:   "+str(aux),fg="green",background="black",font="15")
             LabelPre2.place(x="10", y="250")
    else:
        
             
             LabelPre2=Label(miFrame,text="                                            ",fg="green",background="black",font="15")
             LabelPre2.place(x="10", y="250")
             aux=aux-2
            
             LabelPre2=Label(miFrame,text="PUNTOS:   "+str(aux),fg="green",background="black",font="15")
             LabelPre2.place(x="10", y="250")
            
              
     
   if Contador==3:
    
    auxi=["¿Quién gano el mundial de Rusia 2018?","¿Cuántos puntos anoto Michel Jordán en su Carrera?","¿Cuántos Mundiales gano Pele?","¿En que equipo fue le mayor esplendor de Babe Ruth?","¿En que equipo juega actualmente Lebrón James ?","¿Quién gano la Eurocopa del 2016?","¿Quién gano el Balón de Oro del 1999?","¿En donde nació Erick Barrondo?","¿En que posición jugaba Peyton Manning?","¿Selección que fue la primera campeona del mundo?"]
    if val== auxi[0] and Cajadetex.get()=="Francia" or val==auxi[1] and Cajadetex.get()=="32,292" or val==auxi[2] and Cajadetex.get()=="3"or val==auxi[3] and Cajadetex.get()=="NY Yankees" or val==auxi[4] and Cajadetex.get()=="En los Angeles Lakers" or val==auxi[5] and Cajadetex.get()=="Portugal" or val==auxi[6] and Cajadetex.get()=="Rivaldo" or val==auxi[7] and Cajadetex.get()=="San Cristobal Verapaz" or val==auxi[8] and Cajadetex.get()=="Quarterback" or val==auxi[9] and Cajadetex.get()=="Uruguay" :    
             LabelPre2=Label(miFrame,text="                                           ",fg="green",background="black",font="15")
             LabelPre2.place(x="10", y="250")
             aux=aux+2
            
             LabelPre2=Label(miFrame,text="PUNTOS:   "+str(aux),fg="green",background="black",font="15")
             LabelPre2.place(x="10", y="250")
    else:

             LabelPre2=Label(miFrame,text="                                            ",fg="green",background="black",font="15")
             LabelPre2.place(x="10", y="250")
             aux=aux-2
            
             LabelPre2=Label(miFrame,text="PUNTOS:   "+str(aux),fg="green",background="black",font="15")
             LabelPre2.place(x="10", y="250")
             
   if Contador==4:
    
    auxi=["¿Con que respira una ballena?","¿Por qué están formados los cromosomas?","¿Conversión un miligramo a gramos?","¿Raíz de 144?","¿La velocidad con la que viaja la luz es?","¿Partícula subatómica con carga negativa?","¿Partícula subatómica con carga positiva?","¿El sol es una estrella, planeta o satélite?","¿Cuál es la principal función de los glóbulos rojos?","¿Quién desarrollo la ley de la gravedad?"]
    if val== auxi[0] and Cajadetex.get()=="Pulmones" or val==auxi[1] and Cajadetex.get()=="Por ADN" or val==auxi[2] and Cajadetex.get()=="0.001"or val==auxi[3] and Cajadetex.get()=="12" or val==auxi[4] and Cajadetex.get()=="300,000km/s" or val==auxi[5] and Cajadetex.get()=="Electron" or val==auxi[6] and Cajadetex.get()=="Proton" or val==auxi[7] and Cajadetex.get()=="Estrella" or val==auxi[8] and Cajadetex.get()=="Llevar Oxigeno" or val==auxi[9] and Cajadetex.get()=="Isaac Newton":    
             LabelPre2=Label(miFrame,text="                                           ",fg="green",background="black",font="15")
             LabelPre2.place(x="10", y="250")
             aux=aux+2
            
             LabelPre2=Label(miFrame,text="PUNTOS:   "+str(aux),fg="green",background="black",font="15")
             LabelPre2.place(x="10", y="250")
    else:
        
             
             LabelPre2=Label(miFrame,text="                                            ",fg="green",background="black",font="15")
             LabelPre2.place(x="10", y="250")
             aux=aux-2
            
             LabelPre2=Label(miFrame,text="PUNTOS:   "+str(aux),fg="green",background="black",font="15")
             LabelPre2.place(x="10", y="250")


            


btnHistoria=Button(miFrame,text="Historia",command=PreguntasHistoria)
btnHistoria.place(x="15", y="150")

btnDeportes=Button(miFrame,text="Deportes",command=PreguntasDeportes)
btnDeportes.place(x="100", y="150")

btnArte=Button(miFrame,text="Arte",command=PreguntaArte)
btnArte.place(x="190", y="150")

btnMatematicas=Button(miFrame,text="Ciencias",command=PreguntaCiencia)
btnMatematicas.place(x="250", y="150")

btnAceptar=Button(miFrame,text="Aceptar",command=Comparaciones)
btnAceptar.place(x="150", y="98")


raiz.mainloop()

