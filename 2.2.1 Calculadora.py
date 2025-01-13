
my_operacion= input ('Selecciona la operación a realizar: 1 Suma, 2 Resta, 3 Multiplicación, 4 División')

#Seleccionamos la operación
my_valor= input ('Dime el primer dígito')
my_valor2= input ('Dime el segundo dígito')

my_valor=int(my_valor)
my_valor2=int(my_valor2)

#Como input devuelve un string ponemos "1"
if my_operacion=="1":
    result=my_valor+my_valor2
    print("El resultado es", result)

elif my_operacion=="2":
    result=my_valor-my_valor2
    print("El resultado es", result)

elif my_operacion=="3":
    result=my_valor*my_valor2
    print("El resultado es", result)

elif my_operacion=="4":
    result=my_valor/my_valor2
    print("El resultado es", result)