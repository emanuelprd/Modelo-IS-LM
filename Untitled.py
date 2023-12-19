#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# Função da curva IS
def curva_is(Y, r, a, b, c, d, G, T):
    
    """
    Y = C + I + G
    C = a + b * (Y - T)
    I = c - d*r
    G = G
    T = T
    Y = a + b * (Y - T) + c - d*r + G
    Y - b * Y = (a + c) (G - b * T) - d*r
    Y * (1 - b) = (a + c) + (G - b * T) - d*r 
    """
    
    return (a + c + G - b * T -d * r) * ( 1 / ( 1 - b ) )

# Função da curva LM
def curva_lm(Y, r, k, M, P):
    
    return M/P + k*r

# Parâmetros do Consumo
a = 200  # Consumo autônomo
b = 0.75  # Propensão marginal a consumir

# Parâmetros de Investimentos
c = 200 # Investimento autônomo
d = 25 # Sensibilidade do investimento à taxa de juros

# Parâmetros do governo
G = 100  # Gastos do governo
T = 100  # Tributos

# Parâmetros da moeda
M = 1000  # Demanda por moeda
P = 2 # Nível de Preços
k = 100  # Sensibilidade da demanda por moeda à taxa de juros

# Faixa de valores para Y (produção) e r (taxa de juros)
Y_values = np.linspace(0, 2000, 100)
r_values = np.linspace(0, 12, 100)

# Calcula as curvas IS e LM
IS_values = curva_is(Y_values, r_values, a, b, c, d, G, T)
LM_values = curva_lm(Y_values, r_values, k, M, P)

from sympy import symbols, Eq, solve

# Variáveis
Y_values1 = Y_values
r_values1 = r_values

Y_values1, r_values1 = symbols('Y r')

# Defina a equação curva_is(Y, r) = curva_lm(Y, r)
equation = Eq(curva_is(Y_values1, r_values1, a, b, c, d, G, T) - curva_lm(Y_values1, r_values1, k, M, P), 0)

# Resolva o sistema de equações para encontrar Y e r
solution = solve(equation, (Y_values1, r_values1))

r_equilibrio = np.array(solution[0][1])
y_equilibrio = np.array(M/P + 100*solution[0][1])

# Plota as curvas
plt.figure(figsize=(8, 6))
plt.plot(IS_values, r_values, label='Curva IS')
plt.plot(LM_values, r_values, label='Curva LM')
plt.scatter(y_equilibrio, r_equilibrio, color='red', zorder=3, label = f"r' = {r_equilibrio:.2f} e y' {y_equilibrio:.2f}")   
plt.xlabel('Nível de Produção (Y)')
plt.ylabel('Taxa de Juros (r)')
plt.title('Curvas IS-LM')
plt.xlim(0, max(Y_values))
plt.ylim(0, max(r_values))
plt.xticks(np.arange(0, max(Y_values), step=200))
plt.yticks(np.arange(0, max(r_values), step=2))
plt.legend()
plt.grid(True)
plt.show()


# In[12]:


from ipywidgets import interact
from sympy import symbols, Eq, solve

def update_grafico(a=200, b=0.75, c=200, d=25, G=100, T=100, k=100, M=1000, P=2):
    Y_values = np.linspace(0, 2000, 100)
    r_values = np.linspace(0, 12, 100)
    
    IS_values = curva_is(Y_values, r_values, a, b, c, d, G, T)
    LM_values = curva_lm(Y_values, r_values, k, M, P)
    
    Y_values1 = Y_values
    r_values1 = r_values
    Y_values1, r_values1 = symbols('Y r')
    equation = Eq(curva_is(Y_values1, r_values1, a, b, c, d, G, T) - curva_lm(Y_values1, r_values1, k, M, P), 0)
    solution = solve(equation, (Y_values1, r_values1))
    r_equilibrio = np.array(solution[0][1])
    y_equilibrio = np.array(M/P + k*solution[0][1])
    
    plt.plot(IS_values, r_values, label="IS 2", color = 'black', linestyle = '--', alpha = 0.5)
    plt.plot(LM_values, r_values, label="LM 2", color = 'mediumblue', linestyle = '--', alpha = 0.5)
    plt.scatter(y_equilibrio, r_equilibrio, color='red', zorder=2, label = f"r 2 = {r_equilibrio:.2f}\ny 2 = {y_equilibrio:.2f}", alpha = 0.5)  
    plt.xlabel('Nível de Produção (Y)')
    plt.ylabel('Taxa de Juros (r)')
    plt.title('Curvas IS-LM')
    plt.xlim(0, max(Y_values))
    plt.ylim(0, max(r_values))
    plt.xticks(np.arange(0, max(Y_values), step=200))
    plt.yticks(np.arange(0, max(r_values), step=2))
    plt.legend()
    plt.grid(True)
    setup_grafico()
    
def setup_grafico():    
    
    a = 200  # Consumo autônomo
    b = 0.75  # Propensão marginal a consumir
    c = 200 # Investimento autônomo
    d = 25 # Sensibilidade do investimento à taxa de juros
    G = 100  # Gastos do governo
    T = 100  # Tributos
    M = 1000  # Demanda por moeda
    P = 2 # Nível de Preços
    k = 100  # Sensibilidade da demanda por moeda à taxa de juros

    Y_values = np.linspace(0, 2000, 100)
    r_values = np.linspace(0, 12, 100)
    
    IS_values = curva_is(Y_values, r_values, a, b, c, d, G, T)
    LM_values = curva_lm(Y_values, r_values, k, M, P)

    Y_values1 = Y_values
    r_values1 = r_values

    Y_values1, r_values1 = symbols('Y r')

    equation = Eq(curva_is(Y_values1, r_values1, a, b, c, d, G, T) - curva_lm(Y_values1, r_values1, k, M, P), 0)

    solution = solve(equation, (Y_values1, r_values1))

    r_equilibrio = np.array(solution[0][1])
    y_equilibrio = np.array(M/P + k*solution[0][1])
    
    plt.plot(IS_values, r_values, label='IS 1', color = 'black')
    plt.plot(LM_values, r_values, label='LM 1', color = 'mediumblue')
    plt.scatter(y_equilibrio, r_equilibrio, color='red', zorder=3, label = f"r 1 = {r_equilibrio:.2f}\ny 1 = {y_equilibrio:.2f}")   
    plt.legend()

interact(update_grafico, a=(0, 500), 
         b=(0.1, 1.0), 
         c=(100, 500), 
         d=(10, 50), 
         G=(0, 1000), 
         T=(0, 200), 
         k=(0, 300),
         M=(500, 1500), 
         P=(1, 5))


# In[ ]:




