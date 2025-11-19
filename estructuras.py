from datetime import datetime

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Lista:
    def __init__(self):
        self.frente = None
        self.fin = None

    def insertar_inicio(self, dato): 
        nuevo_nodo = Nodo(dato)
        if self.frente is None:
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.frente
        self.frente = nuevo_nodo

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.frente is None:
            self.frente = nuevo_nodo
        else:
            self.fin.siguiente = nuevo_nodo
        self.fin = nuevo_nodo

    def buscar(self, criterio):
        tmp = self.frente
        while tmp is not None:
            if criterio(tmp.dato):
                return tmp.dato
            tmp = tmp.siguiente
        return None

    def listar_todos(self):
        elementos = []
        tmp = self.frente
        while tmp is not None:
            elementos.append(tmp.dato)
            tmp = tmp.siguiente
        return elementos

    def borrar_nodo(self, busqueda):
        if self.frente is None:
            print("Lista vacía")
            return

        if self.frente.dato == busqueda:
            if self.frente == self.fin:
                self.frente = None
                self.fin = None
            else:
                self.frente = self.frente.siguiente
            return

        tmp = self.frente
        while tmp.siguiente is not None and tmp.siguiente.dato != busqueda:
            tmp = tmp.siguiente

        if tmp.siguiente is None:
            print("Elemento de búsqueda no encontrado")
            return

        objetivo = tmp.siguiente
        tmp.siguiente = objetivo.siguiente

        if tmp.siguiente is None:
            self.fin = tmp

    def esta_vacia(self):
        return self.frente is None

    def recorrer(self):
        tmp = self.frente
        while tmp is not None:
            print(tmp.dato)
            tmp = tmp.siguiente


class Cola:
    def __init__(self):
        self.head = None  
        self.tail = None  
        self.size = 0

    def enqueue(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.head is None:
            self.head = self.tail = nuevo_nodo
        else:
            self.tail.siguiente = nuevo_nodo
            self.tail = nuevo_nodo
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return None
        dato = self.head.dato
        self.head = self.head.siguiente
        if self.head is None:
            self.tail = None
        self.size -= 1
        return dato

    def primer(self):
        if self.head is None:
            return None
        return self.head.dato

    def ultimo(self):
        if self.tail is None:
            return None
        return self.tail.dato

    def tamano(self):
        return self.size

    def listar_todos(self):
        elementos = []
        tmp = self.head
        while tmp is not None:
            elementos.append(tmp.dato)
            tmp = tmp.siguiente
        return elementos

    def esta_vacia(self):
        return self.head is None


class Pila:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.top
        self.top = nuevo_nodo
        self.size += 1
        
    def pop(self):
        if self.top is None:
            return None
        dato = self.top.dato
        self.top = self.top.siguiente
        self.size -= 1
        return dato

    def tope(self):
        if self.top is None:
            return None        
        return self.top.dato

    def tamano(self):
        return self.size

    def listar_todos(self):
        elementos = []
        actual = self.top
        while actual is not None:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

    def esta_vacia(self):
        return self.top is None


class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class ArbolBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato, clave_func):
        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            self._insertar_rec(self.raiz, dato, clave_func)

    def _insertar_rec(self, nodo, dato, clave_func):
        clave_dato = clave_func(dato)
        clave_nodo = clave_func(nodo.dato)
        
        if clave_dato < clave_nodo:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(dato)
            else:
                self._insertar_rec(nodo.izquierdo, dato, clave_func)
        else:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(dato)
            else:
                self._insertar_rec(nodo.derecho, dato, clave_func)

    def buscar(self, clave, clave_func):
        return self._buscar_rec(self.raiz, clave, clave_func)

    def _buscar_rec(self, nodo, clave, clave_func):
        if nodo is None:
            return None
        
        clave_nodo = clave_func(nodo.dato)
        
        if clave == clave_nodo:
            return nodo.dato
        elif clave < clave_nodo:
            return self._buscar_rec(nodo.izquierdo, clave, clave_func)
        else:
            return self._buscar_rec(nodo.derecho, clave, clave_func)

    def listar_inorden(self):
        elementos = []
        self._inorden_rec(self.raiz, elementos)
        return elementos

    def _inorden_rec(self, nodo, elementos):
        if nodo is not None:
            self._inorden_rec(nodo.izquierdo, elementos)
            elementos.append(nodo.dato)
            self._inorden_rec(nodo.derecho, elementos)


class NodoArista:
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso
        self.siguiente = None


class ListaAdyacencia:
    def __init__(self):
        self.primera = None
        self.ultima = None
    
    def agregar_arista(self, destino, peso):
        nueva_arista = NodoArista(destino, peso)
        
        if self.primera is None:
            self.primera = nueva_arista
            self.ultima = nueva_arista
        else:
            self.ultima.siguiente = nueva_arista
            self.ultima = nueva_arista
    
    def buscar_arista(self, destino):
        actual = self.primera
        while actual is not None:
            if actual.destino == destino:
                return actual
            actual = actual.siguiente
        return None
    
    def obtener_todas(self):
        aristas = []
        actual = self.primera
        while actual is not None:
            aristas.append({'destino': actual.destino, 'peso': actual.peso})
            actual = actual.siguiente
        return aristas


