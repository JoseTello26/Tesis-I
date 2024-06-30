import json
import numpy as np
import matplotlib.pyplot as plt

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON.")
x=[]
y=[]
n=["dog", "beauty", "news", "four_people", "hallroom", "ice_skating", "foreman"]
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'black']

for i in range(1,8):
    # Ruta del archivo input.json
    file_path = f'test{i}/input.json'

    # Leer el archivo y guardarlo en un diccionario
    data_dict = read_json_file(file_path)
    si = np.mean(data_dict["si"])
    ti = np.mean(data_dict["ti"])

#    if data_dict is not None:
#        print(f"SITI {i}")
#        print(si,", ", ti)

    x.append(si)
    y.append(ti)
    

plt.scatter(x, y, c=colors)
for i, txt in enumerate(n):
    plt.annotate(f" {i+1}_{txt}",(x[i], y[i]))
plt.title("Spatial-Temporal Information")
plt.xlabel("Spatial Information")
plt.ylabel("Temporal Information")
plt.grid()
plt.savefig("siti_plot.png")
