# Tarifa por hora
tarifa_hora = 90

# Ingresamos la cantidad de horas trabajadas por cada obrero
horas_trabajadas = []
for i in range(1, 81):
    horas_trabajadas.append(int(input("Ingrese las horas trabajadas por el obrero " + str(i) + ": ")))

# Calculamos el sueldo de cada obrero
sueldos = []
for horas in horas_trabajadas:
    sueldo = horas * tarifa_hora
    sueldos.append(sueldo)

# Imprimir la nómina
print("\nNómina de obreros de producción de CellOne")
print("------------------------------------------------------")
print("| Numero de Obrero | Horas trabajadas | Sueldo correspondiente |")
print("------------------------------------------------------")
for i in range(0, 80):
    print("| " + str(i+1).rjust(6) + " | " + str(horas_trabajadas[i]).rjust(15) + " | " + str(sueldos[i]).rjust(22) + " |")
print("------------------------------------------------------")
