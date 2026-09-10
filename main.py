# ● Algoritmos.
# ● Entradas.
# ● Procesos.
# ● Salidas.
# ● Variables.
# ● Tipos de datos.
# ● Operadores aritméticos.
# ● Fórmulas y cálculos.
# ● Conversión de datos.
# ● Reglas de estilo.
# Cantidad de alumnos inscriptos en cada taller.
# Cantidad de alumnos inscriptos en cada turno.
# Cantidad total de inscripciones.
# Cupo disponible de cada taller.
# Porcentaje de cupo utilizado.
# Dinero total recaudado.
# Dinero recaudado por cada taller.
# Ganancia de cada taller.
# Turno más exitoso de cada taller.
# Talleres más concurridos.
# Ranking de los talleres según cantidad de alumnos.
# Ranking de los turnos según cantidad de alumnos o porcentaje de cupo utilizado.



#region - Constantes y variables
VALOR_POR_TALLER = 10000
CUPOS_POR_TALLER = 50
CUPOR_EXTENDIDO = 75
costo_taller_ia = 3000
costo_taller_programacion = 2500
costo_taller_diseno = 2000
costo_taller_juegos = 5000
cantidad_ia = 0 
cantidad_programacion = 0 
cantidad_diseno = 0 
cantidad_juegos = 0 
cantidad_tm = 0
ia_tm = 0
progra_tm = 0
diseno_tm = 0
juegos_tm = 0
cantidad_tt = 0 
ia_tt = 0
progra_tt = 0
diseno_tt = 0
juegos_tt = 0
cantidad_tn = 0 
ia_tn = 0
progra_tn = 0
diseno_tn = 0
juegos_tn = 0

recaudacion_ia = 0
ganancia_ia = 0
ganancia_programacion = 0
ganancia_diseno = 0
ganancia_juego = 0

bandera_aumento = False
#endregion

print("--------------ADMINISTRACIÓN DE TALLERES--------------")
print("\n---CARGA DE DATOS---")

#region -IA
print("\n--Taller IA--\n")
print("Ingrese la cantidad inscriptos para cada turno.\n")
ia_tm = int(input("TALLER IA - Turno mañana: "))
cantidad_ia += ia_tm
ia_tt = int(input("TALLER IA - Turno tarde: "))
cantidad_ia += ia_tt
ia_tn = int(input("TALLER IA - Turno noche: "))
cantidad_ia += ia_tn

print()
if ia_tm > 50:
    print("Turno mañana excedido, considere reorganización")
else:
    disponibles = CUPOS_POR_TALLER - ia_tm 
    print(f"Cupos disponibles - Turno mañana: {disponibles}")
if ia_tt > 50:
    print("Turno tarde excedido, considere reorganización")
else:
    disponibles = CUPOS_POR_TALLER - ia_tt 
    print(f"Cupos disponibles - Turno tarde: {disponibles}")
if ia_tn > 50:
    print("Turno noche excedido, considere reorganización")
else:
    disponibles = CUPOS_POR_TALLER - ia_tn 
    print(f"Cupos disponibles - Turno noche: {disponibles}")

recaudacion_ia = cantidad_ia * VALOR_POR_TALLER 
print(f"\nSe obtiene una recaudación total de ${recaudacion_ia}-\n")

# regla n°1
if cantidad_ia > 120:
    print("Taller con alta concurrencia, evalúe incrementar el costo destinado por persona ")
    aumento = str(input("desea aumentar el costo destinado por persona?:(si/no) "))
    if aumento == "si":
        bandera_aumento = True
        costo_taller_ia += 500




ganancia_ia = recaudacion_ia - (costo_taller_ia * cantidad_ia)
if bandera_aumento == True:
    print(f"\nLa ganacia generada adecuada a los arreglos de costos es de ${ganancia_ia}-")      
else:
    print(f"\nLa ganacia generada es de ${ganancia_ia}-")      
#endregion



# cantidad_ia = 0 
# cantidad_programacion = 0 
# cantidad_diseno = 0 
# cantidad_juegos = 0 
# cantidad_tt = 0 
# cantidad_tn = 0 
# cantidad_tm = 0

# # Entradas

# # Total_alumnos = int(input("Ingrese el total de alumnos: "))
# tipo_taller = input("Ingrese el taller: (1.ia 2.Programacion 3.Diseño grafico 4.Juegos: )")
# cantidad_gente_taller = int(input("Ingrese la cantidad de gente por taller: "))
# if cantidad_gente_taller >45:
#     print("Limite de cupos excedido.Ingrese una cantidad <= 45")
#     cantidad_gente_taller = int(input("Ingrese la cantidad de gente por taller: ")) 

# turno_seleccionado = input("Ingrese el turno: ")



# #Procesos 
#     # Ganacia_neta_total= (valor_taller - costo_taller) * Total_alumnos
#     # ganacia_cada_taller = (cantidad_gente_taller * valor_taller)




# #Salidas
