import curses
import random
import sqlite3
import time

# 1. CONFIGURACIÓN DE LA BASE DE DATOS
def inicializar_bd():
    conexion = sqlite3.connect("records_camiones.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            puntos INTEGER NOT NULL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conexion.commit()
    conexion.close()

def guardar_puntuacion(nombre, puntos):
    conexion = sqlite3.connect("records_camiones.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO records (nombre, puntos) VALUES (?, ?)", (nombre, puntos))
    conexion.commit()
    conexion.close()

def obtener_top_5():
    conexion = sqlite3.connect("records_camiones.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, puntos FROM records ORDER BY puntos DESC LIMIT 5")
    top = cursor.fetchall()
    conexion.close()
    return top


# 2. LÓGICA DEL JUEGO
def juego_camiones(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    # AQUÍ ESTÁ EL ARREGLO REAL: Las columnas exactas en la pantalla
    carriles = [9, 19, 29]
    camion_carril = 1
    camion_y = 15
    obstaculos = []
    puntuacion = 0
    velocidad = 0.1

    while True:
        stdscr.clear()

        # Dibujar carretera
        for y in range(0, 20):
            stdscr.addstr(y, 5, " |")
            stdscr.addstr(y, 15, "|")
            stdscr.addstr(y, 25, "|")
            stdscr.addstr(y, 35, "| ")

        try:
            key = stdscr.getch()
        except Exception:
            key = -1

        if key == ord('q') or key == ord('Q'):
            return None  
        elif key == curses.KEY_LEFT and camion_carril > 0:
            camion_carril -= 1
        elif key == curses.KEY_RIGHT and camion_carril < 2:
            camion_carril += 1

        if random.random() < 0.15:
            carril_obstaculo = random.randint(0, 2)
            if not obstaculos or obstaculos[-1][0] > 2:
                obstaculos.append([0, carril_obstaculo])

        nuevos_obstaculos = []
        colision = False

        for obs in obstaculos:
            obs_y, obs_carril = obs
            obs_y += 1

            if obs_y > 18:
                puntuacion += 1
                continue

            if obs_y == camion_y and obs_carril == camion_carril:
                colision = True

            stdscr.addstr(obs_y, carriles[obs_carril], "[🚗]")
            nuevos_obstaculos.append([obs_y, obs_carril])
        
        obstaculos = nuevos_obstaculos

        if colision:
            stdscr.timeout(-1)
            stdscr.nodelay(False)
            curses.curs_set(1) 
            
            stdscr.addstr(8, 12, "¡GAME OVER!", curses.A_BOLD)
            stdscr.addstr(9, 8, f"Puntuación: {puntuacion} puntos")
            stdscr.addstr(11, 6, "Escribe tu nombre y presiona ENTER:")
            stdscr.refresh()
            
            curses.echo()
            nombre = stdscr.getstr(12, 12, 15).decode('utf-8').strip()
            curses.noecho()
            
            if not nombre:
                nombre = "Anónimo"
                
            return nombre, puntuacion

        stdscr.addstr(camion_y, carriles[camion_carril], "[🚚]", curses.A_REVERSE)
        stdscr.addstr(1, 40, f"Puntos: {puntuacion}", curses.A_BOLD)
        stdscr.addstr(3, 40, "Controles:")
        stdscr.addstr(4, 40, "<-  -> : Moverse")
        stdscr.addstr(5, 40, "Q      : Salir")

        stdscr.refresh()
        time.sleep(velocidad)


# 3. FLUJO PRINCIPAL
if __name__ == "__main__":
    inicializar_bd()
    
    resultado = curses.wrapper(juego_camiones)
    
    if resultado:
        nombre_jugador, puntos_jugador = resultado
        guardar_puntuacion(nombre_jugador, puntos_jugador)
        print(f"\n✅ ¡Récord guardado correctamente para {nombre_jugador}!")
    
    print("\n===============================")
    print("🏆   TOP 5 MEJORES PUNTAJES   🏆")
    print("===============================")
    
    top_5 = obtener_top_5()
    if not top_5:
        print("¡Aún no hay récords registrados! Sé el primero.")
    else:
        for puesto, (nombre, puntos) in enumerate(top_5, 1):
            print(f"{puesto}. {nombre.ljust(15)} -> {puntos} pts")
    print("===============================\n")
