import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt

inf=1.0
sup=20.0
step=1
universo=np.arange(inf,sup+1,step)
A=fuzz.trimf(universo,[7.5,9,11.5])
B=fuzz.trimf(universo,[8.5,15,18.5])
ejemplo=17.8
gp=fuzz.interp_membership(universo,B,ejemplo)
print("Grado de pertenencia de %f a B es: %f" %(ejemplo,gp))

complementariodeA=fuzz.fuzzy_not(A)
print(complementariodeA)

# Graficar
plt.plot(universo, A, label='A', color='blue')
plt.plot(universo, B, label='B', color='red')

# Etiquetas y título
plt.title('A y B')
plt.xlabel('Universo')
plt.ylabel('Grado de Pertenencia')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()


InterseccionAB=fuzz.fuzzy_and(universo,A,universo,B)[1]#no olvidar!!!!
UnionAB=fuzz.fuzzy_or(universo,A,universo,B)[1]#no olvidar!!!!
print("intersección AB ",InterseccionAB)
print("unión AB ",UnionAB)

# Graficar
plt.plot(universo,InterseccionAB, label='Intersección', color='blue')
plt.plot(universo, UnionAB, label='Unión', color='red')

# Etiquetas y título
plt.title('Intersección y unión de A y B')
plt.xlabel('Universo')
plt.ylabel('Grado de Pertenencia')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()


C=fuzz.trapmf(universo,[2,8,9,12])
D=fuzz.trapmf(universo,[6,7,8,17])

InterseccionCD=fuzz.fuzzy_and(universo,C,universo,D)[1]#no olvidar!!!!
UnionCD=fuzz.fuzzy_or(universo,C,universo,D)[1]#no olvidar!!!!



print("intersección CD ", InterseccionCD)
print("intersección CD ",UnionCD)
plt.plot(universo, C, label='C', color='green')
plt.plot(universo, D, label='D', color='orange')
plt.plot(universo, InterseccionCD, label='Interseccion C D', color='black')
plt.plot(universo, UnionCD, label='Union C D', color='red')
# Etiquetas y título
plt.title('C y D: Intersección y Unión')
plt.xlabel('Universo')
plt.ylabel('Grado de Pertenencia')
plt.legend()
plt.grid(True)
# Mostrar la gráfica
plt.show()


#alpha cortes
alpha=0.4
cortes=fuzz.lambda_cut(B,alpha)
print("B:", B)
print("0.4-cortes de B: ",cortes)
CxD=fuzz.cartprod(C,D)
print("CxD: ",CxD)