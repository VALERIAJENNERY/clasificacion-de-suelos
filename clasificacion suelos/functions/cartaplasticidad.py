import matplotlib.pyplot as plt #Se importan las librerías necesarias para programar gráficos y funciones
import numpy as np
def carta_de_plasticidad(LL,IP): #Se programa la carta de plasticidad dentro de una función para llamarla en codigos posteriores para clasificación de suelos.
  #Primeramente se establece el rango de valores que puede tener x y y

  x = np.array([0,100])
  y = np.array([0,70])

  #Se establecen los limites de los ejes x y y que se mostrarán en el gráfico.
  plt.xlim(0,100)
  plt.ylim(0,70)

  
  #Se definen las funciones para las lineas A y U de la carta de plasticidad de casagrande.
  IP_lineaA=0.73*(x-20)
  IP_lineaU=0.9*(x-8)

  #Se realiza el código para colocar las lineas A y U en el grafico.

  plt.plot(x,IP_lineaA, 'c', label= "Linea A IP=0.73(LL-20)")
  plt.plot(x,IP_lineaU, 'b', label= "Linea U IP=0.9(LL-8)", linestyle = "dashed")
  #Además, se coloca la línea divisoria vertical en 50 que separa los suelos de baja y alta compresibilidad.
  plt.axvline(50, color="black", linestyle = "dashed", lw=1)
  #Se grafican las lineas horizontales que delimitan la zona ML-CL
  plt.hlines(7,15.7,29.5)
  plt.hlines(4,12.4,25.5)

  #Se grafican los valores de entrada del límite líquido y el índice plástico que se introdujeron.
  plt.plot(LL,IP, marker ="o", color="red")
  plt.grid(color='lightblue', ls ='dotted', lw = 2) #Se coloca la grilla del gráfico y se definen características de la misma.

  # Se le colocan las leyendas de los ejes y el título del gráfico.
  plt.title("CARTA DE PLASTICIDAD DE CASAGRANDE",fontsize=15 , color="violet")
  plt.xlabel("LIMITE LIQUIDO",fontsize=10)
  plt.ylabel("INDICE DE PLASTICIDAD",fontsize=10)

  # Se colocan las leyendas con el tipo de suelo en las áreas correspondientes para interpretar los valores de entrada.
  plt.annotate('CL',(40,20), fontsize=16, color="darkblue") #Para la zona de suelos arcillosos de baja compresibilidad.
  plt.annotate('ML',(40,8), fontsize=16, color="darkblue") #Para la zona de suelos limosos de baja compresibilidad.
  plt.annotate('CH',(60,40), fontsize=16, color="darkblue") #Para la zona de suelos arcillosos de alta compresibilidad.
  plt.annotate('MH',(80,20), fontsize=16, color="darkblue") #Para la zona de suelos limosos de alta compresibilidad.
  plt.annotate('CL-ML',(16,5),fontsize=9,color="darkblue") #Para la zona de suelos arcillosos-limosos de baja compresibilidad.

  #Se colorean las zonas de los diferentes tipos de suelos para dar más estética al gráfico. Para esto se definieron con rangos las zonas específicas.
  a=[20,50,50]
  b=[0,21.9,0]
  plt.fill(a,b,'pink') #Para la zona de suelos limosos de baja compresibilidad.
  c=[12.44,25.48,29.59,15.78]
  d=[4,4,7,7]
  plt.fill(c,d,'lightgreen') #Para la zona de suelos arcillosos-limosos de baja compresibilidad.
  e=[15.78,29.59,50,50]
  f=[7,7,21.9,37.8]
  plt.fill(e,f,'turquoise') #Para la zona de suelos arcillosos de baja compresibilidad.
  g=[50,50,85.77,100,100]
  h=[21.9,37.8,70,70,58.4]
  plt.fill(g,h,'yellow') #Para la zona de suelos arcillosos de alta compresibilidad.
  l=[50,50,100,100]
  m=[0,21.9,58.4,0]
  plt.fill(l,m,'violet') #Para la zona de suelos limosos de alta compresibilidad.
  plt.legend()
  plt.show() #Se solicita que muestre el grafico señalado.

#Se imprime como interpretar los resultados del gráfico.
  print()
  print("PARA INTERPRETAR LOS RESULTADOS")
  print()
  print("Si el punto rojo que en el area:")
  print(" -Verde, el suelo es un CL-ML (Arcilla-Limo de baja compresibilidad)")
  print(" -Turquesa, el suelo es un CL (Arcilla de baja compresibilidad)")
  print(" -Rosa, el suelo es un ML (Limo de baja compresibilidad)")
  print(" -Amarilla, el suelo es un CH (Arcilla de alta compresibilidad)")
  print(" -Violeta, el suelo es un MH (Limo de alta compresibilidad)")
  print(" -Blanca, el suelo no existe ")
  print()
  print()