# REPT
# 0.5 - 1 húmedo
# 1 - 2 subhúmedo
# 4 - 8 árido

# 2**(2-0.25) = 1.75
# 2**2 = 2
# 2**3 = 2
# 2**(3+0.25) = 1.75

# variable linguistica es parametrizada (n)
#n -> etiqueta
# rango: -3 a 5
# universo: 2^-3 a 2^5
# etiqueta n mu(n) = trapecio(2

# rango de temperatura: de -30 a 80 grados en el mundo real en general
# universo: en nuestro caso, en este ejemplo, la temperatura va

# rango es general, grande
# universo es para nuestro problema en particular

# biotemperatura no tiene etiqueta, le ponemos alta, baja, media, etc

# pisos altitudinales: (region(latitud), latitud)) (1...6, 1...7)

# etiqueta: nival([tropical - > 4000, 4750],
# [subtropical -> 3000,..., 4000],...)
# ...
# premontano([tropical -> 0,...,2000],...)

# 6 grados por 1000 metros sobre el nivel del mar

# rango(t) = 0, 1/4, 1/2, 1, 2, 3, 4, 5
# rango(h) = 0, 1, 2, 3, 4, 4.25, 4.5, 4.75, 5
# f[6*t, 1000*h] -> sigma(t,h) = trapecio

# modelar la latitud y la altitud con conjuntos difusos solapandose como veamos
# repartimos en trozos como queramos, nos inventamos las etiquetas de altitud
# usar nombres que queramos, tropico de cancer y crapicornio, ecuador, etc
# y para altitud pues usar alto, medio, bajo, etc

