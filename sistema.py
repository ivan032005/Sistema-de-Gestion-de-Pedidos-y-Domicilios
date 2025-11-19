from estructuras import Lista, Cola, Pila, ArbolBusqueda, Grafo
from entidades import Cliente, Restaurante, Domiciliario, Pedido

class SistemaGestionPedidos:
    def __init__(self):
        self.clientes = Lista()
        self.restaurantes_arbol = ArbolBusqueda()
        self.restaurantes_lista = Lista()
        self.domiciliarios = Lista()
        self.pedidos_pendientes = Cola()
        self.pedidos_en_camino = Cola()
        self.historial_entregados = Pila()
        self.historial_cancelados = Pila()
        self.mapa_ciudad = Grafo()
        print("Sistema de Gestión de Pedidos inicializado")

    def registrar_cliente(self, codigo, nombre_completo, zona):
        existe = self.clientes.buscar(lambda c: c.codigo == codigo)
        if existe:
            return False, "El código de cliente ya existe"
        cliente = Cliente(codigo, nombre_completo, zona)
        self.clientes.insertar_final(cliente)
        return True, f"Cliente {nombre_completo} registrado exitosamente"

    def consultar_cliente(self, codigo):
        return self.clientes.buscar(lambda c: c.codigo == codigo)

    def listar_clientes(self):
        return self.clientes.listar_todos()

    def registrar_restaurante(self, codigo, nombre, zona):
        existe = self.restaurantes_lista.buscar(lambda r: r.codigo == codigo)
        if existe:
            return False, "El código de restaurante ya existe"
        restaurante = Restaurante(codigo, nombre, zona)
        self.restaurantes_lista.insertar_final(restaurante)
        self.restaurantes_arbol.insertar(restaurante, lambda r: r.codigo)
        return True, f"Restaurante {nombre} registrado exitosamente"

    def consultar_restaurante(self, codigo):
        return self.restaurantes_arbol.buscar(codigo, lambda r: r.codigo)

    def listar_restaurantes(self):
        return self.restaurantes_lista.listar_todos()

    def buscar_restaurante_mas_cercano(self, zona_cliente):
        restaurantes = self.listar_restaurantes()
        if not restaurantes:
            return None
        
        if self.mapa_ciudad.esta_vacio():
            return restaurantes[0] if restaurantes else None
        
        restaurante_mas_cercano = None
        distancia_minima = float('inf')
        for restaurante in restaurantes:
            distancia = self.mapa_ciudad.obtener_distancia(zona_cliente, restaurante.zona)
            if distancia < distancia_minima:
                distancia_minima = distancia
                restaurante_mas_cercano = restaurante
        
        if restaurante_mas_cercano is None and len(restaurantes) > 0:
            return restaurantes[0]
        
        return restaurante_mas_cercano

    def registrar_domiciliario(self, codigo, nombre, zona_actual):
        existe = self.domiciliarios.buscar(lambda d: d.codigo == codigo)
        if existe:
            return False, "El código de domiciliario ya existe"
        domiciliario = Domiciliario(codigo, nombre, zona_actual)
        self.domiciliarios.insertar_final(domiciliario)
        return True, f"Domiciliario {nombre} registrado exitosamente"

    def listar_domiciliarios(self):
        return self.domiciliarios.listar_todos()

    def buscar_domiciliario_disponible_mas_cercano(self, zona_restaurante):
        domiciliarios = self.listar_domiciliarios()
        domiciliario_mas_cercano = None
        distancia_minima = float('inf')
        
        for domiciliario in domiciliarios:
            if domiciliario.disponible:
                if self.mapa_ciudad.esta_vacio():
                    return domiciliario
                
                distancia = self.mapa_ciudad.obtener_distancia(zona_restaurante, domiciliario.zona_actual)
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    domiciliario_mas_cercano = domiciliario
        
        if domiciliario_mas_cercano is None and len(domiciliarios) > 0:
            for domiciliario in domiciliarios:
                if domiciliario.disponible:
                    return domiciliario
        
        return domiciliario_mas_cercano

    def crear_pedido(self, codigo_cliente, codigo_restaurante, items):
        cliente = self.consultar_cliente(codigo_cliente)
        if not cliente:
            return False, "Cliente no encontrado"
        restaurante = self.consultar_restaurante(codigo_restaurante)
        if not restaurante:
            return False, "Restaurante no encontrado"
        pedido = Pedido(cliente, restaurante, items)
        self.pedidos_pendientes.enqueue(pedido)
        return True, f"Pedido #{pedido.codigo} creado y en cola de espera"

    def asignar_pedido(self):
        if self.pedidos_pendientes.esta_vacia():
            return False, "No hay pedidos pendientes"
        
        pedido = self.pedidos_pendientes.dequeue()
        domiciliario = self.buscar_domiciliario_disponible_mas_cercano(pedido.restaurante.zona)
        
        if not domiciliario:
            self.pedidos_pendientes.enqueue(pedido)
            domiciliarios_totales = len(self.listar_domiciliarios())
            if domiciliarios_totales == 0:
                return False, "No hay domiciliarios registrados en el sistema"
            else:
                return False, f"No hay domiciliarios disponibles ({domiciliarios_totales} ocupados)"
        
        pedido.asignar_domiciliario(domiciliario)
        domiciliario.asignar_pedido(pedido)
        self.pedidos_en_camino.enqueue(pedido)
        return True, f"Pedido #{pedido.codigo} asignado a {domiciliario.nombre}"

    def entregar_pedido(self, codigo_pedido):
        pedidos_temp = []
        pedido_encontrado = None
        while not self.pedidos_en_camino.esta_vacia():
            pedido = self.pedidos_en_camino.dequeue()
            if pedido.codigo == codigo_pedido:
                pedido_encontrado = pedido
            else:
                pedidos_temp.append(pedido)
        for p in pedidos_temp:
            self.pedidos_en_camino.enqueue(p)
        if not pedido_encontrado:
            return False, "Pedido no encontrado en pedidos en camino"
        pedido_encontrado.marcar_entregado()
        if pedido_encontrado.domiciliario:
            pedido_encontrado.domiciliario.liberar()
            pedido_encontrado.domiciliario.zona_actual = pedido_encontrado.cliente.zona
        self.historial_entregados.push(pedido_encontrado)
        return True, f"Pedido #{codigo_pedido} entregado exitosamente"

    def cancelar_pedido(self, codigo_pedido):
        pedidos_temp = []
        pedido_encontrado = None
        while not self.pedidos_pendientes.esta_vacia():
            pedido = self.pedidos_pendientes.dequeue()
            if pedido.codigo == codigo_pedido:
                pedido_encontrado = pedido
            else:
                pedidos_temp.append(pedido)
        for p in pedidos_temp:
            self.pedidos_pendientes.enqueue(p)
        if not pedido_encontrado:
            pedidos_temp = []
            while not self.pedidos_en_camino.esta_vacia():
                pedido = self.pedidos_en_camino.dequeue()
                if pedido.codigo == codigo_pedido:
                    pedido_encontrado = pedido
                else:
                    pedidos_temp.append(pedido)
            for p in pedidos_temp:
                self.pedidos_en_camino.enqueue(p)
        if not pedido_encontrado:
            return False, "Pedido no encontrado"
        pedido_encontrado.cancelar()
        if pedido_encontrado.domiciliario:
            pedido_encontrado.domiciliario.liberar()
        self.historial_cancelados.push(pedido_encontrado)
        return True, f"Pedido #{codigo_pedido} cancelado"

    def listar_pedidos_activos(self):
        pedidos = []
        pedidos.extend(self.pedidos_pendientes.listar_todos())
        pedidos.extend(self.pedidos_en_camino.listar_todos())
        return pedidos

    def listar_pedidos_entregados(self):
        return self.historial_entregados.listar_todos()

    def listar_pedidos_cancelados(self):
        return self.historial_cancelados.listar_todos()

    def historial_cliente(self, codigo_cliente):
        historial = []
        for pedido in self.historial_entregados.listar_todos():
            if pedido.cliente.codigo == codigo_cliente:
                historial.append(pedido)
        for pedido in self.historial_cancelados.listar_todos():
            if pedido.cliente.codigo == codigo_cliente:
                historial.append(pedido)
        return historial

    def agregar_zona(self, nombre_zona):
        if self.mapa_ciudad.agregar_vertice(nombre_zona):
            return True, f"Zona '{nombre_zona}' agregada al mapa"
        return False, f"La zona '{nombre_zona}' ya existe"

    def agregar_conexion_zonas(self, zona1, zona2, distancia):
        if self.mapa_ciudad.agregar_arista(zona1, zona2, distancia):
            return True, f"Conexión agregada: {zona1} <-> {zona2} ({distancia} km)"
        return False, "No se pudo agregar la conexión (verificar que ambas zonas existan)"

    def listar_zonas(self):
        return self.mapa_ciudad.listar_vertices()

    def mostrar_mapa_completo(self):
        self.mapa_ciudad.mostrar_grafo()
    
    def obtener_zonas_adyacentes(self, zona):
        return self.mapa_ciudad.obtener_adyacentes(zona)
    
    def recorrido_zonas_bfs(self, zona_inicio):
        return self.mapa_ciudad.bfs(zona_inicio)
    
    def calcular_ruta_optima(self, zona_origen, zona_destino):
        resultado = self.mapa_ciudad.dijkstra(zona_origen, zona_destino)
        if resultado is None:
            return None, "Zona de origen no existe"
        if resultado is None or resultado['distancia_total'] == float('inf'):
            return None, f"No existe ruta entre {zona_origen} y {zona_destino}"
        return resultado, "Ruta calculada exitosamente"
    
    def calcular_todas_rutas(self, zona_origen):
        return self.mapa_ciudad.dijkstra(zona_origen)