# Sistema de Gestión y Simulación de Pedidos a Domicilio Multizona

## Descripción del Proyecto

Sistema completo de gestión de pedidos a domicilio que simula el funcionamiento de plataformas como Rappi o Uber Eats. El sistema maneja clientes, restaurantes, domiciliarios y el ciclo completo de pedidos utilizando **estructuras de datos implementadas manualmente**.

## Características Principales

- Registro y consulta de clientes, restaurantes y domiciliarios
- Gestión completa del ciclo de pedidos (crear, asignar, entregar, cancelar)
- Búsqueda automática del restaurante más cercano
- Asignación inteligente del domiciliario disponible más cercano
- Mapa de ciudad con zonas y distancias (implementado como grafo)
- Historial de pedidos por cliente
- Reportes y estadísticas del sistema
- Interfaz de consola interactiva

## Estructuras de Datos Utilizadas

1. Lista Enlazada Simple:
- Uso: Almacenamiento de clientes y domiciliarios
- Justificación: Permite inserción eficiente y recorrido secuencial para búsquedas por criterios personalizados

2. Árbol Binario de Búsqueda:
- Uso: Almacenamiento de restaurantes indexados por código
- Justificación: Búsqueda eficiente O(log n) de restaurantes por código, optimizando las consultas frecuentes

3. Cola (Queue - FIFO):
- Uso: 
  - Cola de pedidos pendientes
  - Cola de pedidos en camino
- Justificación: Los pedidos deben atenderse en el orden de llegada (primero en llegar, primero en ser atendido)

4. Pila (Stack - LIFO)
- Uso: 
- Historial de pedidos entregados
- Historial de pedidos cancelados
- Justificación: Los pedidos más recientes son más relevantes para consultas de historial

5.  Grafo:
Representa zonas de la ciudad y rutas entre ellas.

7. Algoritmo de Dijkstra:
Se usa para obtener la distancia mínima entre zonas.


## Estructura del Código

\`\`\`
PROY_FINAL/
│
├── estructuras.py      # Implementación manual de todas las estructuras de datos
├── entidades.py        # Clases Cliente, Restaurante, Domiciliario, Pedido, Menu
├── sistema.py          # Lógica principal del sistema de gestión
├── main.py            # Programa principal con menú de consola
└── README.md          # Este archivo
\`\`\`

## Requisitos

- Python 3.12 
- No requiere librerías externas (todo implementado manualmente)

## Cómo Ejecutar

1. Asegúrate de tener todos los archivos en el mismo directorio

2. Ejecuta el programa principal:
\`\`\`bash
python main.py
\`\`\`

3. Usa la opción 7 del menú principal para cargar datos de prueba

4. Explora las diferentes funcionalidades del sistema

## Flujo de Trabajo Típico

1. **Configuración inicial**:
   - Cargar datos de prueba (opción 7)
   - O registrar manualmente zonas, clientes, restaurantes y domiciliarios

2. **Crear un pedido**:
   - Gestión de Pedidos → Crear nuevo pedido
   - Seleccionar cliente y restaurante
   - Elegir items del menú

3. **Asignar pedido**:
   - El sistema encuentra automáticamente el domiciliario disponible más cercano
   - El pedido pasa de "PENDIENTE" a "EN_CAMINO"

4. **Entregar o cancelar**:
   - Marcar como entregado libera al domiciliario y actualiza su ubicación
   - Cancelar devuelve el domiciliario a disponible

5. **Consultar reportes**:
   - Ver historial de pedidos
   - Consultar estadísticas generales
   - Revisar pedidos por cliente

## Decisiones de Diseño

### ¿Por qué Cola para pedidos pendientes?
Los pedidos deben procesarse en orden de llegada (FIFO). La primera persona que solicita debe ser la primera atendida, garantizando justicia en el servicio.

### ¿Por qué Pila para historial?
Los pedidos más recientes son más relevantes. Al usar pila (LIFO), los últimos pedidos entregados/cancelados están en el tope, facilitando consultas recientes.

### ¿Por qué Árbol para restaurantes?
Las búsquedas por código de restaurante son muy frecuentes al crear pedidos. El árbol BST ofrece búsqueda O(log n), mucho más eficiente que búsqueda lineal.

### ¿Por qué Grafo para el mapa?
El mapa de la ciudad es naturalmente un grafo: nodos (zonas) conectados por aristas (vías) con pesos (distancias). Permite calcular distancias y encontrar ubicaciones cercanas.



## Autores

Daniel Obispo
Ivan Orozco

Proyecto desarrollado para el curso de Estructuras de Datos 2025-II

