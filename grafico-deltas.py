# Importar librerías
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

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
nombre_archivo = 'deltas_a_fijo_'+str(a)

# Importar datos
#data3 = np.load(pwd+'simulaciones-trabajofinal/SimulacionesOtrosAlpha/delta_09995_100_10E5.npy')
#data3 = np.loadtxt(pwd+'simulaciones-a-fijo/delta_197900_100_10E6_1_2024-05-09-17-33-45.txt') 
#data2 = np.loadtxt(pwd+'simulaciones-a-fijo/delta_197900_1000_10E6_1_2024-05-07-15-31-03.txt')
#data1 = np.loadtxt(pwd+'simulaciones-a-fijo/delta_197900_5000_10E6_1_2024-05-08-07-02-28.txt')
#data0 = np.loadtxt(pwd+'simulaciones-a-fijo/delta_197900_10000_10E6_1_2024-05-09-16-30-42.txt')

#data3 = np.loadtxt(pwd+'simulaciones-a-fijo/delta_44990_100_10E6_1_2024-05-07-01-33-47.txt') 
#data2 = np.loadtxt(pwd+'simulaciones-a-fijo/delta_44990_1000_10E6_1_2024-05-07-03-07-08.txt')
#data1 = np.loadtxt(pwd+'simulaciones-trabajofinal/09/delta_09_5000_10E6.txt')
#data0 = np.loadtxt(pwd+'simulaciones-a-fijo/delta_44990_10000_10E6_concatenado1.txt')


#data3 = np.loadtxt(pwd+'simulaciones-a-fijo/delta_8990_100_10E6_1_2024-05-06-16-59-52.txt') 
#data2 = np.loadtxt(pwd+'simulaciones-trabajofinal/09/delta_09_1000_10E6.txt')
#data1 = np.loadtxt(pwd+'simulaciones-a-fijo/delta_8990_5000_10E6_1_2024-05-07-14-50-40.txt')
#data0 = np.loadtxt(pwd+'simulaciones-a-fijo/delta_8990_10000_10E6_concatenado1.txt') 

data3 = np.loadtxt(pwd+'simulaciones-trabajofinal/1N/delta_001_100_10E6.txt') 
data2 = np.loadtxt(pwd+'simulaciones-a-fijo/delta_10_1000_10E6_1_2024-05-07-14-06-41.txt')
data1 = np.loadtxt(pwd+'simulaciones-a-fijo/delta_10_5000_10E6_concatenado1.txt')
#data0 = np.loadtxt(pwd+'simulaciones-a-fijo/delta_8990_10000_10E6_concatenado1.txt') 
data0 = 2

muest_aleat = False

#-------------------------------------------------

###############################################################################
########################### GRAFICO PARA DELTAS
###############################################################################

#NORMALIZADA AL VAL MAX

#-----------Parámetros para cada N-----------

lim_escala= 20000000

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

#-----------Parámetros para cada N-----------

# Filtrar los valores mayores a lim_escala
#data0 = data0[data0 <= lim_escala]
data1 = data1[data1 <= lim_escala]
data2 = data2[data2 <= lim_escala]
data3 = data3[data3 <= lim_escala] 

#es para que no se haga tan pesado calcular todos los bins del 0 a un valor aislado 35213123513

#print(data0.shape)
#print(data1.shape)
#print(data2.shape)
#print(data3.shape)

#---------------------------------

def muestreo_aleatorio(data,num_puntos_submuestra):
    
    #Realiza el muestreo aleatorio
    indices_submuestra = np.random.choice(len(data), size=num_puntos_submuestra, replace=False)
    #Selecciona los puntos de la submuestra
    data = data[indices_submuestra]
    return data


if muest_aleat == True:
    data0 = muestreo_aleatorio(data0,1000000)
    data1 = muestreo_aleatorio(data1,1000000)
    data2 = muestreo_aleatorio(data2,1000000)
    #data3 = muestreo_aleatorio(data3,1000000)

    print('luego del muestreo aleatorio')
    print(data0.shape)
    print(data1.shape)
    print(data2.shape)
    #print(data3.shape)

#NORMALIZADA AL VAL MAX
fig = plt.figure(figsize = [7.4, 5.8],layout='tight' )
ax1 = fig.add_subplot(111)



#================================================================================================
binsdelta0 = np.linspace(1.5, np.amax(data0)+0.5, int(np.amax(data0))) 

y0, bin_edges = np.histogram(data0, bins=binsdelta0)
x0 = bin_edges[1:]
x0 = x0.astype(int)

#plt.axvline(x1[-1],linestyle='-',linewidth=0.5)

p00 = np.amax(y0)
y0=y0/p00          #normalizo para que P(delta_max) = 1 (misma normaliz que Bakar)

mask = y0 != 0   # mascara booleana que quita los puntos del histograma que valdrían cero 
x0 = x0[mask]     # (joden al calcularles el log pq log(0) es menos inf)
y0 = y0[mask]

ax1.scatter(x0, y0, marker=marker0, facecolor='none', edgecolor=color0, s=10, label=label0)
#================================================================================================
#================================================================================================
binsdelta1 = np.linspace(1.5, np.amax(data1)+0.5, int(np.amax(data1))) 

y1, bin_edges = np.histogram(data1, bins=binsdelta1)
x1 = bin_edges[1:]
x1 = x1.astype(int)

