# =========================================================
# ROBOT PASEADOR DE PERROS AUTÓNOMO
# =========================================================
#
# SISTEMA COMPLETO INTERACTIVO
#
# FUNCIONES:
#
# 1. PREPARAR PARA SALIR
#    a. indicar origen y destino
#    b. tomar bolsas
#    c. coger correa
#    d. colocar correa
#
# 2. PASEAR AL PERRO
#    a. comprobar correa
#    b. detectar obstáculos
#    c. dejar oler
#    d. interacción segura
#    e. nunca soltar correa
#
# 3. RECOGER NECESIDADES
#    a. detectar necesidades
#    b. tomar bolsa
#    c. recoger excremento
#    d. cerrar bolsa
#    e. botar basura
#
# 4. VOLVER A CASA
#    a. no volver hasta hacer necesidades
#    b. volver al origen
#    c. quitar correa
#    d. avisar propietario
#    e. modo reposo
#
# =========================================================


# =========================================================
# IMPORTAR LIBRERÍAS
# =========================================================

import heapq
import random
import time


# =========================================================
# VARIABLES GLOBALES
# =========================================================

# Estado de la correa
perro_atado = False

# Estado de necesidades
necesidades_realizadas = False

# Estado del robot
robot_activo = True


# =========================================================
# MAPA DEL ENTORNO
# =========================================================
#
# FORMATO:
# "PUNTO":
# [
#   ("DESTINO", distancia, riesgo)
# ]
#
# riesgo:
# 0 = seguro
# 10 = muy peligroso
# =========================================================

mapa = {

    "Casa": [
        ("Parque", 5, 2),
        ("Avenida", 3, 8)
    ],

    "Avenida": [
        ("Casa", 3, 8),
        ("Parque", 4, 7)
    ],

    "Parque": [
        ("Casa", 5, 2),
        ("Avenida", 4, 7),
        ("Pipican", 2, 1)
    ],

    "Pipican": [
        ("Parque", 2, 1)
    ]
}


# =========================================================
# FUNCIÓN:
# VOZ DEL ROBOT
# =========================================================

def hablar_robot(mensaje):

    """
    Simula la voz del robot.
    """

    print(f"\n🤖 ROBOT: {mensaje}")

    time.sleep(1)


# =========================================================
# FUNCIÓN:
# ESCUCHAR AL USUARIO
# =========================================================

def escuchar_usuario():

    """
    Captura respuesta del usuario.
    """

    respuesta = input("\n🧑 TÚ: ")

    return respuesta.lower()


# =========================================================
# FUNCIÓN:
# CALCULAR MEJOR RUTA
# =========================================================

def calcular_mejor_ruta(mapa, origen, destino):

    """
    Calcula la ruta más segura.
    """

    # Cola de prioridad
    cola = []

    # Insertar origen
    heapq.heappush(cola, (0, origen, []))

    # Nodos visitados
    visitados = set()

    # Bucle principal
    while cola:

        # Extraer menor costo
        costo_actual, punto_actual, ruta = heapq.heappop(cola)

        # Evitar repetir
        if punto_actual in visitados:
            continue

        # Marcar visitado
        visitados.add(punto_actual)

        # Agregar a ruta
        ruta = ruta + [punto_actual]

        # Verificar destino
        if punto_actual == destino:

            return costo_actual, ruta

        # Revisar vecinos
        for vecino, distancia, riesgo in mapa[punto_actual]:

            if vecino not in visitados:

                # Penalizar riesgos
                costo_total = (
                    costo_actual
                    + distancia
                    + (riesgo * 2)
                )

                # Insertar nueva ruta
                heapq.heappush(
                    cola,
                    (
                        costo_total,
                        vecino,
                        ruta
                    )
                )

    return float("inf"), []


# =========================================================
# TAREA 1:
# PREPARAR PARA SALIR
# =========================================================

