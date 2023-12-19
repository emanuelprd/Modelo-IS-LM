O modelo IS-LM é um dos primeiros modelos que somos introduzidos nas aulas de macroeconomia, ele foi fruto de uma tentativa de modelar a teoria keynesiana e sua formalização pode ser encontrada no famoso paper do John Hicks: Mr. Keynes and the “Classics”, A Suggested Interpretation.

O modelo ilustra as interações do mercado de bens e serviços e do mercado de moeda no curto prazo, as duas variáveis endógenas do modelo é o nível de produto (Y) e taxa de juros (r) que podem ser encontradas no ponto onde a curva IS e LM se interseccionam, ou seja, quando estão em equilíbrio. O modelo é didático para extrair insights de como políticas monetárias e fiscais podem influenciar o produto e juros de uma economia.

Eu fiz em Python um gráfico interativo do modelo baseado no livro-texto de Macroeconomia do Gregory Mankiw e as soluções algébricas estão no apêndice do livro (*). É possível brincar com o modelo para visualizar como um aumento dos gastos (G) ou e da oferta de moeda (M) afetam o equilíbrio de uma economia dentre outros parâmetros. 

(*) A formulação algébrica pode ser vizualida abaixo:


Curva IS

Y = C + I + G

C = a + b * (Y - T)

I = c - d*r

G = G

T = T

Y = a + b * (Y - T) + c - d*r + G

Y - b * Y = (a + c) (G - b * T) - d*r

Y * (1 - b) = (a + c) + (G - b * T) - d*r 

Y = (a + c + G - b * T -d * r) * ( 1 / ( 1 - b ) )


Curva LM

M / P = e* Y + k* r

Y = ( M / P + k * r ) * ( 1 / e )


Parâmetros

a = Consumo autônomo

b = Propensão marginal a consumir

c = Investimento autônomo

d = Sensibilidade do investimento à taxa de juros

G = Gastos do governo

T = Tributos

M = Demanda por moeda

P = Nível de Preços

k = Sensibilidade da demanda por moeda à taxa de juros

e = Sensibilidade demanda por moeda à renda

Referências: 

Macroeconomics, Ed. 5, N. Gregory Mankiw

![Modelo IS-LM](https://github.com/emanuelprd/Modelo-IS-LM/blob/main/modelo%20is-lm.png)
