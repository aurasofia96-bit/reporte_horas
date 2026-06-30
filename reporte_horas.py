#calcular el total de horas semanales por persona y señalar si alguien excedió las horas estándar.
# horas_trabajador = ["Nombre trabajador", lunes, martes, miercoles, jueves, viernes]
horas_trabajador = [
    ["David", 8, 9, 10, 7, 8],
    ["Liz",8, 7, 8, 6, 8],
    ["Sofia", 8, 7, 7, 9, 9],
    ["Felipe", 8, 8, 8, 8, 8]
]
# Función para calcular horas semanales
def suma_horas (horas):
    """ Suma de horas por trabajador
    Ingresa: Horas del trabajador en la semana
    Sale: Horas semanales del trabajador. """
    suma = 0
    for dia in range(1,len(horas)):
        suma += horas[dia]
    return suma
# Función para clasificar la jornada
def clasificar_jornada (suma_trabajador):
    """ Clasificación de la Jornada segun las horas laboradas en la semana
    Ingresa: Total horas laboradas
    Sale: clasificación. """
    if suma_trabajador > 40:
        clase = "Sobretiempo"
    elif suma_trabajador == 40:
        clase = "Horario Estándar"
    else:
        clase = "Inferior"
    return clase
#Mostrar resultados
print("-"*50)
print("\n Reporte de horas semanales por trabajador \n")
print("-"*50)
for trabajador in horas_trabajador:
    suma = suma_horas(trabajador)
    clase = clasificar_jornada(suma)
    print(f"\nNombre del trabajador: {trabajador[0]}")
    print(f"Total de horas semanales: {suma}")
    print(f"Clasificación de jornada: {clase}")