def preparar_para_salir():

    global perro_atado

    hablar_robot("¿Estás listo para salir?")

    respuesta = escuchar_usuario()

    if respuesta not in ["si", "sí", "ok", "claro"]:

        hablar_robot("Esperaré instrucciones.")

        return False

    # =====================================================
    # ORIGEN Y DESTINO
    # =====================================================

    hablar_robot("Indica el origen.")

    origen = input("\nOrigen: ")

    hablar_robot("Indica el destino.")

    destino = input("\nDestino: ")

    # Validar mapa
    if origen not in mapa:

        hablar_robot("El origen no existe.")

        return False

    if destino not in mapa:

        hablar_robot("El destino no existe.")

        return False

    # =====================================================
    # PLANIFICAR RUTA
    # =====================================================

    hablar_robot("Calculando mejor ruta.")

    time.sleep(2)

    costo, ruta = calcular_mejor_ruta(
        mapa,
        origen,
        destino
    )

    print("\n===================================")
    print(" RUTA CALCULADA ")
    print("===================================")

    print("\nRuta segura:")

    print(" -> ".join(ruta))

    print(f"\nCosto total: {costo}")

    # =====================================================
    # TOMAR BOLSAS
    # =====================================================

    hablar_robot("Tomando bolsas.")

    time.sleep(2)

    hablar_robot("Bolsas aseguradas.")

    # =====================================================
    # COGER CORREA
    # =====================================================

    hablar_robot("Cogiendo correa.")

    time.sleep(2)

    hablar_robot("Correa asegurada.")

    # =====================================================
    # COLOCAR CORREA
    # =====================================================

    hablar_robot("¿Puedo colocar la correa al perro?")

    respuesta = escuchar_usuario()

    if respuesta not in ["si", "sí", "ok"]:

        hablar_robot("Operación cancelada.")

        return False

    hablar_robot("Reconocimiento facial canino iniciado.")

    time.sleep(2)

    hablar_robot("Perro identificado.")

    hablar_robot("Analizando lenguaje corporal.")

    time.sleep(2)

    estado = "tranquilo"

    print(f"\n🐶 Estado detectado: {estado}")

    hablar_robot("Colocando correa.")

    time.sleep(3)

    perro_atado = True

    hablar_robot("Correa colocada correctamente.")

    return True


# =========================================================
# TAREA 2:
# PASEAR AL PERRO
# =========================================================

def pasear_perro():

    global perro_atado

    # =====================================================
    # COMPROBAR CORREA
    # =====================================================

    hablar_robot("Comprobando seguridad de la correa.")

    time.sleep(2)

    if not perro_atado:

        hablar_robot("ERROR. El perro no está asegurado.")

        return False

    hablar_robot("Correa correctamente asegurada.")

    # =====================================================
    # SIMULACIÓN DEL PASEO
    # =====================================================

    hablar_robot("Iniciando paseo.")

    # Obstáculos posibles
    obstaculos = [
        "escaleras",
        "anden",
        "otro perro",
        "peatón"
    ]

    # Simular recorrido
    for paso in range(3):

        # ================================================
        # DETECTAR OBSTÁCULOS
        # ================================================

        obstaculo = random.choice(obstaculos)

        hablar_robot(f"Obstáculo detectado: {obstaculo}")

        time.sleep(2)

        # ================================================
        # DEJAR OLER
        # ================================================

        hablar_robot(
            "El perro desea explorar olores."
        )

        hablar_robot(
            "¿Deseas permitirlo?"
        )

        respuesta = escuchar_usuario()

        if respuesta in ["si", "sí", "ok"]:

            hablar_robot(
                "Permitiendo exploración."
            )

            time.sleep(3)

        # ================================================
        # INTERACTUAR CON OTROS PERROS
        # ================================================

        if obstaculo == "otro perro":

            hablar_robot(
                "¿Permitir interacción segura?"
            )

            respuesta = escuchar_usuario()

            if respuesta in ["si", "sí", "ok"]:

                hablar_robot(
                    "Interacción segura iniciada."
                )

                time.sleep(3)

                hablar_robot(
                    "Interacción finalizada."
                )

            else:

                hablar_robot(
                    "Evitando interacción."
                )

        # ================================================
        # NUNCA SOLTAR CORREA
        # ================================================

        hablar_robot(
            "Manteniendo control de la correa."
        )

    return True


# =========================================================
# TAREA 3:
# RECOGER NECESIDADES
# =========================================================

