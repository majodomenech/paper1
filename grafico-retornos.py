
# Importar librerías
import numpy as np
import matplotlib.pyplot as plt
#from scipy import stats

#------------------ configuración ----------------

# Directorio donde están los datos
#pwd = 'C:/Users/mariajose/Desktop/archivos-para-ccad/simulaciones-Durga/simulaciones-BUENAS/'
pwd = 'C:/Users/mariajose/Documents/GitHub/simulaciones/'


a = 10
title = True

def alpha(a,N):
    return (a+1)/(N+a)

# Ruta para guardar graficos
pwdgraf = 'C:/Users/mariajose/Documents/GitHub/graficos/'
save_fig = True
#nombre_archivo = 'retornos_09_norm-val-max'
nombre_archivo = 'retornos_a_fijo_'+str(a)

# Importar datos

#data3 = np.load(pwd+'simulaciones-trabajofinal/SimulacionesOtrosAlpha/retorno_09995_100_10E5.npy') 
#data3 = np.loadtxt(pwd+'simulaciones-a-fijo/retorno_197900_100_10E6_1_2024-05-09-17-33-45.txt')
#data2 = np.loadtxt(pwd+'simulaciones-a-fijo/retorno_197900_1000_10E6_1_2024-05-07-15-31-03.txt')
#data1 = np.loadtxt(pwd+'simulaciones-a-fijo/retorno_197900_5000_10E6_1_2024-05-08-07-02-28.txt')
#data0 = np.loadtxt(pwd+'simulaciones-a-fijo/retorno_197900_10000_10E6_1_2024-05-09-16-30-42.txt')


#data3 = np.loadtxt(pwd+'simulaciones-a-fijo/retorno_44990_100_10E6_1_2024-05-07-01-33-47.txt') 
#data2 = np.loadtxt(pwd+'simulaciones-a-fijo/retorno_44990_1000_10E6_1_2024-05-07-03-07-08.txt')
#data1 = np.loadtxt(pwd+'simulaciones-trabajofinal/09/retorno_09_5000_10E6.txt')
#data0 = np.loadtxt(pwd+'simulaciones-a-fijo/retorno_44990_10000_10E6_concatenado1.txt') 


#data3 = np.loadtxt(pwd+'simulaciones-a-fijo/retorno_8990_100_10E6_1_2024-05-06-16-59-52.txt') 
#data2 = np.loadtxt(pwd+'simulaciones-trabajofinal/09/retorno_09_1000_10E6.txt')
#data1 = np.loadtxt(pwd+'simulaciones-a-fijo/retorno_8990_5000_10E6_1_2024-05-07-14-50-40.txt')
#data0 = np.loadtxt(pwd+'simulaciones-a-fijo/retorno_8990_10000_10E6_concatenado1.txt') 

data3 = np.loadtxt(pwd+'simulaciones-trabajofinal/1N/retorno_001_100_10E6.txt') 
data2 = np.loadtxt(pwd+'simulaciones-a-fijo/retorno_10_1000_10E6_1_2024-05-07-14-06-41.txt')
data1 = np.loadtxt(pwd+'simulaciones-a-fijo/retorno_10_5000_10E6_concatenado1.txt')
#data0 = np.loadtxt(pwd+'simulaciones-a-fijo/delta_8990_10000_10E6_concatenado1.txt') 
data0 = 0




color0 = 'gold'
color1 = 'dodgerblue'#'blue'
color2 = 'lime'
color3 = 'magenta'#'deeppink'

marker0 = 'D'
marker1 = 's'
marker2 = 'o'
marker3 = '^'

label0 = f'$N = 10^4$, {round(alpha(a,10000),4)}'
label1 = f'$N = 5x10^3$, {round(alpha(a,5000),4)}'
label2 = f'$N = 10^3$, {round(alpha(a,1000),4)}'
label3 = f'$N = 10^2$, {round(alpha(a,100),4)}'

lim_grafico = [-20500,20500]
lim_grafico_zoom = [-2000,2000]
lim_grafico_ZOOMZOOM = [-80,80]

#-------------------------------------------------



