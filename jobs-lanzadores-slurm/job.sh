#!/bin/bash

#SBATCH --job-name=10E3jose
#SBATCH --output=10E3jose.log
#SBATCH --partition=multi
#SBATCH --nodes=3  # Ejemplo: ejecutar en 3 nodos
#SBATCH --ntasks-per-node=1 
#SBATCH --cpus-per-task=64
#SBATCH --exclusive 
#SBATCH --mail-type=ALL    
#SBATCH --mail-user=m.jose.domenech@mi.unc.edu.ar

# Define los argumentos para el lanzador.jl en un array
args=(
    "0.0001 10000 10E3 64"
    "0.001 5000 5E3 32"
    "0.0005 8000 8E3 16"
    # Agrega más argumentos según sea necesario
)

# Número total de tareas
total_tasks=${#args[@]}

# Bucle sobre el array de argumentos
for ((i=0; i<$total_tasks; i++)); do
    srun -n 1 /home/mjdomenech/julia-1.9.1/bin/julia -t 64 lanzador.jl ${args[$i]} &
done

# Espera a que todos los trabajos lanzados con srun terminen
wait
