import pandas as pd #Se importa la librería necesaria para realizar la tabla para la clasificación de suelos.
import matplotlib.pyplot as plt #Se importan las librerías necesarias para programar gráficos y funciones
import numpy as np

#Se establece la primera columna que contiene los nombres de los tamices.  
Tamiz= pd.Series([
    'N° 4',
    'N° 10',
    'N° 20',
    'N° 30',
    'N° 40',
    'N° 60',
    'N° 140',
    'N° 200',

])
#Se coloca los tamaños de las aperturas de los tamices correspondientes a la columna anterior.
Apertura =pd.Series([
    
    4.75,
    1.9,
    0.85,
    0.600,
    0.425,
    0.25,
    0.16,
    0.075,
])
#Se definen las variables de los porcentajes retenidos en cada tamiz.
Porc_Retenido_Tamiz4 = 30  #Porcentaje retenido en el tamiz número 4
Porc_Retenido_Tamiz10=20   #Porcentaje retenido en el tamiz número 10
Porc_Retenido_Tamiz20=10 #Porcentaje retenido en el tamiz número 20
Porc_Retenido_Tamiz30=15  #Porcentaje retenido en el tamiz número 30
Porc_Retenido_Tamiz40=2 #Porcentaje retenido en el tamiz número 40
Porc_Retenido_Tamiz60=1  #Porcentaje retenido en el tamiz número 60
Porc_Retenido_Tamiz140=13 #Porcentaje retenido en el tamiz número 140
Porc_Retenido_Tamiz200=1  #Porcentaje retenido en el tamiz número 200

#Se realiza una matriz con los valores de las variables correspondientes a los porcentajes retenidos.
Porcentajes_retenidos=[Porc_Retenido_Tamiz4,Porc_Retenido_Tamiz10,Porc_Retenido_Tamiz20,Porc_Retenido_Tamiz30,Porc_Retenido_Tamiz40,Porc_Retenido_Tamiz60,Porc_Retenido_Tamiz140,Porc_Retenido_Tamiz200]
# Se establece la columna de porcentajes retenidos para la tabla
Retenida =pd.Series(Porcentajes_retenidos)

#Se definen las variables de los porcentajes de la muestra que pasan por cada tamiz tomando en cuenta los valores ingresados para los porcentajes retenidos.
Porc_Pasa_Tamiz4=100-Porc_Retenido_Tamiz4 #Porcentaje que pasa por el tamiz número 4
Porc_Pasa_Tamiz10=Porc_Pasa_Tamiz4-Porc_Retenido_Tamiz10 #Porcentaje que pasa por el tamiz número 10
Porc_Pasa_Tamiz20=Porc_Pasa_Tamiz10-Porc_Retenido_Tamiz20 #Porcentaje que pasa por el tamiz número 20
Porc_Pasa_Tamiz30=Porc_Pasa_Tamiz20-Porc_Retenido_Tamiz30 #Porcentaje que pasa por el tamiz número 30
Porc_Pasa_Tamiz40=Porc_Pasa_Tamiz30-Porc_Retenido_Tamiz40 #Porcentaje que pasa por el tamiz número 40
Porc_Pasa_Tamiz60=Porc_Pasa_Tamiz40-Porc_Retenido_Tamiz60 #Porcentaje que pasa por el tamiz número 60
Porc_Pasa_Tamiz140=Porc_Pasa_Tamiz60-Porc_Retenido_Tamiz140 #Porcentaje que pasa por el tamiz número 140
Porc_Pasa_Tamiz200=Porc_Pasa_Tamiz140-Porc_Retenido_Tamiz200 #Porcentaje que pasa por el tamiz número 200

#Se realiza una matriz con los valores de las variables correspondientes a los porcentajes que pasan los tamices.
Porcentajes_Pasa=[Porc_Pasa_Tamiz4,Porc_Pasa_Tamiz10,Porc_Pasa_Tamiz20,Porc_Pasa_Tamiz30,Porc_Pasa_Tamiz40,Porc_Pasa_Tamiz60,Porc_Pasa_Tamiz140,Porc_Pasa_Tamiz200]
# Se establece la columna de porcentajes que pasan para la tabla
Pasa=pd.Series(Porcentajes_Pasa)

#Se realiza la tabla con las tres columnas antes mencionadas.
Estructura = pd.DataFrame({
    'Tamiz':Tamiz,
    'Apertura':Apertura,
    '% Retenido':Retenida,
    '% Pasa':Pasa,
    

})
#Se imprime la tabla.
print(Estructura)

apertura_tamiz = [] # Se crea una matriz vacia para la apertura de tamices
posicion = [60, 30, 10] #Se crea una matriz con los porcentajes a los que deseamos estimar.
diametro = [] # Se crea otra matriz vacia.
for i in (0,1,2): # Se comienza un ciclo con el rango determinado.
  for  k in range(0, len(Pasa)): # Se genera otro ciclo con un rango desde cero hasta la extension de la lista de porcentajes pasa.
    if Pasa[k] <= posicion[i]: #Se coloca un condicional que relaciona los valores de porcentajes que pasa y la porcentajes a estimar.
      diametro.append(k) # Se añade el valor de K a la lista creada para el valor correspondiente a las aperturas.
      break # Se rompe el ciclo. 
      #Se utiliza una formula para logral la interpolacion.
  formula = (posicion[i]-Pasa[diametro[i]])*(Apertura[diametro[i]-1]-Apertura[diametro[i]])/(Pasa[diametro[i]-1]-Pasa[diametro[i]])+Apertura[diametro[i]] 
  apertura_tamiz.append(formula) # Se añado el valor obtenido de la formula a la lista apertura tamiz antes creada
