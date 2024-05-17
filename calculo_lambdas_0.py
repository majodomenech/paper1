# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:45:31 2024

@author: mariajose
"""

#####################
# calculo de lambda_0
#####################

import numpy as np
import matplotlib.pyplot as plt


#-------------CONFIGURACIÓN---------------------------------------

# Ruta para guardar datos de x y p(x)
pwd_xy = 'C:/Users/mariajose/Documents/GitHub/datos_xy/'
#nombre_datos = {100: 'delta_44990_100_10E6_1_2024-05-07-01-33-47', 
#                1000: 'delta_44990_1000_10E6_1_2024-05-07-03-07-08',
#                5000: 'delta_44990_5000_10E6_09tf',
#                10000: 'delta_44990_10000_10E6_concatenado1'}

nombre_datos = {#100: 'delta_8990_100_10E6_1_2024-05-06-16-59-52', 
                #1000: 'delta_8990_1000_10E6_09tf',
                5000: 'delta_8990_5000_10E6_1_2024-05-07-14-50-40',
                #10000: 'delta_8990_10000_10E6_concatenado1'
                }

a = 8990
title = True

save_fig = True
pwdgraf = 'C:/Users/mariajose/Documents/GitHub/graficos/'
nombre_archivo = 'deltas_a_fijo_CON_LAMBDA0_'+str(a)+'_zoom'

#----------------------------------------------------------------


def alpha(a,N):
    return (a+1)/(N+a)
             
lambda_0 = []
y_lambda_0 = []

delta_maxs = []

#=====================
fig = plt.figure(figsize = [7.4, 5.8],layout='tight' )
                          #[11.6, 4.8] [9.8, 3.8]

ax1 = fig.add_subplot(111)
#=====================

for numero,nombre in nombre_datos.items():
    
    x = np.loadtxt(pwd_xy+'x_'+nombre+'.txt')
    p_delta = np.loadtxt(pwd_xy+'y_'+nombre+'.txt')
    
    delta_maxs.append(np.amax(p_delta))

    x = x.astype(int)

    for i in x:
        
        print(i)
        
        j=i-2
        print('diferencia p(i)-p(i+2)   ', abs(np.log(p_delta[j])-np.log(p_delta[j+2])))
        print('diferencia p(i+1)-p(i+3) ', abs(np.log(p_delta[j+1])-np.log(p_delta[j+2])))
        print('promedio                 ', (abs(np.log(p_delta[j])-np.log(p_delta[j+2]))+abs(np.log(p_delta[j+1])-np.log(p_delta[j+2])))/2)
        print('diferencia p(i)-p(i+1)   ', abs(np.log(p_delta[j])-np.log(p_delta[j+1])))
        
        if (abs(np.log(p_delta[j])-np.log(p_delta[j+2]))+abs(np.log(p_delta[j+1])-np.log(p_delta[j+2])))/2 >= 2 * abs(np.log(p_delta[j])-np.log(p_delta[j+1])):
        
            lambda_0.append(i)
            y_lambda_0.append(p_delta[j])
            break
    
    # Genera colores aleatorios para cada punto
    color = np.random.rand(3)
    
    delta_maxs_array = np.array(delta_maxs)
    p_delta00 = np.amax(delta_maxs_array)
    
    alfa = alpha(a,numero)
    ax1.scatter(x, p_delta/p_delta00, marker='D', facecolor='none', edgecolor=color, s=10, label = f'N={numero}, {round(alfa,4)}')


ax1.scatter(lambda_0,y_lambda_0/p_delta00, marker='o', color='black', s=15)

if title == True:
    aa = a
    
    lambda_0_dadovuelta = lambda_0[::-1]
    ax1.set_title(f'a = {aa}, $\\lambda_0$={lambda_0_dadovuelta}')


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
ax1.legend(fontsize = 10)
#ax1.set_xlim(0.5, lim_escala)    

ax1.set_ylim(0.0005, 10)
ax1.set_xlim(0.9, 200)    
        

if save_fig == True:
    #fig.savefig(pwdgraf+nombre_archivo+'.pdf', format='pdf')
    fig.savefig(pwdgraf+nombre_archivo, dpi=600)
    
print(lambda_0)
print(y_lambda_0)