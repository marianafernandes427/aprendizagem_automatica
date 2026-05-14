import csv

input_file = 'C:/bd2/cassandra_data/querie2.csv'
output_file = 'C:/bd2/cassandra_data/querie2_limpo.csv'

with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    
    for line in infile:
        # Remover aspas do início da linha
        line = line.lstrip('"')
        
        # Se a linha termina com aspa, remover
        line = line.rstrip('"\n') + '\n'
        
        outfile.write(line)

print("Arquivo limpo!")

