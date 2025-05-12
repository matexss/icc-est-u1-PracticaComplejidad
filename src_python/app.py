
from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt
from datetime import datetime

if __name__ == "__main__":

    metodos = MetodosOrdenamiento()
    benchmarking = Benchmarking()

    tamanios = [5000,10000,30000,50000,100000]
    resultados = []
     # métodos de ordenamiento
    metodosD = {
        "burbuja": metodos.sortByBubble,
        "burbuja optimizado": metodos.sortByBubbleOptimizado,
        "seleccion": metodos.sortBySelection,
        "insercion": metodos.sortByInsertion,
        "shell": metodos.sortByshell,

    }

    # Ejecutar cada método con cada tamaño
    for tam in tamanios:
        arreglo_base = benchmarking.build_arreglo(tam)

        for nombre, metodo in metodosD.items():
            tiempo = benchmarking.medir_tiempo(metodo, arreglo_base)
            tuplaResultado = (tam, nombre, tiempo)
            resultados.append(tuplaResultado)

    # Mostrar resultados en consola
    for resultado in resultados:
        tam, nombre, tiempo = resultado
        print(f"tamaño: {tam}, método:  {nombre}, tiempo: {tiempo:.6f} segundos")

    # Clasificar los tiempos según el método
    tiempos_by_metodo = {
        "burbuja": [],
        "burbuja optimizado": [],
        "seleccion": [],
        "insercion": [],
        "shell": [],
    }

    # Clasificar los métodos según su nombre
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)

    # Crear una gráfica
    plt.figure(figsize=(10, 6))

    # Graficar una línea de tiempo para cada método
    # x = tamaño del arreglo, y = tiempo obtenido
    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label=nombre, marker='o')


    now = datetime.now()
    titulo_ventana = f"Mateo Morejon - {now.strftime('%Y-%m-%d %H:%M')}"
    plt.gcf().canvas.manager.set_window_title(titulo_ventana)

    # Agregar parámetros visuales
    plt.title("Comparación de tiempos de ordenamiento")
    plt.suptitle(titulo_ventana)
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo (segundos)")
    plt.grid(True)
    plt.legend()  # Muestra qué color representa cada método
    plt.show()