
import numpy as np

#------------------ configuración ----------------

# aca poner la ruta donde estan los archivo_names, destildar la correcta

pwd = 'C:\\Users\\mariajose\\Documents\\GitHub\\simulaciones\\simulaciones-a-fijo\\'

#archivo = 'deltas_8990_10000_50E3.txt'
#archivo = 'retornos_8990_10000_50E3.txt'
#archivo = 'deltas_44990_10000_50E3.txt'
#archivo = 'retornos_44990_10000_50E3.txt'
#archivo = 'deltas_10_5000_50E3.txt'
#archivo = 'retornos_10_5000_50E3.txt'
#archivo = 'deltas_10_10000_50E3.txt'
archivo = 'retornos_10_10000_50E3.txt'

#archivo_resultante = 'delta_8990_10000_10E6_concatenado1.txt'
#archivo_resultante = 'retorno_8990_10000_10E6_concatenado1.txt'
#archivo_resultante = 'delta_44990_10000_10E6_concatenado1.txt'
#archivo_resultante = 'retorno_44990_10000_10E6_concatenado1.txt'
#archivo_resultante = 'delta_10_5000_10E6_concatenado1.txt'
#archivo_resultante = 'retorno_10_5000_10E6_concatenado1.txt'
#archivo_resultante = 'delta_10_10000_10E6_concatenado1.txt'
archivo_resultante = 'retorno_10_10000_10E6_concatenado1.txt'

#------------------------------------------------

archivo_names = np.loadtxt(pwd+'para-concatenar3\\'+archivo, dtype='str')

print('ejemplo: ', archivo_names[99]) 

arrays = []

# Ruta base de los archivos
base_path = pwd+'para-concatenar3\\'

i=1

# Iterar sobre los nombres de archivos en deltas_00001_10E4
for filename in archivo_names:
    # Construir la ruta completa del archivo
    full_path = base_path + filename
    
    if i % 10 == 0:
        print(i,full_path)
        
    i+=1
    
    # Cargar el archivo y agregarlo a la lista de arrays
    array = np.loadtxt(full_path)
    arrays.append(array)

# Concatenar los arrays en uno solo
result_array = np.concatenate(arrays)

print('shape del array resultante:', np.shape(result_array))

np.savetxt(pwd+archivo_resultante, result_array)