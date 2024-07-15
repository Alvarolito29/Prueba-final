import random
import csv
import math

empleados = [
  "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
  "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
  "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]

salarios = []

def asignar_salarios():
  global salarios
  salarios = [random.randint(300000, 2500000) for _ in empleados]
  print("Salarios asignados aleatoriamente.")

def categorizar_salarios():

  menores_300k = [(empleados[i], salario) for i, salario in enumerate(salarios) if salario < 300000]
  entre_300k_2m = [(empleados[i], salario) for i, salario in enumerate(salarios) if 300000 <= salario <= 2500000]
  mayores_2m = [(empleados[i], salario) for i, salario in enumerate(salarios) if salario > 2500000]
  print("\nSueldos minimos a $300.000")

  for empleado, salario in menores_300k:
   print(f"{empleado} - ${salario}")
  print(f"TOTAL: {len(menores_300k)}\n")
  print("Salarios entre $300.000 y $2.500.000")

  for empleado, salario in entre_300k_2m:
   print(f"{empleado} - ${salario}")
  print(f"TOTAL: {len(entre_300k_2m)}\n")
  print("Salarios sobre a $2.500.000")

  for empleado, salario in mayores_2m:
   print(f"{empleado} - ${salario}")
  print(f"TOTAL: {len(mayores_2m)}\n")
  total_salarios = sum(salarios)
  print(f"TOTAL SALARIOS: ${total_salarios}")

def mostrar_estadisticas():
  if not salarios:
   print("Debe asignar los salarios primero.")
   return
  
  salario_mas_alto = max(salarios)
  salario_mas_bajo = min(salarios)
  promedio_salarios = sum(salarios) / len(salarios)
  media_geometrica = math.exp(sum(math.log(salario) for salario in salarios) / len(salarios))
  print(f"\nSalario más alto: ${salario_mas_alto}")
  print(f"Salario más bajo: ${salario_mas_bajo}")
  print(f"Promedio de salarios: ${promedio_salarios}")
  print(f"Media: ${media_geometrica}")

def generar_reporte_salarios():
  if not salarios:
   print("Debe asignar los salarios primero.")
   return

  descuentos_salud = [salario * 0.07 for salario in salarios]
  descuentos_afp = [salario * 0.12 for salario in salarios]
  salarios_liquidos = [salario - salud - afp for salario, salud, afp in zip(salarios, descuentos_salud, descuentos_afp)]
  print("\n|Nombre empleador | Sueldo Base | Descuento Salud | Descuento AFP | Sueldo Líquido|")

  for i in range(len(empleados)):
   print(f"{empleados[i]} | ${salarios[i]} | ${descuentos_salud[i]} | ${descuentos_afp[i]} | ${salarios_liquidos[i]}")

  with open("reporte_salarios.csv", mode='w', newline='') as file:
   writer = csv.writer(file)
   writer.writerow(["Nombre empleado", "Salario Base", "Descuento Salud", "Descuento AFP", "Salario Líquido"])
   for i in range(len(empleados)):
    writer.writerow([empleados[i], salarios[i], descuentos_salud[i], descuentos_afp[i], salarios_liquidos[i]])
  print("\nReporte de salarios generado: reporte_salarios.csv")

def menu():
  
  while True:
   print("------------------------------")
   print("Menú:")
   print("1. Asignar salarios de manera aleatoria")
   print("2. Categorizar salarios")
   print("3. Mostrar estadísticas")
   print("4. Generar reporte de salarios")
   print("5. Salir del programa")

   print("------------------------------")

   opcion = input("Seleccione una opción: ")

   if opcion == '1':
    asignar_salarios()
   elif opcion == '2':
    categorizar_salarios()
   elif opcion == '3':
    mostrar_estadisticas()
   elif opcion == '4':
    generar_reporte_salarios()
   elif opcion == '5':
    print("\n------------------------------")
    print("Finalizando programa...\nDesarrollado: por Alvaro Rivera\n21270647-7")
    print("-------------------------------")
    break
   else:
    print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
  menu()