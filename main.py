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




VALOR_POR_TALLER = 10000
COSTO_TALLLER_IA = 5000
COSTO_TALLLER_PROGRAMACION = 3000
COSTO_TALLLER_DISENO = 4000
COSTO_TALLLER_JUEGOS = 6000
CUPOS_POR_TALLER = 45
cantidad_ia = 0 
cantidad_programacion = 0 
cantidad_diseno = 0 
cantidad_juegos = 0 
cantidad_tt = 0 
cantidad_tn = 0 
cantidad_tm = 0

# Entradas

# Total_alumnos = int(input("Ingrese el total de alumnos: "))
tipo_taller = input("Ingrese el taller: (1.ia 2.Programacion 3.Diseño grafico 4.Juegos: )")
cantidad_gente_taller = int(input("Ingrese la cantidad de gente por taller: "))
if cantidad_gente_taller >45:
    print("Limite de cupos excedido.Ingrese una cantidad <= 45")
    cantidad_gente_taller = int(input("Ingrese la cantidad de gente por taller: ")) 

turno_seleccionado = input("Ingrese el turno: ")



#Procesos 
    # Ganacia_neta_total= (valor_taller - costo_taller) * Total_alumnos
    # ganacia_cada_taller = (cantidad_gente_taller * valor_taller)




#Salidas
