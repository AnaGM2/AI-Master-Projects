# %% [markdown]
# # Práctica 1 Lógica Fuzzy
# ## Contextualización: Clasificación Bioclimática de un Ecosistema
# Modelar las siguientes variables lingüísticas:
# * RETP: Ratio de Evapotranspiración potencial.
# * Concepto = $ETP / PP$
# * Unidad de medida: no (porque es un ratio).
# * Universo / rango: [0, 64]
# * Valores lingüísticos (provincias de humedad)
# * Superárido: [16,32]
# * Preárido: [8]
# * Árido: [4]
# * Semiárido: [2]
# * Subhúmedo: [1]
# * Húmedo: [0.5]
# * Perhúmedo: [.25]
# * Superhúmedo: [.125]
# * Semisaturado: [.0625]
# * Subsaturado: [.03125]
# Solapamiento: 20% de cada franja.
# Funciones de pertenencia: trapezoidal
# * BT: BioTemperatura
# * Unidad: ºC
# * Universo / rango: [1.5, 30]
# * LAT: Latitud
# * 
# * ALT: Altitud
# * 

# %%
import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt

universo=np.arange(0,64.01,0.01)
universo

# %%
superarido = fuzz.trapmf(universo, [12, 20, 64, 64])
prearido = fuzz.trapmf(universo, [6, 10, 12, 20])
arido = fuzz.trapmf(universo, [3, 6, 6, 10])
semiarido = fuzz.trapmf(universo, [1.75, 3, 3, 6])
subhumedo = fuzz.trapmf(universo, [0.8, 1.2, 1.75, 3])
humedo = fuzz.trapmf(universo, [0.4, 0.6, 0.8, 1.2])
perhumedo = fuzz.trapmf(universo, [0.2, 0.3, 0.4, 0.6])
superhumedo = fuzz.trapmf(universo, [0.1, 0.2, 0.2, 0.3])
semisaturado = fuzz.trapmf(universo, [0.05, 0.07, 0.1, 0.2])
subsaturado = fuzz.trapmf(universo, [0, 0.04, 0.05, 0.07])
retp = [superarido, prearido, arido, semiarido, subhumedo, humedo, perhumedo, superhumedo, semisaturado, subsaturado]
labels = ["superarido", "prearido", "arido", "semiarido", "subhumedo", "humedo", "perhumedo", "superhumedo", "semisaturado", "subsaturado"]

# %%
# Graficar
for conjunto, label in zip(retp, labels):
    plt.plot(universo, conjunto, label=label)

# Etiquetas y título
plt.title('RETP')
plt.xlabel('Universo')
plt.ylabel('Grado de Pertenencia')
plt.xscale(value="log")
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

# %%
superarido_comp = fuzz.fuzzy_not(superarido)
# Graficar
plt.plot(universo, superarido, label="superarido", color='blue')
plt.plot(universo, superarido_comp, label="complementario", color='red')


# Etiquetas y título
plt.title('Complementario')
plt.xlabel('Universo')
plt.ylabel('Grado de Pertenencia')
plt.xscale(value="log")
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()


# %%
valores = [10, 20, 30]
pertenencia = [[ fuzz.interp_membership(universo,conjunto, x) for conjunto in retp] for x in valores]
pertenencia

# %%
for i in range(len(retp)-1):
    interseccion = fuzz.fuzzy_and(universo,retp[i],universo,retp[i+1])[1] #no olvidar!!!!
    plt.plot(universo, interseccion, label=labels[i] + "^" + labels[i+1])

# Etiquetas y título
plt.title('Intersecciones')
plt.xlabel('Universo')
plt.ylabel('Grado de Pertenencia')
plt.xscale(value="log")
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

# %%
i = 5    
union = fuzz.fuzzy_or(universo,retp[i],universo,retp[i+1])[1] #no olvidar!!!!
plt.plot(universo, union, label=labels[i] + " U " + labels[i+1])

# Etiquetas y título
plt.title('Uniones')
plt.xlabel('Universo')
plt.ylabel('Grado de Pertenencia')
plt.xscale(value="log")
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

# %%
universo_lat=np.arange(0,90.01,1)
universo_lat

tropical = fuzz.trapmf(universo_lat, [0, 6, 10, 13])
subtropical = fuzz.trapmf(universo_lat, [13, 20, 25, 27.30])
templadoCalido = fuzz.trapmf(universo_lat, [27.30, 35, 40, 42])
templadoFrio = fuzz.trapmf(universo_lat, [42, 50, 55, 58.30])
boreal = fuzz.trapmf(universo_lat, [58.30, 60, 62, 63.48])
subpolar = fuzz.trapmf(universo_lat, [63.48, 64, 66, 68])
polar = fuzz.trapmf(universo_lat, [68, 73, 87, 90])
lat = [tropical, subtropical, templadoCalido, templadoFrio, boreal, subpolar, polar]
labelslat = ["tropical", "subtropical", "templadoCalido", "templadoFrio", "boreal", "subpolar", "polar"]