def grafico_retornos(data0,data1,data2,data3,  lim_grafico,
                     color0,color1,color2,color3,
                     marker0,marker1,marker2,marker3,
                     label0,label1,label2,label3,
                     pwdgraf, save_fig, nombre_archivo,a):

    lim_grafico=lim_grafico

    fig = plt.figure(figsize = [7.4, 5.8], layout='tight')

    ax1 = fig.add_subplot(111)
    binsretorno = np.linspace(lim_grafico[0]-0.5,lim_grafico[1]+0.5,-lim_grafico[0]+lim_grafico[1]+2)

    #==================================
    y_tot, bin_edges_tot = np.histogram(data0, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker0, facecolor='none', edgecolor=color0, s=15, label=label0)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data1, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker1, facecolor='none', edgecolor=color1, s=15, label=label1)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data2, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker2, facecolor='none', edgecolor=color2, s=15, label=label2)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data3, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker3, facecolor='none', edgecolor=color3, s=15, label=label3)#, color='cyan')
    #==================================
    
    #---------------------------------------------------------
    # Aumentar el tamaño de la fuente en los ejes
    ax1.tick_params(axis='x', labelsize=18, length=6, width=1)
    ax1.tick_params(axis='y', labelsize=18, length=6, width=1)

    # Configurar las marcas menores en el eje y
    ax1.tick_params(axis='y', which='minor', size=3)


    ax1.yaxis.set_ticks_position('both')
    ax1.tick_params(labelleft=True,labelright=False)

    ax1.xaxis.set_ticks_position('both')
    ax1.tick_params(labelbottom=True,labeltop=False)

    ax1.set_yscale("log")
    ax1.legend(fontsize = 15)
    #---------------------------------------------------------
    #ax1.set_title('distribución de retornos (log return)')
    #fig.show()
    
    ax1.set_xlabel('$\Delta \lambda$ (retornos)',fontsize = 14)
    ax1.set_ylabel('$P(\Delta \lambda)/P(0)$',fontsize = 14)
    ax1.set_xlim(lim_grafico[0],lim_grafico[1])
    
    if title == True:
        numero = a
        ax1.set_title(f'a = {numero}')
    
    if save_fig == True:
        fig.savefig(pwdgraf+nombre_archivo+'.pdf', format='pdf')

    #fig.savefig('/home/mjdomenech/TrabajoFinal/Figuras/OVERLEAF/resultados-febrero/1-retornos_09_norm-val-max.png', dpi=300)

grafico_retornos(data0,data1,data2,data3,  lim_grafico,
                     color0,color1,color2,color3,
                     marker0,marker1,marker2,marker3,
                     label0,label1,label2,label3,
                     pwdgraf, save_fig, nombre_archivo,a)

def grafico_retornos_zoom(data0,data1,data2,data3,  lim_grafico_zoom,
                     color0,color1,color2,color3,
                     marker0,marker1,marker2,marker3,
                     label0,label1,label2,label3,
                     pwdgraf, save_fig, nombre_archivo,a):

    #ZOOM
    lim_grafico=lim_grafico_zoom
    fig = plt.figure(figsize = [7.4, 5.8], layout='tight')

    ax1 = fig.add_subplot(111)
    binsretorno = np.linspace(lim_grafico[0]-0.5,lim_grafico[1]+0.5,-lim_grafico[0]+lim_grafico[1]+2)

    #==================================
    y_tot, bin_edges_tot = np.histogram(data0, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker0, facecolor='none', edgecolor=color0, s=15, label=label0)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data1, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker1, facecolor='none', edgecolor=color1, s=15, label=label1)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data2, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker2, facecolor='none', edgecolor=color2, s=15, label=label2)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data3, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker3, facecolor='none', edgecolor=color3, s=15, label=label3)#, color='cyan')
    #==================================
    
    # Aumentar el tamaño de la fuente en los ejes
    ax1.tick_params(axis='x', labelsize=18, length=6, width=1)
    ax1.tick_params(axis='y', labelsize=18, length=6, width=1)

    # Configurar las marcas menores en el eje y
    ax1.tick_params(axis='y', which='minor', size=3)

    ax1.yaxis.set_ticks_position('both')
    ax1.tick_params(labelleft=True,labelright=False)

    ax1.xaxis.set_ticks_position('both')
    ax1.tick_params(labelbottom=True,labeltop=False)

    ax1.set_yscale("log")
    ax1.legend(fontsize = 15)
    
    ax1.set_xlabel('$\Delta \lambda$ (retornos)',fontsize = 14)
    ax1.set_ylabel('$P(\Delta \lambda)/P(0)$',fontsize = 14)
    ax1.set_xlim(lim_grafico_zoom[0],lim_grafico_zoom[1])
    #ax1.set_title('distribución de retornos (log return)')
    #fig.show()
    
    if title == True:
        numero = a
        ax1.set_title(f'a = {numero}')

    if save_fig == True:
        fig.savefig(pwdgraf+nombre_archivo+'_zoom'+'.pdf', format='pdf')

    #fig.savefig('/home/mjdomenech/TrabajoFinal/Figuras/OVERLEAF/resultados-febrero/1-retornos_09_norm-val-maxZOOM1.png', dpi=300)

