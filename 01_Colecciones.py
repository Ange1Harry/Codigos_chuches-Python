#Ejemplos de colecciones 

l = [21, True, "ejemplo de lista", [1, 2, 3 ]]

new_variable = l[2] #nueva valor de "ejemplo de lista"

#print (new_variable)

#Lista dentro de lista
l2 = [21, True, False, "Lista exterior", [23, "Lista interior"]]
variable2 = l2[4][1] #Valor nuevo de "lista interior"
#print(variable2)

#Asignacion de nuevo valor 
l2[2] = True
#print(l2)

#Uso de numeros negativos
l3 = [True, 245, "Hola", "MUNDO"]
l3[-1] = "mundo"
#print(l3)

l4 = [100, True, "Lista de salto", [1, 2,3]]
variable3 = l4[0:2] # muesta desde [100, True, "Lista de salto"]
variable4 = l4[0:5:2] #muestra [100, "Lista de salto"]
print(variable4)