d60 = apertura_tamiz[0] #Se define el d60
d30 = apertura_tamiz[1] # Se define el d30
d10 = apertura_tamiz[2] # Se define el d10

CU=d60/d10 #Calculamos el coeficiente de curvatura.
CC=(d30**2)/(d10*d60) # Calculamos el coeficiente de uniformidad. 

# Imprimimos los datos anteriormente hallados:
print("El 60% pasa por un tamiz de apertura (mm): ", d60) 
print("El 30% pasa por un tamiz de apertura (mm): ", d30)
print("El 10% pasa por un tamiz de apertura (mm): ", d10)
print("El coeficiente de curvatura es: ", CC)
print("El coeficiente de uniformidad es: ", CU)

#Se crea una función para realizar el gráfico de la curva granulométrica de una muestra de suelo.
def curva_granulometrica():
  plt.figure(figsize=(14, 4)) 
#Se definen los limites de las curvas. 
  a=[37.5,25,19,9.5,4.74,2,0.425,0.075] #Valores de las aperturas de los tamices que seran el eje x de la grafica
  b=[100,75,65,45,30,15,7,0] #Valores para el límite inferior de la curva admisible para bases granulares, valores en y
  c=[100,100,90,68,50,32,20,9] #Valores para el límite superior de la curva admisible para bases granulares, valores en y
  plt.plot(a,b,'m',linestyle = "dashed") #Se grafica la curva para el limite inferior admisible para bases granulares.
  plt.plot(a,c,'m',linestyle = "dashed") #Se grafica la curva para el limite superior admisible para bases granulares.
  plt.plot(a,Estructura['% Pasa'],'red',lw=2)#Se grafica la curva del suelo de muestra tomando en cuenta los valores de entrada colocados en la tabla.
  plt.grid(color='grey', ls ='dotted', lw = 2) #Se graica la grilla del grafico.
  plt.xscale("log") #Se cambia el eje x a una escala logaritmica.
 
   
 

  #Se colocan las leyendas de los ejes del gráfico.
  plt.xlabel("Apertura de Tamices (mm)", fontsize=10)
  plt.ylabel("% de suelo que pasa", fontsize=10)


  #Se coloca el titulo del gráfico
  plt.title("GRAFICA GRANULOMÉTRICA PARA BASES GRANULARES",fontsize=15 , color="purple")
  plt.legend() 
  #Se invierte el grafico.
  ax1 = plt.gca()
  ax1.invert_xaxis()
  ax2 = ax1.twiny()
  #se establece la escala logaritmica
  ax2.set_xscale('log')
  #Se colocan legendas al grafico
  ax2.set_xticks(Apertura)
  ax2.set_xticklabels(Tamiz, rotation=90, fontsize=8)
  #Se colocan legendas al grafico
  ax2.set_xlabel('Tamices')
  ax2.set_xlim(0.075,4.75)
  ax2.invert_xaxis()
  #Se establecen los valores donde apareceran las leyendas
  L_No10 = ([4.75,4.75]) 
  L_No20 = ([2,2]) 
  L_No40 = ([0.850,0.850]) 
  L_No60 = ([0.425,0.425])
  L_No140 = ([0.106,0.106])  
  L_rango = ([0,100])
  #Se establece la estetica de las leyendas anteriormente definidas
  plt.plot(L_No10, L_rango, color='b', lw='0.8', ls='--')
  plt.plot(L_No20, L_rango, color='b', lw='0.8', ls='--') 
  plt.plot(L_No40, L_rango, color='b', lw='0.8', ls='--')
  plt.plot(L_No60, L_rango, color='b', lw='0.8', ls='--')
  plt.plot(L_No140, L_rango, color='b', lw='0.8', ls='--')
  #Se establece la estetica de las leyendas anteriormente definidas
  plt.text(4.75, 2, 'Grava(Fina)',color='b', fontsize=8, rotation=90)
  plt.text(1.95, 2, 'Arena(Gruesa)', color='b',fontsize=8, rotation=90)
  plt.text(0.415, 2, 'Arena(Mediana)', color='b',fontsize=8, rotation=90)
  plt.text(0.075, 2, 'Arena(Fina)', color='b',fontsize=8, rotation=90)
  x_values = [4, 3, 2, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08]
  for x in x_values:
      plt.axvline(x=x, color='grey', ls='-', lw='0.3')

  #Se muestra el gráfico
  plt.show()
  #Se imprime un texto para la interpretación del gráfico
  print()
  print("Para que el suelo sea apto para una base granular debe acoplarse la grafica dentro de las franjas establecidas.")
curva_granulometrica()