class NodoVertice:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_adyacencia = ListaAdyacencia()
        self.siguiente = None


class Grafo:
    def __init__(self):
        self.primer_vertice = None
        self.ultimo_vertice = None
        self.num_vertices = 0
    
    def agregar_vertice(self, nombre):
        if self.buscar_vertice(nombre) is not None:
            return False
        
        nuevo_vertice = NodoVertice(nombre)
        
        if self.primer_vertice is None:
            self.primer_vertice = nuevo_vertice
            self.ultimo_vertice = nuevo_vertice
        else:
            self.ultimo_vertice.siguiente = nuevo_vertice
            self.ultimo_vertice = nuevo_vertice
        
        self.num_vertices += 1
        return True
    
    def buscar_vertice(self, nombre):
        actual = self.primer_vertice
        while actual is not None:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None
    
    def agregar_arista(self, origen, destino, peso):
        vertice_origen = self.buscar_vertice(origen)
        vertice_destino = self.buscar_vertice(destino)
        
        if vertice_origen is None or vertice_destino is None:
            return False
        
        vertice_origen.lista_adyacencia.agregar_arista(destino, peso)
        vertice_destino.lista_adyacencia.agregar_arista(origen, peso)
        
        return True
    
    def obtener_distancia(self, origen, destino):
        if origen == destino:
            return 0
        
        vertice = self.buscar_vertice(origen)
        if vertice is None:
            return float('inf')
        
        arista = vertice.lista_adyacencia.buscar_arista(destino)
        if arista is not None:
            return arista.peso
        
        return float('inf')
    
    def listar_vertices(self):
        vertices = []
        actual = self.primer_vertice
        while actual is not None:
            vertices.append(actual.nombre)
            actual = actual.siguiente
        return vertices
    
    def obtener_adyacentes(self, nombre_vertice):
        vertice = self.buscar_vertice(nombre_vertice)
        if vertice is None:
            return []
        return vertice.lista_adyacencia.obtener_todas()
    
    def mostrar_grafo(self):
        print("\n--- REPRESENTACIÓN DEL GRAFO ---")
        actual = self.primer_vertice
        while actual is not None:
            adyacentes = actual.lista_adyacencia.obtener_todas()
            ady_str = ", ".join([f"{a['destino']}({a['peso']}km)" for a in adyacentes])
            print(f"{actual.nombre} -> {ady_str if ady_str else 'sin conexiones'}")
            actual = actual.siguiente
    
    def bfs(self, inicio):
        if self.buscar_vertice(inicio) is None:
            return []
        
        visitados = set()
        cola = Cola()
        resultado = []
        
        cola.enqueue(inicio)
        visitados.add(inicio)
        
        while not cola.esta_vacia():
            actual = cola.dequeue()
            resultado.append(actual)
            
            vertice = self.buscar_vertice(actual)
            adyacentes = vertice.lista_adyacencia.obtener_todas()
            
            for ady in adyacentes:
                if ady['destino'] not in visitados:
                    visitados.add(ady['destino'])
                    cola.enqueue(ady['destino'])
        
        return resultado
    
    def dijkstra(self, origen, destino=None):
        if self.buscar_vertice(origen) is None:
            return None
        
        distancias = {}
        previos = {}
        no_visitados = []
        
        actual = self.primer_vertice
        while actual is not None:
            distancias[actual.nombre] = float('inf')
            previos[actual.nombre] = None
            no_visitados.append(actual.nombre)
            actual = actual.siguiente
        
        distancias[origen] = 0
        
        while len(no_visitados) > 0:
            minimo = None
            for vertice in no_visitados:
                if minimo is None or distancias[vertice] < distancias[minimo]:
                    minimo = vertice
            
            if distancias[minimo] == float('inf'):
                break
            
            no_visitados.remove(minimo)
            
            if destino is not None and minimo == destino:
                break
            
            vertice_actual = self.buscar_vertice(minimo)
            adyacentes = vertice_actual.lista_adyacencia.obtener_todas()
            
            for ady in adyacentes:
                vecino = ady['destino']
                peso = ady['peso']
                distancia_alternativa = distancias[minimo] + peso
                
                if distancia_alternativa < distancias[vecino]:
                    distancias[vecino] = distancia_alternativa
                    previos[vecino] = minimo
        
        if destino is not None:
            return self._reconstruir_camino(origen, destino, previos, distancias)
        
        return {'distancias': distancias, 'previos': previos}
    
    def _reconstruir_camino(self, origen, destino, previos, distancias):
        if distancias[destino] == float('inf'):
            return None
        
        camino = []
        actual = destino
        
        while actual is not None:
            camino.insert(0, actual)
            actual = previos[actual]
        
        return {
            'camino': camino,
            'distancia_total': distancias[destino]
        }
    
    def esta_vacio(self):
        return self.primer_vertice is None