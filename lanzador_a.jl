# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:29:06 2024

@author: mariajose
"""

#using Threads
using Random
using DelimitedFiles
using Dates
include("funciones.jl")  # archivo funciones.jl que contiene las funciones


# Poner ruta donde se guardarán los archivos
#pwd = "/home/mjdomenech/TrabajoFinal/ArchivosCCAD/JuliaThreads/marzo1/"
pwd = "/home/mjdomenech/Paper/Simulaciones-a-fijo/"

(a, N, l, cantidad_simulaciones) = ARGS   #ojo que los ARGS los toma como strings (aunque ingrese por ej: 0.01 100 10E4 5)

a_number = parse(Float64, a)
l_number = parse(Float64, l)
N_number = parse(Int, N)
cantidad_simulaciones_number = parse(Int, cantidad_simulaciones)



# CHEQUEO TIPOS
tipo1 = typeof(a_number)
tipo2 = typeof(a)
println("a_number es $a_number y de tipo $tipo1, mientras que a es $a y de tipo $tipo2")

tipo1 = typeof(N_number)
tipo2 = typeof(N)
println("N_number es $N_number y de tipo $tipo1, mientras que N es $l y de tipo $tipo2")

tipo1 = typeof(l_number)
tipo2 = typeof(l)
println("l_number es $l_number y de tipo $tipo1, mientras que l es $l y de tipo $tipo2")

tipo1 = typeof(cantidad_simulaciones_number)
tipo2 = typeof(cantidad_simulaciones)
println("cantidad_simulaciones_number es $cantidad_simulaciones_number y de tipo $tipo1, mientras que cantidad_simulaciones es $cantidad_simulaciones y de tipo $tipo2")
###



T = 300000   # INDICE T

astring = replace(string(a), "." => "")




Threads.@threads for i = 1:cantidad_simulaciones_number
        
    println("i = $i on thread $(Threads.threadid())")
    #comando = crear_comando(alfa,N,l,i)
    #print(string(comando))
    
    v = sistema(N_number, N_number/2, 0, 1)
    
    (delta, retorno, tejec, Ttotal) = evolucion_temporal_sin_s_a!(a_number,v,T,cant_puntos=l_number)
    
   
    fecha = Dates.format(Dates.now(), "yyyy-mm-dd-HH-MM-SS")
    -
    archivo_output = pwd*"output_"*astring*"_"*N*"_"*l*"_"*string(i)*"_"*fecha*".txt"
    
    open(archivo_output, "w") do file
    
        #redirect_stdout(file) # Redirigir la salida estándar al archivo
        
        
        println(file, "a_number:      ", a_number)
        println(file, "cantidad de puntos en distrib de retorno:      ", size(retorno, 1))
        println(file, "                                 delta: ", size(delta, 1))
        println(file, "pasos temporales por ciclo, T=", T)
        println(file, "tiempo de ejecución: ", tejec, " minutos")
        println(file, "pasos temp totales: ", Ttotal)
    
    end
    
    # Guardar arreglos en archivos
    archivo_retorno = pwd*"retorno_"*astring*"_"*N*"_"*l*"_"*string(i)*"_"*fecha*".txt"

    open(archivo_retorno, "w") do io
        writedlm(io, retorno)
    end

    archivo_delta = pwd*"delta_"*astring*"_"*N*"_"*l*"_"*string(i)*"_"*fecha*".txt"
    open(archivo_delta, "w") do io
        writedlm(io, delta)
    end

    archivo_tiempo = pwd*"tejec_"*astring*"_"*N*"_"*l*"_"*string(i)*"_"*fecha*".txt"
    open(archivo_tiempo, "w") do io
        writedlm(io, tejec)
    end
     
end