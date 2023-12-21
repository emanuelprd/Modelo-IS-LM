#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive_output, Layout, FloatSlider, VBox, HBox
from sympy import symbols, Eq, solve


# In[2]:


# Definindo a função da curva IS
def curva_is(Y, r, a, b, c, d, G, T):
    
    return (a+c+G-b*T-d*r)/(1-b)

# Definindo a função da curva LM
def curva_lm(Y, r, f, M, P, e):
    
    return (M/P+f*r)*(1/e)

# Definindo a função de equilíbrio
def equilibrio(Y, r, a, b, c, d, G, T, f, M, P, e, color):
    
    Y_values, r_values = symbols('Y r')
    equation = Eq(curva_is(Y_values, r_values, a, b, c, d, G, T) - curva_lm(Y_values, r_values, f, M, P, e), 0)
    solution = solve(equation, (Y_values, r_values))
    
    r_equilibrio = np.array(solution[0][1])
    y_equilibrio = np.array((M/P+f*solution[0][1])*(1/e))
    
    if color == 'blue':
        plt.scatter(y_equilibrio, r_equilibrio, color=color, zorder=3, s = 15, 
                label = f"r1 = {r_equilibrio:.2f}\nY1 = {y_equilibrio:.0f}")  
    else:
        plt.scatter(y_equilibrio, r_equilibrio, color=color, zorder=3, s = 15, 
                label = f"r2 = {r_equilibrio:.2f}\nY2 = {y_equilibrio:.0f}")  
    
    plt.vlines(x= y_equilibrio, ymin = 0, ymax=r_equilibrio, linestyle='dashed', color=color, alpha=0.3) 
    plt.hlines(y= r_equilibrio, xmin = 0, xmax=y_equilibrio, linestyle='dashed', color=color, alpha=0.3) 
    plt.legend
    
# Valores limites para o eixo x e o eixo y
Y_values = np.linspace(100, 2500, 100)
r_values = np.linspace(2, 14, 100)

def grafico_interativo(a, b, c, d, G, T, f, M, P, e):
    
    # Valores para as curvas IS e LM
    IS_values = curva_is(Y_values, r_values, a, b, c, d, G, T)
    LM_values = curva_lm(Y_values, r_values, f, M, P, e)
    
    #Ponto Equilíbrio
    color = 'red'
    equilibrio(Y_values, r_values, a, b, c, d, G, T, f, M, P, e, color)
    
    #Gráficos
    plt.plot(IS_values, r_values, color = 'red', alpha=0.9)
    plt.plot(LM_values, r_values, color = 'red', alpha=0.9)
    
    #Configurações gerais do gráfico
    plt.xlabel('Produto (Y)')
    plt.ylabel('Taxa de Juros (r)')
    plt.title('Curvas IS-LM: Interativo', fontsize = 14)
    plt.xlim(0, max(Y_values))
    plt.ylim(0, max(r_values)+2)
    plt.xticks(np.arange(0, max(Y_values), step=250))
    plt.yticks(np.arange(0, max(r_values)+2, step=2))
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    grafico_padrao()
    plt.show()
    
def grafico_padrao():    

    #Parâmetros do gráfico padrâo
    a = 200  # Consumo autônomo
    b = 0.75  # Propensão marginal a consumir
    c = 200 # Investimento autônomo
    d = 25 # Sensibilidade do investimento à taxa de juros
    G = 100  # Gastos do governo
    T = 100  # Tributos
    M = 1000  # Demanda por moeda
    P = 2 # Nível de Preços
    f = 100  # Sensibilidade da demanda por moeda à taxa de juros
    e = 1 # Sensibilidade demanda por moeda à renda
   
    # Valores para as curvas IS e LM
    IS_values = curva_is(Y_values, r_values, a, b, c, d, G, T)
    LM_values = curva_lm(Y_values, r_values, f, M, P, e)
    
    #Ponto equilíbrio
    color = 'blue'
    equilibrio(Y_values, r_values, a, b, c, d, G, T, f, M, P, e, color)
    
    #Gráficos
    plt.plot(IS_values, r_values, color = 'mediumblue')
    plt.plot(LM_values, r_values, color = 'mediumblue')
    plt.legend()

# Layout dos sliders
slider_layout = Layout(width='370px')
    
# Configuração dos sliders
a_slider = FloatSlider(value=200, min=0, max=1000, continuous_update=False, layout=slider_layout)
b_slider = FloatSlider(value=0.75, min=0.1, max=1.0, continuous_update=False, layout=slider_layout)
c_slider = FloatSlider(value=200, min=100, max=1000, continuous_update=False, layout=slider_layout)
d_slider = FloatSlider(value=25, min=0, max=50, continuous_update=False, layout=slider_layout)
G_slider = FloatSlider(value=100, min=0, max=1000, continuous_update=False, layout=slider_layout)
T_slider = FloatSlider(value=100, min=0, max=1000, continuous_update=False, layout=slider_layout)
f_slider = FloatSlider(value=100, min=0, max=200, continuous_update=False, layout=slider_layout)
M_slider = FloatSlider(value=1000, min=0, max=2000, continuous_update=False, layout=slider_layout)
P_slider = FloatSlider(value=2, min=0, max=10, continuous_update=False, layout=slider_layout)
e_slider = FloatSlider(value=1, min=0.1, max=3, continuous_update=False, layout=slider_layout)

# Layout do Vbox
controls_column = VBox([a_slider, b_slider, c_slider, d_slider, G_slider, 
                        T_slider, f_slider, M_slider, P_slider, e_slider],
                       layout=Layout(display='flex', flex_flow='column', width='400px', height ='330px'))
# Layout do Hbox
controls_column = VBox([
    Label(value='Consumo autônomo', layout=Layout(margin='0 0 0 10px')), a_slider,
    Label(value='Propensão marginal a consumir', layout=Layout(margin='0 0 0 10px')), b_slider,
    Label(value='Investimento autônomo', layout=Layout(margin='0 0 0 10px')), c_slider,
    Label(value='Sensibilidade do investimento à taxa de juros', layout=Layout(margin='0 0 0 10px')), d_slider,
    Label(value='Gastos do governo', layout=Layout(margin='0 0 0 10px')), G_slider,
    Label(value='Tributos pagos ao governo', layout=Layout(margin='0 0 0 10px')), T_slider,
    Label(value='Sensibilidade da demanda por moeda à taxa de juros', layout=Layout(margin='0 0 0 10px')), f_slider,
    Label(value='Demanda por moeda', layout=Layout(margin='0 0 0 10px')), M_slider,
    Label(value='Nível de Preços', layout=Layout(margin='0 0 0 10px')), P_slider,
    Label(value='Sensibilidade demanda por moeda à renda', layout=Layout(margin='0 0 0 10px')), e_slider,
], layout=Layout(display='flex', flex_flow='column', width='400px', height='550px', border='solid'))

# Saída Interativa
output = interactive_output(grafico_interativo,
                             {'a': a_slider, 'b': b_slider, 'c': c_slider, 'd': d_slider, 'G': G_slider, 
                              'T': T_slider, 'f': f_slider, 'M': M_slider, 'P': P_slider, 'e': e_slider})

#Rodando o display
display(HBox([output, controls_column]))