#plt.axvline(x3[-1],linestyle='-',linewidth=0.5)

p01 = np.amax(y1)
y1=y1/p01          #normalizo para que P(delta_max) = 1 (misma normaliz que Bakar)

mask = y1 != 0   # mascara booleana que quita los puntos del histograma que valdrían cero 
x1 = x1[mask]     # (joden al calcularles el log pq log(0) es menos inf)
y1 = y1[mask]

ax1.scatter(x1, y1, marker=marker1, facecolor='none', edgecolor=color1, s=10, label=label1)

#================================================================================================
#================================================================================================
binsdelta2 = np.linspace(1.5, np.amax(data2)+0.5, int(np.amax(data2))) 

y2, bin_edges = np.histogram(data2, bins=binsdelta2)
x2 = bin_edges[1:]    #de esta forma se ignora el ultimo valor, pero no me importa pq seguro es 0
x2 = x2.astype(int)

#plt.axvline(x2[-1],linestyle='-',linewidth=0.5)

p02 = np.amax(y2)
y2=y2/p02          #normalizo para que P(delta_max) = 1 (misma normaliz que Bakar)

mask = y2 != 0   # mascara booleana que quita los puntos del histograma que valdrían cero 
x2 = x2[mask]     # (joden al calcularles el log pq log(0) es menos inf)
y2 = y2[mask]

ax1.scatter(x2, y2, marker=marker2, facecolor='none', edgecolor=color2, s=10, label=label2)
#================================================================================================

#================================================================================================
binsdelta3 = np.linspace(1.5, np.amax(data3)+0.5, int(np.amax(data3))) 

y3, bin_edges = np.histogram(data3, bins=binsdelta3)
x3 = bin_edges[1:]    #de esta forma se ignora el ultimo valor, pero no me importa pq seguro es 0
x3 = x3.astype(int)

#plt.axvline(x3[-1],linestyle='-',linewidth=0.5)

p03 = np.amax(y3)
y3=y3/p03          #normalizo para que P(delta_max) = 1 (misma normaliz que Bakar)

mask = y3 != 0   # mascara booleana que quita los puntos del histograma que valdrían cero 

x3 = x3[mask]     # (joden al calcularles el log pq log(0) es menos inf)
y3 = y3[mask]

ax1.scatter(x3, y3, marker=marker3, facecolor='none', edgecolor=color3, s=10, label=label3)
#================================================================================================


#================================================================================================
# AJUSTE

intervalo=[60,4000] # Elijo un intervalo diferente para hacer el ajuste
x=np.log(x1)
y=np.log(y1)
xcasi = x[x >= np.log(intervalo[0])]         #cota inferior
ycasi = y[x >= np.log(intervalo[0])]
xfinal = xcasi[xcasi <= np.log(intervalo[1])]         #cota superior
yfinal = ycasi[xcasi <= np.log(intervalo[1])]
#plt.axvline(intervalo[0],linestyle='-',linewidth=0.5)
#plt.axvline(intervalo[1],linestyle='-',linewidth=0.5)
#plt.scatter(np.exp(xfinal), np.exp(yfinal), color='orange')

# Hacer ajuste
slope, intercept, r_value, p_value, std_err = stats.linregress(xfinal, yfinal)

print("Pendiente:", slope)
print("Intercept:", intercept)

plt.plot(np.exp(xfinal), np.exp(slope*xfinal + intercept), color="black",linewidth=0.8)#label='Ajuste'
#plt.plot(np.exp(xfinal), np.exp(-1.409*xfinal + intercept), color="black",linewidth=0.8)#label='Ajuste'
#plt.plot(np.exp(xfinal), np.exp(-1.409*xfinal + intercept+1.5), color="black",linewidth=0.8)#label='Ajuste'
#plt.plot(np.exp(xfinal), np.exp(-1.517*xfinal + intercept+1.5), color="red",linewidth=0.5)

#================================================================================================

#-------------------------configuración estilo-------------------------
ax1.yaxis.set_ticks_position('both')
ax1.tick_params(labelleft=True,labelright=False)

ax1.xaxis.set_ticks_position('both')
ax1.tick_params(labelbottom=True,labeltop=False)

# Aumentar el tamaño de la fuente en los ejes
ax1.tick_params(axis='x', labelsize=18, length=6, width=1)
ax1.tick_params(axis='y', labelsize=18, length=6, width=1)

# Configurar las marcas menores en el eje y
ax1.tick_params(axis='y', which='minor', size=3)

ax1.yaxis.set_ticks_position('both')
ax1.tick_params(labelleft=True,labelright=False)

ax1.xaxis.set_ticks_position('both')
ax1.tick_params(labelbottom=True,labeltop=False)

#ax1.set_title("distribución deltas (fluctuation lenght)")
ax1.set_yscale('log')
ax1.set_xscale('log')

ax1.set_xlabel('$\lambda$',fontsize = 18)
ax1.set_ylabel('$P(\lambda)/P(\lambda_{máx})$', fontsize = 18)

#plt.xticks(fontsize = 15)

ax1.legend(fontsize = 16)
#ax1.set_xlim(0.5, lim_escala)

if title == True:
    numero = a
    ax1.set_title(f'a = {numero}, slope={round(slope,4)}')

if save_fig == True:
    fig.savefig(pwdgraf+nombre_archivo+'.pdf', format='pdf')



#fig.show()