def recoger_necesidades():

    global necesidades_realizadas

    # =====================================================
    # DETECTAR PARADA
    # =====================================================

    hablar_robot(
        "El perro se ha detenido."
    )

    hablar_robot(
        "¿Está haciendo sus necesidades?"
    )

    respuesta = escuchar_usuario()

    if respuesta not in ["si", "sí", "ok"]:

        hablar_robot(
            "Continuando paseo."
        )

        return False

    # =====================================================
    # DETENER ROBOT
    # =====================================================

    hablar_robot(
        "Deteniendo paseo."
    )

    time.sleep(2)

    # =====================================================
    # TOMAR BOLSA
    # =====================================================

    hablar_robot(
        "Tomando bolsa."
    )

    time.sleep(2)

    # =====================================================
    # RECOGER EXCREMENTO
    # =====================================================

    hablar_robot(
        "Recogiendo excremento."
    )

    time.sleep(3)

    # =====================================================
    # CERRAR BOLSA
    # =====================================================

    hablar_robot(
        "Cerrando bolsa."
    )

    time.sleep(2)

    # =====================================================
    # BOTAR BASURA
    # =====================================================

    hablar_robot(
        "Buscando contenedor."
    )

    time.sleep(2)

    hablar_robot(
        "Depositando bolsa en basura."
    )

    time.sleep(2)

    necesidades_realizadas = True

    hablar_robot(
        "Necesidades gestionadas correctamente."
    )

    return True


# =========================================================
# TAREA 4:
# VOLVER A CASA
# =========================================================

def volver_a_casa():

    global perro_atado
    global robot_activo

    # =====================================================
    # VALIDAR NECESIDADES
    # =====================================================

    if not necesidades_realizadas:

        hablar_robot(
            "No regresaré hasta que el perro haga sus necesidades."
        )

        return False

    # =====================================================
    # REGRESAR AL ORIGEN
    # =====================================================

    hablar_robot(
        "Calculando ruta de regreso."
    )

    time.sleep(2)

    hablar_robot(
        "Regresando a casa."
    )

    time.sleep(4)

    hablar_robot(
        "Hemos llegado al origen."
    )

    # =====================================================
    # QUITAR CORREA
    # =====================================================

    hablar_robot(
        "¿Puedo quitar la correa?"
    )

    respuesta = escuchar_usuario()

    if respuesta in ["si", "sí", "ok"]:

        hablar_robot(
            "Quitando correa."
        )

        time.sleep(2)

        perro_atado = False

        hablar_robot(
            "Correa retirada."
        )

    # =====================================================
    # AVISAR PROPIETARIO
    # =====================================================

    hablar_robot(
        "Enviando mensaje al propietario."
    )

    print("\n📱 MENSAJE:")
    print("El perro ha llegado correctamente a casa.")

    # =====================================================
    # MODO REPOSO
    # =====================================================

    hablar_robot(
        "Activando modo reposo."
    )

    robot_activo = False

    time.sleep(2)

    hablar_robot(
        "Sistema en reposo."
    )

    return True


# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

def main():

    print("\n===================================")
    print(" ROBOT PASEADOR DE PERROS ")
    print(" SISTEMA AUTÓNOMO ")
    print("===================================")

    # =====================================================
    # PSEUDOCÓDIGO
    # =====================================================
    #
    # 1. Llamar tarea (1)
    # 2. Llamar tarea (2)
    # 3. Si hace necesidades -> tarea (3)
    # 4. Si hizo necesidades -> tarea (4)
    #
    # =====================================================

    # =====================================================
    # TAREA 1
    # =====================================================

    tarea_1 = preparar_para_salir()

    if not tarea_1:

        hablar_robot(
            "No fue posible iniciar el paseo."
        )

        return

    # =====================================================
    # TAREA 2
    # =====================================================

    tarea_2 = pasear_perro()

    if not tarea_2:

        hablar_robot(
            "Paseo cancelado."
        )

        return

    # =====================================================
    # TAREA 3
    # =====================================================

    recoger_necesidades()

    # =====================================================
    # TAREA 4
    # =====================================================

    if necesidades_realizadas:

        volver_a_casa()


# =========================================================
# INICIO DEL SISTEMA
# =========================================================

if __name__ == "__main__":

    main()