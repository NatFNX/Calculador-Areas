#Tarea 1
#test, guardar cambios

#importamos una libreria (recomendacion de chatti para que sea mas exacto que definir el float de pi jiji)
import math

print()  # imprimo una línea vacía para hacer un enter y se vea mas wonito :3
print()  
print("Hola!")
print()  
print("Para calcular el Area Total, porfavor indique las medidas de las partes del muñeco en el orden indicado")
print("y presione Enter, cada vez que agregue un valor")  
print()

ancho_brazo = float (input ("Ancho de un brazo:"))        
altura_brazo = float (input ("Altura de un brazo:"))

ancho_pierna = float (input ("Ancho de una pierna:"))
altura_pierna = float (input ("Altura de una pierna:")) 

ancho_tronco = float (input ("Ancho del tronco:"))
altura_tronco = float (input ("Altura del tronco:"))

base_sombrero = float (input ("Base del sombrero:"))
altura_sombrero = float (input ("Altura del sombrero:"))

radio = float (input ("Radio de la cabeza: "))

print() 
print("Gracias! calculando...")
print() 

#Area del Brazo - rectangulo= (Base * Altura)
area_brazo = ancho_brazo * altura_brazo
print ("Area de un brazo")
print(area_brazo)
# x2
brazos= area_brazo *2


#Area de la pierna rectangulo= (Base * Altura) 
area_pierna = ancho_pierna * altura_pierna
print("Area de una pierna:")  
print(area_pierna)  
# x2
piernas = area_pierna * 2

#Area del tronco - rectangulo= (Base * Altura)
area_tronco = ancho_tronco * altura_tronco
print(f"Area del tronco:{area_tronco:.2f}")  

#Area del sombrero - triangulo = (Base * Altura) /2
area_sombrero = (base_sombrero * altura_sombrero) /2
print(f"Area del sombrero: {area_sombrero:.2f}") 

#Area de la cabeza - circulo = pi * radio **2
area_cabeza = math.pi * radio**2
# chatti me ayudo a saber como podia mostrar el resultado en la misma linea que imprime el texto
# Usando f-string 
print(f"Area de la cabeza:{area_cabeza: .2f}") 

#Area total - brazos  + pierna x2 + sombrero + cabeza
area_total = piernas + brazos + area_tronco + area_sombrero + area_cabeza

print()  
print()  
# chatti: forma #2 para mostrar el resultado en la misma linea que imprime el texto
# se usa el operador % - se usa el %.2f para indicar al float mostrarse con dos decimales.
print ("Area total del muñeco: %.2f" %area_total )
print()  
print() 
print()  
print() 
