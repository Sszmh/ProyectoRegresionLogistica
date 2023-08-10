import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

datos = pd.read_csv('datos_clientes.csv')

#Selección de características:
X = datos[['NOMBRE', 'CIUDAD', 'EDAD', 'DINERO INVERTIDO']]
X = pd.get_dummies(X, columns=['NOMBRE', 'CIUDAD'])  
y = datos['RIESGO'].map({'BAJO': 0, 'MEDIO': 1, 'ALTO': 2})  

#División de datos en conjuntos de entrenamiento:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Construcción del modelo:
model = LogisticRegression()

#Entrenamiento del modelo:
model.fit(X_train, y_train)

#Evaluación del modelo:
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo: {:.2%}".format(accuracy))

#Generacion de las estrategias:
riesgo = {0: 'BAJO', 1: 'MEDIO', 2: 'ALTO'}
estrategia_cliente = model.predict(X)
print("Estrategia del cliente:", [riesgo[estrategia] for estrategia in estrategia_cliente])

#Cecesidades de los clientes y generación de portafolios:

datos_clientes_encoded = pd.get_dummies(datos, columns=['RIESGO', 'CIUDAD'])

necesidades_clientes = ['RIESGO_ALTO', 'RIESGO_MEDIO', 'RIESGO_BAJO', 'EDAD', 'DINERO INVERTIDO']
puntajes_importancia = [0.1, 0.2, 0.1, 0.3, 0.3]

#Calcular las puntuaciones de las estrategias:
puntuaciones_estrategias = []
for i in range(len(estrategia_cliente)):
    puntuacion_total = 0
    for j, necesidad in enumerate(necesidades_clientes):
        valor_necesidad = datos_clientes_encoded[necesidad][i]
        puntuacion_total += valor_necesidad * puntajes_importancia[j]
    puntuaciones_estrategias.append(puntuacion_total)

#Imprimir las puntuaciones:
for i, puntuacion in enumerate(puntuaciones_estrategias):
    print("Puntuación estrategia {}: {:.2f}".format(i+1, puntuacion))

estrategias_ordenadas = sorted(estrategia_cliente, key=lambda x: puntuaciones_estrategias[x], reverse=True)

num_portafolios_modelo = 4
portafolios_modelo = estrategias_ordenadas[:num_portafolios_modelo]

print("Portafolios modelo recomendados:")
for i, portafolio in enumerate(portafolios_modelo):
    print(f"Portafolio {i+1}: {portafolio}")

