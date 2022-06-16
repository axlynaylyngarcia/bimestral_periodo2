""" Programa para calcular la nota final de un estudiante en una materia
por las calificaciones de sus evaluciones"""

print("--------------------------------")
print("------ NOTAS ESTUDIANTES -------")
print("--------------------------------")

#Input
cod = int(input("Digite el código del estudiante: "))
if cod!=0:
   nota1 = float(input("Digite la nota del parcial no. 1:"))
   nota2 = float(input("Digite la nota del parcial no. 2:"))
   nota3 = float(input("Digite la nota del parcial no. 3:"))
   nota4 = float(input("Digite la nota del parcial no. 4:"))
   nota5 = float(input("Digite la nota del parcial no. 5:"))

else:
    print("Fin de los datos de entrada")

#Prossecing
reprobados = 0
while cod != 0:
    nota_final = (nota1 + nota2 + nota3 + nota4 + nota5 )/5
    print("La nota definitiva de el estudiante con el codigo " + str(cod) + " obtuvo una nota definitiva de " + str(nota_final))
    cod = int(input("Digite el cogido de el estudiante: "))
    if cod!=0:
            nota1 = float(input("Digite la nota del parcial no. 1:"))
            nota2 = float(input("Digite la nota del parcial no. 2:"))
            nota3 = float(input("Digite la nota del parcial no. 3:"))
            nota4 = float(input("Digite la nota del parcial no. 4:"))
            nota5 = float(input("Digite la nota del parcial no. 5:"))
    else:        
        print("fin de la entrada")
    if nota_final < 3:
        reprobados = reprobados + 1

#Output 
print(str(reprobados) + " reprobaron la materia")
print("Eso era...")