def leer_archivo(nombre_archivo):

    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    lineas = [line.strip() for line in lineas if not line.startswith("#")]

    cantidad_registros = int(lineas[0])

    time_stamps = [tuple(map(int, line.split(','))) for line in lineas[1:cantidad_registros + 1]]

    registros = [int(line) for line in lineas[cantidad_registros + 1:cantidad_registros * 2 + 1]]

    return time_stamps, registros
