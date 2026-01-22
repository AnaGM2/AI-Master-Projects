#!/bin/bash
#SBATCH -p cola02
#SBATCH --gres=gpu:1
#SBATCH -c 1
#SBATCH --mem=4G
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=06:30:00
#SBATCH --job-name=Ej3_Javi
#SBATCH --output=./logs/job%j.out  # Archivo para la salida estándar
#SBATCH --error=./logs/job%j.err   # Archivo para la salida de error

apptainer exec --writable-tmpfs --nv /software/singularity/Informatica/mia-dlpln-apptainer/mia_dlpln_parte1_1.0.sif /opt/conda/bin/jupyter nbconvert --to notebook --execute /home/jgarciaserrano1/Cluster/Practica1_DLPLN_Ejer3.ipynb >--output /home/jgarciaserrano1/Cluster/Practica1_DLPLN_Ejer3_done.ipynb