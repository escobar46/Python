otroscusos_min= 2.5
otroscusos_max= 7
otroscusos_promedio= 4
dalto_curso= 1.5

#duracion del video crudo

crudo_dalto=3.5
crudo_promedio=5


#diferencia de duracion 

diferencia_min= 100-dalto_curso/otroscusos_min*100
diferencia_max= 100-dalto_curso*1000//otroscusos_max / 10
diferencia_promedio= 100-dalto_curso/otroscusos_promedio*100


#calculando el porcentaje de tiempo vacio promedio 
tiempo_vacio= 100 - otroscusos_promedio *1000 // crudo_promedio/10
#la formula sirve para rondear los datos y darle decimales 
tiempo_vacio_dalto= 100 - dalto_curso *1000 // crudo_dalto/10

print(f'el curso de dalto dura  {diferencia_min}%  menos el mas rapido ')