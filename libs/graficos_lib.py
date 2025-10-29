#libs/graficos_lib.py

# Biblioteca para criação de gráficos
import matplotlib.pyplot as plt

# Função para plotar gráfico de linhas
def plotar_grafico_linhas(ds, x, y, group, titulo, xlabel, ylabel):
    plt.figure(figsize=(16, 8))
    if group is None:
        plt.plot(ds[x], ds[y], marker='o', color='steelblue')
    else:
        for key, grp in ds.groupby(group):
            plt.plot(grp[x], grp[y], marker='o', linestyle='-', label=key)
        plt.legend()
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()  
    plt.show()

# Função para plotar gráfico de dispersão com bolhas
def plotar_dispersao_bolhas(df, x, y, size, hue=None, title='', xlabel='', ylabel='', figsize=(16,8), logx=False, logy=False):
    plt.figure(figsize=figsize)
    s = (df[size] / df[size].max()) * 2000  # escala para bolhas
    if hue is None:
        plt.scatter(df[x], df[y], s=s, alpha=0.6)
    else:
        cats = sorted(df[hue].unique())
        for c in cats:
            sub = df[df[hue]==c]
            ss = (sub[size] / df[size].max()) * 2000
            plt.scatter(sub[x], sub[y], s=ss, alpha=0.6, label=c)
        plt.legend()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if logx:
        plt.xscale('log')
    if logy:
        plt.yscale('log')
    plt.grid(alpha=0.3)
    plt.show()

# Função para plotar gráfico de barras horizontais
def plotar_barras_horizontais(df, x_col, y_col, title='', xlabel='', ylabel='', figsize=(16, 8)):
    plt.figure(figsize=figsize)
    plt.barh(range(len(df)), df[x_col])
    plt.yticks(range(len(df)), df[y_col])
    plt.xlabel(xlabel)
    plt.title(title)
    plt.gca().invert_yaxis()
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.show()