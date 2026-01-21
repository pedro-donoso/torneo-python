import statistics as stats

participantes = []
equipos = []
partidas = []

def registrar():
    print("--- REGISTRAR JUGADOR/A ---")
    nombre = input("➤ Ingresa NOMBRE JUGADOR/A: ").strip()
    while not nombre:
        print("❌ NOMBRE requerido!")
        nombre = input("➤ Ingresa NOMBRE JUGADOR/A: ").strip()

    while True:
        edad = input("➤ EDAD (12-70): ")
        try:
            edad = int(edad)
            if 12 <= edad <= 70: break
            print("❌ 12-70 años")
        except: print("❌ EDAD requerida, ingresa Número")
    
    while True:
        nivel = input("➤ NIVEL (1-5): ")
        try:
            nivel = int(nivel)
            if 1 <= nivel <= 5: break
            print("❌ 1-5")
        except: print("❌ NIVEL requerido, ingresa Número")
    
    participantes.append({"nombre": nombre, "edad": edad, "nivel": nivel})
    print("✅ Jugador/a Registrado")

def formar_equipo():
    libres = [p for p in participantes if not any(p["nombre"] in [j["nombre"] for j in e["integrantes"]] for e in equipos)]
    
    if len(libres) < 2:
        print("❌ Min 2 libres")
        return
    
    print("\n🎮 DISPONIBLES:")
    for i, p in enumerate(libres):
        print(f"  {i+1}. {p['nombre']} (E:{p['edad']}, N:{p['nivel']})")
    
    print("\n👥 EQUIPO")
    while True:
        j1 = input("➤ Jugador 1: ")
        try:
            j1 = int(j1) - 1
            if 0 <= j1 < len(libres): break
            print(f"❌ 1-{len(libres)}")
        except: print("❌ Número")
    
    while True:
        j2 = input("➤ Jugador 2: ")
        try:
            j2 = int(j2) - 1
            if 0 <= j2 < len(libres) and j2 != j1: break
            print(f"❌ Diferente (1-{len(libres)})")
        except: print("❌ Número")
    
    nombre = input("➤ NOMBRE EQUIPO: ").strip()
    while any(e["nombre"] == nombre for e in equipos):
        print("❌ Ya existe!")
        nombre = input("➤ NOMBRE NUEVO: ").strip()
    
    equipos.append({"nombre": nombre, "integrantes": [libres[j1], libres[j2]], "puntos": 0})
    print(f"✅ Equipo'{nombre}' creado")

def mostrar():
    if not equipos:
        print("Sin equipos")
        return
    print("\n🏆 EQUIPOS:")
    for e in equipos:
        print(f"\n{e['nombre']}: {e['puntos']} pts")
        for j in e['integrantes']:
            print(f"  👤 {j['nombre']}")

def registrar_partida():
    print("\n⚔️ PARTIDA")
    mostrar()
    
    eq1 = input("➤ Equipo 1: ").strip()
    eq2 = input("➤ Equipo 2: ").strip()
    
    eq1_ok = eq1 in [e["nombre"] for e in equipos]
    eq2_ok = eq2 in [e["nombre"] for e in equipos]
    
    if not (eq1_ok and eq2_ok):
        print("❌ Equipos inválidos")
        return
    
    ganador = input("➤ Ganador: ").strip()
    if ganador not in [eq1, eq2]:
        print("❌ Eq1 o Eq2")
        return
    
    partidas.append({"eq1": eq1, "eq2": eq2, "ganador": ganador})
    
    for e in equipos:
        if e["nombre"] == ganador:
            e["puntos"] += 3
            print(f"✅ {ganador}: {e['puntos']} pts")
            break

def ranking():
    if not equipos:
        print("Sin equipos")
        return
    
    print("\n🥇 RANKING:")
    ordenados = sorted(equipos, key=lambda e: e["puntos"], reverse=True)
    
    for i, e in enumerate(ordenados, 1):
        print(f"{i}. {e['nombre']}: {e['puntos']} pts")

def reporte_completo():
    print("\n" + "="*60)
    print("📊 REPORTE COMPLETO - TORNE PIXELS RETRO")
    print("="*60)
    
    print("\n👥 PARTICIPANTES REGISTRADOS ({})".format(len(participantes)))
    print("-" * 40)
    for i, p in enumerate(participantes, 1):
        en_equipo = "✅ EN EQUIPO" if any(p["nombre"] in [j["nombre"] for j in e["integrantes"]] for e in equipos) else "⭕ LIBRE"
        print(f"{i:2d}. {p['nombre']:12s} | Edad: {p['edad']:2d} | Nivel: {p['nivel']} | {en_equipo}")
    
    print(f"\n🏆 EQUIPOS FORMADOS ({len(equipos)})")
    print("-" * 50)
    for e in equipos:
        print(f"\n{e['nombre']}")
        print("   Integrantes:")
        for j in e['integrantes']:
            print(f"     • {j['nombre']} (E:{j['edad']}, N:{j['nivel']})")
        print(f"   Puntos totales: {e['puntos']}")
    
    if equipos:
        print("\n🥇 RANKING DE EQUIPOS")
        print("-" * 30)
        ordenados = sorted(equipos, key=lambda e: e["puntos"], reverse=True)
        for i, e in enumerate(ordenados, 1):
            print(f"{i}. {e['nombre']:15s} | {e['puntos']:3d} puntos")
    
    print(f"\n📈 ESTADÍSTICAS")
    print("-" * 20)
    print(f"Partidas jugadas: {len(partidas)}")
    if equipos:
        puntos_totales = sum(e["puntos"] for e in equipos)
        print(f"Puntos totales: {puntos_totales}")
        print(f"Promedio pts/equipo: {puntos_totales/len(equipos):.1f}")

print("=== 🎮 TORNEO PIXELS RETRO ===")
while True:
    print("\n📋 OPCIONES:")
    print("1️⃣ Registrar Jugador/a")
    print("2️⃣ Formar Equipo") 
    print("3️⃣ Ver Equipos")
    print("4️⃣ Partida")
    print("5️⃣ Ranking")
    print("6️⃣ Reporte completo")
    print("7️⃣ Salir")
    opcion = input("➤ Elige una Opción: ").strip()
    
    if opcion == "1": registrar()
    elif opcion == "2": formar_equipo()
    elif opcion == "3": mostrar()
    elif opcion == "4": registrar_partida()
    elif opcion == "5": ranking()
    elif opcion == "6": reporte_completo()
    elif opcion == "7": print("👋 ¡Adios!"); break
    else: print("❌ Requisito opción 1-7")



