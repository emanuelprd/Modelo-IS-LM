#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive_output, Layout, FloatSlider, VBox, HBox
from sympy import symbols, Eq, solve


# In[2]:


# Função da curva IS
def curva_is(Y, r, a, b, c, d, G, T):
    return ( a + c + G - b*T - d*r) * (1/(1-b))

# Função da curva LM
def curva_lm(Y, r, k, M, P, e):
    return (M/P + k*r)*(1/e)

# Função de Equilíbrio IS-LM
def equilibrio(Y, r, a, b, c, d, G, T, k, M, P, e, color):
    Y_values_, r_values_ = symbols('Y r')
    #Definindo a equação onde: curva_is - curva_lm = 0
    equation = Eq(curva_is(Y_values_, r_values_, a, b, c, d, G, T) - curva_lm(Y_values_, r_values_, k, M, P, e), 0)
    solution = solve(equation, (Y_values_, r_values_))
    r_equilibrio = np.array(solution[0][1])
    y_equilibrio = np.array((M/P + k*solution[0][1])*(1/e))
    plt.scatter(y_equilibrio, r_equilibrio, color=color, zorder=3, s = 15, 
                label = f"r = {r_equilibrio:.2f}\ny = {y_equilibrio:.2f}")  
    plt.vlines(x= y_equilibrio, ymin = 0, ymax=r_equilibrio, linestyle='dashed', color=color, alpha=0.3) 
    plt.hlines(y= r_equilibrio, xmin = 0, xmax=y_equilibrio, linestyle='dashed', color=color, alpha=0.3) 
    plt.legend
    
# Valores limites para o eixo x (Y_values) e o eixo y (r_values)
Y_values = np.linspace(100, 2500, 100)
r_values = np.linspace(2, 14, 100)

Y_values_ = Y_values
r_values_ = r_values

def grafico_interativo(a=200, b=0.75, c=200, d=25, G=100, T=100, k=100, M=1000, P=2, e=1):
    
    IS_values = curva_is(Y_values, r_values, a, b, c, d, G, T)
    LM_values = curva_lm(Y_values, r_values, k, M, P, e)
    
    #Equilíbrio
    color = 'darkgreen'
    equilibrio(Y_values_, r_values_, a, b, c, d, G, T, k, M, P, e, color)
    
    #Gráficos
    plt.plot(IS_values, r_values, color = 'black', linestyle = '--', alpha=0.9)
    plt.plot(LM_values, r_values, color = 'mediumblue', linestyle = '--', alpha=0.9)
    
    #Parâmetros gerais do Gráfico
    plt.xlabel('Produto (Y)')
    plt.ylabel('Taxa de Juros (r)')
    plt.title('Curvas IS-LM: Interativo', fontsize = 14)
    plt.xlim(0, max(Y_values))
    plt.ylim(0, max(r_values)+2)
    plt.xticks(np.arange(0, max(Y_values), step=500))
    plt.yticks(np.arange(0, max(r_values)+2, step=2))
    plt.grid(True)
    grafico_padrao()
    plt.show()
    
def grafico_padrao():    

    #Parâmetros das funções
    a = 200  # Consumo autônomo
    b = 0.75  # Propensão marginal a consumir
    c = 200 # Investimento autônomo
    d = 25 # Sensibilidade do investimento à taxa de juros
    G = 100  # Gastos do governo
    T = 100  # Tributos
    M = 1000  # Demanda por moeda
    P = 2 # Nível de Preços
    k = 100  # Sensibilidade da demanda por moeda à taxa de juros
    e = 1 # Sensibilidade demanda por moeda à renda
   
    # Calculo das curvas IS e LM
    IS_values = curva_is(Y_values, r_values, a, b, c, d, G, T)
    LM_values = curva_lm(Y_values, r_values, k, M, P, e)
    
    #Equilíbrio
    color = 'red'
    equilibrio(Y_values_, r_values_, a, b, c, d, G, T, k, M, P, e, color)
    
    #Gráficos
    plt.plot(IS_values, r_values, color = 'black')
    plt.plot(LM_values, r_values, color = 'mediumblue')
    plt.legend()

# Parâmetros do Slider
a_slider = FloatSlider(value=200, min=0, max=500, description='a', continuous_update=False)
b_slider = FloatSlider(value=0.75, min=0.1, max=1.0, description='b', continuous_update=False)
c_slider = FloatSlider(value=200, min=100, max=500, description='c', continuous_update=False)
d_slider = FloatSlider(value=25, min=10, max=50, description='d', continuous_update=False)
G_slider = FloatSlider(value=100, min=0, max=1000, description='G', continuous_update=False)
T_slider = FloatSlider(value=100, min=0, max=200, description='T', continuous_update=False)
k_slider = FloatSlider(value=100, min=0, max=300, description='k', continuous_update=False)
M_slider = FloatSlider(value=1000, min=500, max=4000, description='M', continuous_update=False)
P_slider = FloatSlider(value=2, min=1, max=5, description='P', continuous_update=False)
e_slider = FloatSlider(value=1, min=0.1, max=2, description='e', continuous_update=False)

# Layout dos sliders
slider_layout = Layout(width='200px')

# Criar layout de coluna única
controls_column = VBox([a_slider, b_slider, c_slider, d_slider, G_slider, T_slider, k_slider, M_slider, P_slider, e_slider],
                       layout=Layout(display='flex', flex_flow='column'))

# Criar saída interativa
output = interactive_output(grafico_interativo,
                             {'a': a_slider, 'b': b_slider, 'c': c_slider,
                              'd': d_slider, 'G': G_slider, 'T': T_slider,
                              'k': k_slider, 'M': M_slider, 'P': P_slider,
                              'e': e_slider})

# Exibir gráfico e sliders
display(HBox([output, controls_column]))


# In[ ]:




