import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

normaError = []
ePesos = []

def entrenamiento(archivo,epocas, eta):
    global neEpocas, ePesos, normaError
    
    normaError = []  
    ePesos = [] 
    
    data = pd.read_csv(archivo, delimiter= ';',  header=None)
    columnas = [f'x{i}' for i in range(1, len(data.columns))] + ['y']
    xs = len(columnas)-1
    yd = np.array(data.iloc[:, -1])
 
    ws = np.random.uniform(low=0, high=1, size=(xs + 1, 1)).round(2)
    matrizX = np.hstack([data.iloc[:, :-1].values, np.ones((data.shape[0], 1))])
    wIniciales = ws.copy()
    
    for _ in range(epocas):
        u = np.dot(matrizX, ws)
        yc = (u >= 0).astype(int)
        
        e = yd.reshape(-1, 1) - yc
        norma_error = np.linalg.norm(e)
        normaError.append(norma_error)
        
        ePesos.append(np.copy(ws.flatten()))
        
        deltaW = eta * np.dot( matrizX.T, e)
        ws += deltaW
    wFinales = ws
    return wIniciales, wFinales

def graficarNormaError(epocas):
    global normaError
    sns.set(style="whitegrid")

    plt.figure(figsize=(9, 6))
    x_range = range(1, len(normaError) + 1)
    sns.lineplot(x=x_range, y=normaError, marker='o')
    plt.title('Evolución de la norma del error |e| por época')
    plt.xlabel('Época')
    plt.ylabel('Norma del error |e|')

    plt.show()
    
def graficarEvolucionPesos(epocas):
    global ePesos
    sns.set(style="whitegrid")

    plt.figure(figsize=(9, 6))
    for i in range(len(ePesos[0])):
        sns.lineplot(x=range(1, epocas + 1), y=[peso[i] for peso in ePesos], label=f'Peso {i+1}')

    plt.title('Evolución de los pesos por época')
    plt.xlabel('Época')
    plt.ylabel('Valor del peso')
    plt.legend()

    plt.show()
def procesar_archivo(archivo, eta, epoca):
    resultado = f"eta={eta} \nepoca={epoca}\n"
    
    df = pd.read_csv(archivo)
    print("Iniciando procesamiento del archivo CSV...")
    print(df)

    return resultado
