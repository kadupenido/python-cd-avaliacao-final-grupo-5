#libs/graficos_lib.py

# Biblioteca para criação de gráficos
import matplotlib.pyplot as plt

# Função para plotar gráfico de linhas
def plotar_grafico_linhas(ds, x, y, titulo, xlabel, ylabel):
    plt.figure(figsize=(16, 8))
    plt.plot(ds[x], ds[y], marker='o', color='steelblue')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()  
    plt.show()