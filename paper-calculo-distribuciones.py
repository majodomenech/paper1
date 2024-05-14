# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:49:20 2024

@author: mariajose
"""

import numpy as np
import matplotlib.pyplot as plt
#--------------------

# Directorio donde están los datos
#pwd = 'C:/Users/mariajose/Desktop/archivos-para-ccad/simulaciones-Durga/simulaciones-BUENAS/09/'
#pwd = 'C:/Users/mariajose/Desktop/archivos-para-ccad/simulaciones-Durga/simulaciones-BUENAS/1N/'
pwd = 'C:/Users/mariajose/Documents/GitHub/simulaciones/'

# Importar datos
#data0 = np.loadtxt(pwd+'/simulaciones-a-fijo/delta_44990_1000_10E6_1_2024-05-07-03-07-08.txt')
data0 = np.loadtxt(pwd+'/simulaciones-a-fijo/delta_44990_10000_10E6_concatenado1.txt')

distrib = 'delta'
#distrib = 'retorno'

# Ruta para guardar datos de x y p(x)
pwd_xy = 'C:/Users/mariajose/Documents/GitHub/datos_xy/'
save_datos = False
nombre_datos = 'delta_44990_10000_10E6_concatenado1'

color0 ='gold'
marker0 = 'D'


if distrib == 'delta':
    #------------------- configuración ----------------
    datadelta=data0
    lim_escala=100000

    # Ruta para guardar graficos
    #pwdgraf = 'C:/Users/mariajose/Desktop/graficos_tf/'
    #save_fig = False
    #nombre_archivo = 'AJUSTES_09_norm-val-max_10000'
    #---------------------


    # Filtrar los valores mayores a lim_escala
    datadelta = datadelta[datadelta <= lim_escala]

    print('valor máximo de x: ', np.amax(datadelta).astype(int))

    p_delta = []
    for i in range(2,np.amax(datadelta).astype(int)+1):
        p_delta.append(np.sum(datadelta == i))
        
    
    p_delta = np.array(p_delta)
    x = np.linspace(2,np.amax(datadelta).astype(int),np.amax(datadelta).astype(int)-1)
    
    #mask = p_delta != 0     # Máscara booleana que quita los puntos del histograma que valdrían cero 
    #x = x[mask]      # (joden al calcularles el log pq log(0) es menos inf)
    #p_delta = p_delta[mask]
    
    print(x.shape,p_delta.shape)


    if save_datos == True:
    
        np.savetxt(pwd_xy+'x_'+nombre_datos+'.txt',x)
        np.savetxt(pwd_xy+'y_'+nombre_datos+'.txt',p_delta)

    #=====================
    fig = plt.figure(figsize = [10.5, 3.9],layout='tight' )
                              #[11.6, 4.8] [9.8, 3.8]

    ax1 = fig.add_subplot(121)
       
    ax1.scatter(x, p_delta, marker=marker0, facecolor='none', edgecolor=color0, s=10)
    
    #===================== PARÁMETROS AX1

    ax1.yaxis.set_ticks_position('both')
    ax1.tick_params(labelleft=True,labelright=False)
    ax1.xaxis.set_ticks_position('both')
    ax1.tick_params(labelbottom=True,labeltop=False)
    # Aumentar el tamaño de la fuente en los ejes
    #ax1.tick_params(axis='x', labelsize=18, length=6, width=1)
    #ax1.tick_params(axis='y', labelsize=18, length=6, width=1)
    # Configurar las marcas menores en el eje y
    ax1.tick_params(axis='y', which='minor', size=3)
    ax1.yaxis.set_ticks_position('both')
    ax1.tick_params(labelleft=True,labelright=False)
    ax1.xaxis.set_ticks_position('both')
    ax1.tick_params(labelbottom=True,labeltop=False)
    #ax1.set_title("distribución deltas (fluctuation lenght)")
    ax1.set_yscale('log')
    ax1.set_xscale('log')
    ax1.set_xlabel('$\lambda$',fontsize = 10)
    ax1.set_ylabel('$P(\lambda)/P(\lambda_{máx})$', fontsize = 10)
    #plt.xticks(fontsize = 15)
    #ax1.legend(fontsize = 10)
    #ax1.set_xlim(0.5, lim_escala)

elif distrib == 'retorno':
    #------------------- configuración ----------------
    dataretorno=data0
    lim_escala=100000

    # Ruta para guardar graficos
    #pwdgraf = 'C:/Users/mariajose/Desktop/graficos_tf/'
    #save_fig = False
    #nombre_archivo = 'AJUSTES_09_norm-val-max_10000'
    #---------------------
    
    # Filtrar los valores mayores y menores a lim_escala
    dataretorno = dataretorno[dataretorno <= lim_escala]
    dataretorno = dataretorno[dataretorno >= -lim_escala]
    
    print('valor máximo de x: ', np.amax(dataretorno).astype(int))
    print('valor mínimo de x: ', np.amin(dataretorno).astype(int))

    #p_retorno = []

    #for i in range(np.amin(dataretorno).astype(int),np.amax(dataretorno).astype(int)+1):
        
        #print(i)
    #    p_retorno.append(np.sum(dataretorno == i))
        
    #p_retorno = np.array(p_retorno)

    #x = np.linspace(np.amin(dataretorno).astype(int),np.amax(dataretorno).astype(int),(-np.amin(dataretorno)+np.amax(dataretorno)).astype(int)+1)

    #print(x)
    #print(p_retorno)
    
    #mask = p_delta != 0     # Máscara booleana que quita los puntos del histograma que valdrían cero 
    #x = x[mask]      # (joden al calcularles el log pq log(0) es menos inf)
    #p_delta = p_delta[mask]
    
    #print(x.shape,p_retorno.shape)
    
    x = np.loadtxt(pwd_xy+'x_'+nombre_datos+'.txt')
    p_retorno = np.loadtxt(pwd_xy+'y_'+nombre_datos+'.txt') 

    if save_datos == True:
    
        np.savetxt(pwd_xy+'x_'+nombre_datos+'.txt',x)
        np.savetxt(pwd_xy+'y_'+nombre_datos+'.txt',p_retorno)
        
       
    
    #=====================
    fig = plt.figure(figsize = [10.5, 3.9],layout='tight' )
                              #[11.6, 4.8] [9.8, 3.8]

    ax1 = fig.add_subplot(121)
       
    ax1.scatter(x, p_retorno, marker=marker0, facecolor='none', edgecolor=color0, s=10)
    
    #===================== PARÁMETROS AX1

    ax1.yaxis.set_ticks_position('both')
    ax1.tick_params(labelleft=True,labelright=False)
    ax1.xaxis.set_ticks_position('both')
    ax1.tick_params(labelbottom=True,labeltop=False)
    # Aumentar el tamaño de la fuente en los ejes
    #ax1.tick_params(axis='x', labelsize=18, length=6, width=1)
    #ax1.tick_params(axis='y', labelsize=18, length=6, width=1)
    # Configurar las marcas menores en el eje y
    ax1.tick_params(axis='y', which='minor', size=3)
    ax1.yaxis.set_ticks_position('both')
    ax1.tick_params(labelleft=True,labelright=False)
    ax1.xaxis.set_ticks_position('both')
    ax1.tick_params(labelbottom=True,labeltop=False)
    #ax1.set_title("distribución deltas (fluctuation lenght)")
    ax1.set_yscale('log')
    #ax1.set_xscale('log')
    ax1.set_xlabel('$\lambda$',fontsize = 10)
    ax1.set_ylabel('$P(\lambda)/P(\lambda_{máx})$', fontsize = 10)
    #plt.xticks(fontsize = 15)
    #ax1.legend(fontsize = 10)
    ax1.set_xlim(-100,100)
    