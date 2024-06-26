#!/bin/bash

#SBATCH --job-name=job20-jose

#SBATCH --output=job20-jose.log

#SBATCH --partition=multi

#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=1 
#SBATCH --cpus-per-task=64 ## Esto nos deja modificar el número de hilos que podemos usar. Serafin 1-64

#SBATCH --exclusive 

#SBATCH --mail-type=ALL    
#SBATCH --mail-user=m.jose.domenech@mi.unc.edu.ar

. /etc/profile

#srun /home/mjdomenech/julia-1.9.1/bin/julia -t 64 lanzador.jl 0.0001 10000 10E3 64

srun /home/mjdomenech/julia-1.9.1/bin/julia -t 64 lanzador_a.jl 44990 10000 50E3 64