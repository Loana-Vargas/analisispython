#Ejercicio 1 

def f(x, y):
  return 0.2 * x * y #La función retorna el valor de la derivada en ese punto

#f= funcion 
#x0= valor inicial de x
#y0= el valor inicial de y
#h= el tamaño del paso
#n= numero de pasos 
def euler(f, x0, y0, h, n):
  x = [x0]
  y = [y0]
  for i in range(1, n + 1):
    x.append(x0 + i * h)
    y.append(y0 + h * f(x[i - 1], y[i - 1]))
  return x, y

x0 = 1
y0 = 1

h_1 = 0.1
h_2 = 0.05

x_1, y_1 = euler(f, x0, y0, h_1, 5)
y_1_5 = y_1[4]

x_2, y_2 = euler(f, x0, y0, h_2, 10)
y_2_5 = y_2[9]

print(f"Aproximación de y(1.5) con paso de 0.1: {y_1_5}")
print(f"Aproximación de y(1.5) con paso de 0.05: {y_2_5}")

#ejercicio 2

def f(t, I):
  return 15 - 3 * I


t0 = 0
I0 = 0

t_f = 0.5

h = 0.01

#condición inicial I(0) = 0
# tiempo final t_f = 0.5 segundos
# tamaño del paso h = 0.01 segundos
#I_medio_segundo: corriente en el circuito a los 0.5 segundos

def euler(f, t0, I0, h, n):
  t = [t0]
  I = [I0]
  for i in range(1, n + 1):
    t.append(t0 + i * h)
    I.append(I0 + h * f(t[i - 1], I[i - 1]))
  return t, I

t, I = euler(f, t0, I0, h, int(t_f / h))
I_medio_segundo = I[int(t_f / h)]

print(f"Corriente en el circuito a los 0.5 segundos: {I_medio_segundo} A")