grafico_retornos_zoom(data0,data1,data2,data3,  lim_grafico_zoom,
                     color0,color1,color2,color3,
                     marker0,marker1,marker2,marker3,
                     label0,label1,label2,label3,
                     pwdgraf, save_fig, nombre_archivo,a)

def grafico_retornos_ZOOMZOOM(data0,data1,data2,data3,  lim_grafico_ZOOMZOOM,
                     color0,color1,color2,color3,
                     marker0,marker1,marker2,marker3,
                     label0,label1,label2,label3,
                     pwdgraf, save_fig, nombre_archivo,a):

    #ZOOM ZOOM

    lim_grafico=lim_grafico_ZOOMZOOM
    fig = plt.figure(figsize = [4.4, 3.5], layout='tight')

    ax1 = fig.add_subplot(111)
    binsretorno = np.linspace(lim_grafico[0]-0.5,lim_grafico[1]+0.5,-lim_grafico[0]+lim_grafico[1]+2)

    #==================================
    y_tot, bin_edges_tot = np.histogram(data0, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker0, facecolor='none', edgecolor=color0, s=15, label=label0)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data1, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker1, facecolor='none', edgecolor=color1, s=15, label=label1)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data2, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker2, facecolor='none', edgecolor=color2, s=15, label=label2)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data3, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker3, facecolor='none', edgecolor=color3, s=15, label=label3)#, color='cyan')
    #==================================

    # Aumentar el tamaño de la fuente en los ejes
    ax1.tick_params(axis='x', labelsize=15, length=4, width=1)
    ax1.tick_params(axis='y', labelsize=15, length=4, width=1)

    # Configurar las marcas menores en el eje y
    ax1.tick_params(axis='y', which='minor', size=3)

    ax1.yaxis.set_ticks_position('both')
    ax1.tick_params(labelleft=True,labelright=False)

    ax1.xaxis.set_ticks_position('both')
    ax1.tick_params(labelbottom=True,labeltop=False)

    ax1.set_yscale("log")
    #ax1.legend(fontsize = 15)
    #ax1.set_title('distribución de retornos (log return)')
    ax1.set_xlim(lim_grafico_ZOOMZOOM[0],lim_grafico_ZOOMZOOM[1])
    #ax1.set_ylim(0.01,2)
    
    if title == True:
        numero = a
        ax1.set_title(f'a = {numero}')

    if save_fig == True:
        fig.savefig(pwdgraf+nombre_archivo+'_ZOOMZOOM'+'.pdf', format='pdf')

    #fig.savefig('/home/mjdomenech/TrabajoFinal/Figuras/OVERLEAF/resultados-febrero/1-retornos_09_norm-val-maxZOOM1PICO.png', dpi=300)
    #fig.show()
        

grafico_retornos_ZOOMZOOM(data0,data1,data2,data3,  lim_grafico_ZOOMZOOM,
                     color0,color1,color2,color3,
                     marker0,marker1,marker2,marker3,
                     label0,label1,label2,label3,
                     pwdgraf, save_fig, nombre_archivo,a) 