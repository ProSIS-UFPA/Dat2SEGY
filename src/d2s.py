#usr/bin/python3
#%%%%%%%%%%%%%%%%%%%#

"""
Autor: Wilson Oliveira (github.com/wnods)
Objetivo: Uma conversão mais automatizada de dados ".dat" para ".SGY" com o objetivo de maior compatibilidade com o programa GnSeis criado por mim. 

"""
import os
from obspy import read

# Files in .dat diretory
input_directory = "diretory/.dat" # Change to path diretory input
output_directory = "diretory/.SGY"  # change to path diretory output for save in .SGY

os.makedirs(output_directory, exist_ok=True)

# Loop for all .dat files
for filename in os.listdir(input_directory):
    if filename.endswith(".dat"):
    
        # Path diretory for 
        input_file = os.path.join(input_directory, filename)
        
        # Read .dat files
        st = read(input_file)
        
        output_file = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.SGY")
        
        # Save in SEG-Y format
        st.write(output_file, format="SEGY")
        print(f"Convertido: {filename} para {output_file}")
        print(f"Todos os Diretos Reservados ao Laboratório de Processamento Sísmico da UFPA e ao Autor Wilson Weliton Oliveira de Souza")

