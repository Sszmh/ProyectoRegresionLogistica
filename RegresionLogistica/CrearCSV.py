import csv

datos_clientes = [
    ['Juan', 'Medellin', 35, 2000000, 'ALTO'],
    ['Santiago', 'Bogota', 40, 800000, 'MEDIO'],
    ['Fernando', 'Medellin', 18, 20000, 'BAJO'],
    ['Dylan', 'Cali', 30, 5000000, 'ALTO']
]

nombre_archivo = 'datos_clientes.csv'

#Clasificacion riesgos:
with open(nombre_archivo, 'w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(['NOMBRE', 'CIUDAD', 'EDAD', 'DINERO INVERTIDO', 'RIESGO'])
    for cliente in datos_clientes:
        riesgo = cliente[4]
        if riesgo == 'BAJO':
            riesgo_label = 'BAJO'
        elif riesgo == 'MEDIO':
            riesgo_label = 'MEDIO'
        elif riesgo == 'ALTO':
            riesgo_label = 'ALTO'
        else:
            riesgo_label = 'DESCONOCIDO'
        cliente[4] = riesgo_label
        writer.writerow(cliente)

print("Archivo CSV creado exitosamente.")