# %%
# Graficar
for conjunto, label in zip(lat, labelslat):
    plt.plot(universo_lat, conjunto, label=label)

# Etiquetas y título
plt.title('LAT')
plt.xlabel('Universo')
plt.ylabel('Grado de Pertenencia')
plt.xscale(value="log")
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

# %%
universo_alt=np.arange(0,5000,150)
universo_alt

basal = fuzz.trapmf(universo_alt, [0, 50, 600, 1000])
premontano = fuzz.trapmf(universo_alt, [1000, 1200, 1800, 2000])
montanoBajo = fuzz.trapmf(universo_alt, [2000, 2200, 2800, 3000])
montano = fuzz.trapmf(universo_alt, [3000, 3200, 3800, 4000])
subalpino = fuzz.trapmf(universo_alt, [4000, 4100, 4400, 4500])
alpino = fuzz.trapmf(universo_alt, [4500, 4550, 4650, 4750])
nival = fuzz.trapmf(universo_alt, [4750, 4850, 4950, 5000])
alt = [basal, premontano, montanoBajo, montano, subalpino, alpino, nival]
labelsalt = ["basal", "premontano", "montanoBajo", "montano", "subalpino", "alpino", "nival"]

# %%
# Graficar
for conjunto, label in zip(alt, labelsalt):
    plt.plot(universo_alt, conjunto, label=label)

# Etiquetas y título
plt.title('ALT')
plt.xlabel('Universo')
plt.ylabel('Grado de Pertenencia')
plt.xscale(value="log")
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

# %%
universoPP=np.arange(0,16000,60)
universoPP

semisaturado = fuzz.trapmf(universoPP, [0, 0, 0, 0])
subsaturado = fuzz.trapmf(universoPP, [0, 10, 55, 62.5])
superarido = fuzz.trapmf(universoPP, [62.5, 70, 110, 125])
prearido = fuzz.trapmf(universoPP, [110, 125, 200, 250])
arido = fuzz.trapmf(universoPP, [250, 300, 400, 500])
semiarido = fuzz.trapmf(universoPP, [400, 500, 900, 1000])
subhumedo = fuzz.trapmf(universoPP, [900, 1000, 1800, 2000])
humedo = fuzz.trapmf(universoPP, [1800, 2000, 3800, 4000])
perhumedo = fuzz.trapmf(universoPP, [3800, 4000, 7500, 8000])
superhumedo = fuzz.trapmf(universoPP, [7500, 8000, 15000, 16000])
pp = [superarido, prearido, arido, semiarido, subhumedo, humedo, perhumedo, superhumedo, semisaturado, subsaturado]
labelspp = ["superarido", "prearido", "arido", "semiarido", "subhumedo", "humedo", "perhumedo", "superhumedo", "semisaturado", "subsaturado"]

# %%
# Graficar
for conjunto, label in zip(pp, labelspp):
    plt.plot(universoPP, conjunto, label=label)

# Etiquetas y título
plt.title('PP')
plt.xlabel('Universo')
plt.ylabel('Grado de Pertenencia')
plt.xscale(value="log")
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

# %%
universo_bt=np.arange(0,30,0.5)
universo_bt

tropical = fuzz.trapmf(universo_bt, [24, 24.5, 29.5, 30])
subtropical = fuzz.trapmf(universo_bt, [18, 18.5, 23.5, 24])
templadoCalido = fuzz.trapmf(universo_bt, [12, 12.5, 17.5, 18])
templadoFrio = fuzz.trapmf(universo_bt, [6, 6.5, 11.5, 12])
boreal = fuzz.trapmf(universo_bt, [3, 3.5, 5.5, 6])
subpolar = fuzz.trapmf(universo_bt, [1.3, 1.5, 2.5, 3])
polar = fuzz.trapmf(universo_bt, [0, 0.2, 1, 1.3])
bt = [tropical, subtropical, templadoCalido, templadoFrio, boreal, subpolar, polar]
labelsbt = ["tropical", "subtropical", "templadoCalido", "templadoFrio", "boreal", "subpolar", "polar"]

# %%
# Graficar
for conjunto, label in zip(bt, labelsbt):
    plt.plot(universo_bt, conjunto, label=label)

# Etiquetas y título
plt.title('BT')
plt.xlabel('Universo')
plt.ylabel('Grado de Pertenencia')
plt.xscale(value="log")
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()


