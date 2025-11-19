from datetime import datetime

class Cliente:
    def __init__(self, codigo, nombre_completo, zona):
        self.codigo = codigo
        self.nombre_completo = nombre_completo
        self.zona = zona
        self.pedido_actual = None

    def __str__(self):
        return f"[{self.codigo}] {self.nombre_completo} - Zona: {self.zona}"


class Menu:
    def __init__(self):
        self.entradas = []
        self.platos_fuertes = []
        self.postres = []
        self.bebidas = []

    def agregar_entrada(self, nombre, precio):
        self.entradas.append({'nombre': nombre, 'precio': precio})

    def agregar_plato_fuerte(self, nombre, precio):
        self.platos_fuertes.append({'nombre': nombre, 'precio': precio})

    def agregar_postre(self, nombre, precio):
        self.postres.append({'nombre': nombre, 'precio': precio})

    def agregar_bebida(self, nombre, precio):
        self.bebidas.append({'nombre': nombre, 'precio': precio})

    def mostrar(self):
        print("\n--- MENÚ ---")
        print("\nEntradas:")
        for item in self.entradas:
            print(f"  - {item['nombre']}: ${item['precio']}")
        print("\nPlatos Fuertes:")
        for item in self.platos_fuertes:
            print(f"  - {item['nombre']}: ${item['precio']}")
        print("\nPostres:")
        for item in self.postres:
            print(f"  - {item['nombre']}: ${item['precio']}")
        print("\nBebidas:")
        for item in self.bebidas:
            print(f"  - {item['nombre']}: ${item['precio']}")


class Restaurante:
    def __init__(self, codigo, nombre, zona):
        self.codigo = codigo
        self.nombre = nombre
        self.zona = zona
        self.menu = Menu()

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - Zona: {self.zona}"


class Domiciliario:
    def __init__(self, codigo, nombre, zona_actual):
        self.codigo = codigo
        self.nombre = nombre
        self.zona_actual = zona_actual
        self.disponible = True
        self.pedido_asignado = None

    def asignar_pedido(self, pedido):
        self.disponible = False
        self.pedido_asignado = pedido

    def liberar(self):
        self.disponible = True
        self.pedido_asignado = None

    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupado"
        return f"[{self.codigo}] {self.nombre} - Zona: {self.zona_actual} ({estado})"


class Pedido:
    contador_pedidos = 1000

    def __init__(self, cliente, restaurante, items):
        self.codigo = Pedido.contador_pedidos
        Pedido.contador_pedidos += 1
        self.cliente = cliente
        self.restaurante = restaurante
        self.items = items
        self.domiciliario = None
        self.estado = "PENDIENTE"
        self.fecha_hora = datetime.now()
        self.total = sum(item['precio'] for item in items)

    def asignar_domiciliario(self, domiciliario):
        self.domiciliario = domiciliario
        self.estado = "EN_CAMINO"

    def marcar_entregado(self):
        self.estado = "ENTREGADO"

    def cancelar(self):
        self.estado = "CANCELADO"

    def __str__(self):
        domiciliario_info = f"{self.domiciliario.nombre}" if self.domiciliario else "Sin asignar"
        items_str = ", ".join([item['nombre'] for item in self.items])
        return (f"Pedido #{self.codigo} | Cliente: {self.cliente.nombre_completo} | "
                f"Restaurante: {self.restaurante.nombre} | "
                f"Items: {items_str} | Total: ${self.total} | "
                f"Domiciliario: {domiciliario_info} | Estado: {self.estado}")
