from ast import While


print("----------------------------------")
print("-------- cheques, y gasto al final del dia -------")
print("----------------------------------")

#Entrada

Valor_del_cheque = int (input ('Ingresa el valor del cheque: '))
total_monedas_de_100=0
total_billetes_de_10000=0
total_billetes_de_2000=0

#Processing
while Valor_del_cheque !=0:
    monedas_de_100=Valor_del_cheque
    billetes_de_10000=(monedas_de_100-monedas_de_100%10000)//10000
    monedas_de_100=monedas_de_100%10000
    billetes_de_2000=(monedas_de_100-monedas_de_100%2000)//2000
    monedas_de_100=monedas_de_100%2000
    monedas_de_100=(monedas_de_100-monedas_de_100%100)//100
    monedas_de_100=monedas_de_100%100   
    print ('valor de billetes de 10000: ' + repr (billetes_de_10000))
    print ('valor de billetes de 2000: ' + repr (billetes_de_2000))
    print ('valor de monedas de 100: ' + repr (monedas_de_100))
    total_monedas_de_100=total_monedas_de_100 + monedas_de_100
    total_billetes_de_10000=total_billetes_de_10000 + billetes_de_10000
    total_billetes_de_2000=total_billetes_de_2000 + billetes_de_2000
    Valor_del_cheque = int (input ('Ingresa el valor de tu cheque: '))


else:
    print("Fin de ingreso de datos")

#output

print("El total de billetes de 10000 en el dia fue de " + str(total_billetes_de_10000))
print("El total de billetes de  2000 en el dia fue de " + str(total_billetes_de_2000))
print("El total de monedas de 100 en el dia fue de " + str(total_monedas_de_100))