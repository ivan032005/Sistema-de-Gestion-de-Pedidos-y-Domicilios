from sistema import SistemaGestionPedidos

def limpiar_pantalla():
    print("\n" * 1)

def pausa():
    input("\nPresione Enter para continuar...")

def mostrar_menu_principal():
    print("  SISTEMA DE GESTIÓN DE PEDIDOS A DOMICILIO MULTIZONA")
    print("\n1.  Gestión de Clientes")
    print("2.  Gestión de Restaurantes")
    print("3.  Gestión de Domiciliarios")
    print("4.  Gestión de Pedidos")
    print("5.  Gestión del Mapa de la Ciudad")
    print("6.  Reportes y Consultas")
    print("7.  Cargar Datos de Prueba")
    print("0.  Salir")

def menu_clientes(sistema):
    while True:
        limpiar_pantalla()
        print("\n--- GESTIÓN DE CLIENTES ---")
        print("1. Registrar cliente")
        print("2. Consultar cliente")
        print("3. Listar todos los clientes")
        print("0. Volver")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            print("\n--- REGISTRAR CLIENTE ---")
            codigo = input("Código del cliente: ")
            nombre = input("Nombre completo: ")
            zona = input("Zona de ubicación: ")
            exito, mensaje = sistema.registrar_cliente(codigo, nombre, zona)
            print(f"\n{'✓' if exito else '✗'} {mensaje}")
            pausa()
        
        elif opcion == "2":
            print("\n--- CONSULTAR CLIENTE ---")
            codigo = input("Código del cliente: ")
            cliente = sistema.consultar_cliente(codigo)
            if cliente:
                print(f"\n{cliente}")
            else:
                print("\n✗ Cliente no encontrado")
            pausa()
        
        elif opcion == "3":
            print("\n--- LISTA DE CLIENTES ---")
            clientes = sistema.listar_clientes()
            if clientes:
                for cliente in clientes:
                    print(cliente)
            else:
                print("No hay clientes registrados")
            pausa()
        
        elif opcion == "0":
            break

def menu_restaurantes(sistema):
    while True:
        limpiar_pantalla()
        print("\n--- GESTIÓN DE RESTAURANTES ---")
        print("1. Registrar restaurante")
        print("2. Consultar restaurante")
        print("3. Listar todos los restaurantes")
        print("4. Agregar items al menú")
        print("5. Ver menú de un restaurante")
        print("0. Volver")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            print("\n--- REGISTRAR RESTAURANTE ---")
            codigo = input("Código del restaurante: ")
            nombre = input("Nombre: ")
            zona = input("Zona de ubicación: ")
            exito, mensaje = sistema.registrar_restaurante(codigo, nombre, zona)
            print(f"\n{'✓' if exito else '✗'} {mensaje}")
            pausa()
        
        elif opcion == "2":
            print("\n--- CONSULTAR RESTAURANTE ---")
            codigo = input("Código del restaurante: ")
            restaurante = sistema.consultar_restaurante(codigo)
            if restaurante:
                print(f"\n{restaurante}")
            else:
                print("\n✗ Restaurante no encontrado")
            pausa()
        
        elif opcion == "3":
            print("\n--- LISTA DE RESTAURANTES ---")
            restaurantes = sistema.listar_restaurantes()
            if restaurantes:
                for rest in restaurantes:
                    print(rest)
            else:
                print("No hay restaurantes registrados")
            pausa()
        
        elif opcion == "4":
            print("\n--- AGREGAR ITEMS AL MENÚ ---")
            codigo = input("Código del restaurante: ")
            restaurante = sistema.consultar_restaurante(codigo)
            if not restaurante:
                print("\n✗ Restaurante no encontrado")
                pausa()
                continue
            
            print("\nTipo de item:")
            print("1. Entrada")
            print("2. Plato fuerte")
            print("3. Postre")
            print("4. Bebida")
            tipo = input("Seleccione: ")
            
            nombre_item = input("Nombre del item: ")
            precio = float(input("Precio: $"))
            
            if tipo == "1":
                restaurante.menu.agregar_entrada(nombre_item, precio)
            elif tipo == "2":
                restaurante.menu.agregar_plato_fuerte(nombre_item, precio)
            elif tipo == "3":
                restaurante.menu.agregar_postre(nombre_item, precio)
            elif tipo == "4":
                restaurante.menu.agregar_bebida(nombre_item, precio)
            
            print("\n✓ Item agregado al menú")
            pausa()
        
        elif opcion == "5":
            print("\n--- VER MENÚ ---")
            codigo = input("Código del restaurante: ")
            restaurante = sistema.consultar_restaurante(codigo)
            if restaurante:
                restaurante.menu.mostrar()
            else:
                print("\n✗ Restaurante no encontrado")
            pausa()
        
        elif opcion == "0":
            break

def menu_domiciliarios(sistema):
    while True:
        limpiar_pantalla()
        print("\n--- GESTIÓN DE DOMICILIARIOS ---")
        print("1. Registrar domiciliario")
        print("2. Listar todos los domiciliarios")
        print("3. Ver domiciliarios disponibles")
        print("4. Ver estado detallado")
        print("0. Volver")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            print("\n--- REGISTRAR DOMICILIARIO ---")
            codigo = input("Código del domiciliario: ")
            nombre = input("Nombre: ")
            zona = input("Zona actual: ")
            exito, mensaje = sistema.registrar_domiciliario(codigo, nombre, zona)
            print(f"\n{'✓' if exito else '✗'} {mensaje}")
            pausa()
        
        elif opcion == "2":
            print("\n--- LISTA DE DOMICILIARIOS ---")
            domiciliarios = sistema.listar_domiciliarios()
            if domiciliarios:
                for dom in domiciliarios:
                    print(dom)
                print(f"\nTotal: {len(domiciliarios)} domiciliarios")
            else:
                print("No hay domiciliarios registrados")
            pausa()
        
        elif opcion == "3":
            print("\n--- DOMICILIARIOS DISPONIBLES ---")
            domiciliarios = sistema.listar_domiciliarios()
            disponibles = [d for d in domiciliarios if d.disponible]
            if disponibles:
                for dom in disponibles:
                    print(dom)
                print(f"\nTotal disponibles: {len(disponibles)}/{len(domiciliarios)}")
            else:
                print(f"No hay domiciliarios disponibles (Total: {len(domiciliarios)})")
            pausa()
        
        elif opcion == "4":
            print("\n--- ESTADO DETALLADO DE DOMICILIARIOS ---")
            domiciliarios = sistema.listar_domiciliarios()
            if domiciliarios:
                disponibles = [d for d in domiciliarios if d.disponible]
                ocupados = [d for d in domiciliarios if not d.disponible]
                
                print(f"\nTotal de domiciliarios: {len(domiciliarios)}")
                print(f"Disponibles: {len(disponibles)}")
                print(f"Ocupados: {len(ocupados)}")
                
                if disponibles:
                    print("\n--- DISPONIBLES ---")
                    for dom in disponibles:
                        print(f"  {dom}")
                
                if ocupados:
                    print("\n--- OCUPADOS ---")
                    for dom in ocupados:
                        pedido_info = f" (Pedido #{dom.pedido_asignado.codigo})" if dom.pedido_asignado else ""
                        print(f"  {dom}{pedido_info}")
            else:
                print("No hay domiciliarios registrados")
            pausa()
        
        elif opcion == "0":
            break

def menu_pedidos(sistema):
    while True:
        limpiar_pantalla()
        print("\n--- GESTIÓN DE PEDIDOS ---")
        print("1. Crear nuevo pedido")
        print("2. Asignar pedido pendiente a domiciliario")
        print("3. Marcar pedido como entregado")
        print("4. Cancelar pedido")
        print("5. Ver pedidos activos")
        print("6. Ver pedidos pendientes")
        print("7. Ver pedidos en camino")
        print("0. Volver")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            print("\n--- CREAR NUEVO PEDIDO ---")
            codigo_cliente = input("Código del cliente: ")
            codigo_restaurante = input("Código del restaurante: ")
            
            cliente = sistema.consultar_cliente(codigo_cliente)
            restaurante = sistema.consultar_restaurante(codigo_restaurante)
            
            if not cliente:
                print("\n✗ Cliente no encontrado")
                pausa()
                continue
            
            if not restaurante:
                print("\n✗ Restaurante no encontrado")
                pausa()
                continue
            
            restaurante.menu.mostrar()
            
            items = []
            print("\n--- SELECCIONAR ITEMS ---")
            while True:
                nombre_item = input("\nNombre del item (o 'fin' para terminar): ")
                if nombre_item.lower() == 'fin':
                    break
                precio = float(input("Precio del item: $"))
                items.append({'nombre': nombre_item, 'precio': precio})
            
            if items:
                exito, mensaje = sistema.crear_pedido(codigo_cliente, codigo_restaurante, items)
                print(f"\n{'✓' if exito else '✗'} {mensaje}")
            else:
                print("\n✗ Debe seleccionar al menos un item")
            pausa()
        
        elif opcion == "2":
            print("\n--- ASIGNAR PEDIDO ---")
            exito, mensaje = sistema.asignar_pedido()
            print(f"\n{'✓' if exito else '✗'} {mensaje}")
            pausa()
        
        elif opcion == "3":
            print("\n--- ENTREGAR PEDIDO ---")
            codigo_input = input("Código del pedido: ")
            codigo_input = codigo_input.replace('#', '').strip()
            try:
                codigo = int(codigo_input)
                exito, mensaje = sistema.entregar_pedido(codigo)
                print(f"\n{'✓' if exito else '✗'} {mensaje}")
            except ValueError:
                print("\n✗ Código inválido. Debe ser un número")
            pausa()
        
        elif opcion == "4":
            print("\n--- CANCELAR PEDIDO ---")
            codigo_input = input("Código del pedido: ")
            codigo_input = codigo_input.replace('#', '').strip()
            try:
                codigo = int(codigo_input)
                exito, mensaje = sistema.cancelar_pedido(codigo)
                print(f"\n{'✓' if exito else '✗'} {mensaje}")
            except ValueError:
                print("\n✗ Código inválido. Debe ser un número")
            pausa()
        
        elif opcion == "5":
            print("\n--- PEDIDOS ACTIVOS ---")
            pedidos = sistema.listar_pedidos_activos()
            if pedidos:
                for pedido in pedidos:
                    print(pedido)
            else:
                print("No hay pedidos activos")
            pausa()
        
        elif opcion == "6":
            print("\n--- PEDIDOS PENDIENTES ---")
            pedidos = sistema.pedidos_pendientes.listar_todos()
            if pedidos:
                for pedido in pedidos:
                    print(pedido)
            else:
                print("No hay pedidos pendientes")
            pausa()
        
        elif opcion == "7":
            print("\n--- PEDIDOS EN CAMINO ---")
            pedidos = sistema.pedidos_en_camino.listar_todos()
            if pedidos:
                for pedido in pedidos:
                    print(pedido)
            else:
                print("No hay pedidos en camino")
            pausa()
        
        elif opcion == "0":
            break

def menu_mapa(sistema):
    while True:
        limpiar_pantalla()
        print("\n--- GESTIÓN DEL MAPA DE LA CIUDAD (GRAFO) ---")
        print("1. Agregar zona")
        print("2. Agregar conexión entre zonas")
        print("3. Listar zonas")
        print("4. Mostrar mapa completo")
        print("5. Ver zonas adyacentes")
        print("6. Recorrido BFS")
        print("7. Calcular ruta óptima (Dijkstra)")
        print("8. Ver todas las distancias desde una zona")
        print("0. Volver")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            print("\n--- AGREGAR ZONA ---")
            nombre = input("Nombre de la zona: ")
            exito, mensaje = sistema.agregar_zona(nombre)
            print(f"\n{'✓' if exito else '✗'} {mensaje}")
            pausa()
        
        elif opcion == "2":
            print("\n--- AGREGAR CONEXIÓN ---")
            zona1 = input("Zona origen: ")
            zona2 = input("Zona destino: ")
            distancia = float(input("Distancia (km): "))
            exito, mensaje = sistema.agregar_conexion_zonas(zona1, zona2, distancia)
            print(f"\n{'✓' if exito else '✗'} {mensaje}")
            pausa()
        
        elif opcion == "3":
            print("\n--- ZONAS DE LA CIUDAD ---")
            zonas = sistema.listar_zonas()
            if zonas:
                for zona in zonas:
                    print(f"  - {zona}")
            else:
                print("No hay zonas registradas")
            pausa()
        
        elif opcion == "4":
            print("\n--- MAPA COMPLETO ---")
            sistema.mostrar_mapa_completo()
            pausa()
        
        elif opcion == "5":
            print("\n--- ZONAS ADYACENTES ---")
            zona = input("Nombre de la zona: ")
            adyacentes = sistema.obtener_zonas_adyacentes(zona)
            if adyacentes:
                print(f"\nZonas conectadas a '{zona}':")
                for ady in adyacentes:
                    print(f"  → {ady['destino']} ({ady['peso']} km)")
            else:
                print(f"\nNo hay zonas adyacentes o la zona '{zona}' no existe")
            pausa()
        
        elif opcion == "6":
            print("\n--- RECORRIDO BFS ---")
            zona = input("Zona de inicio: ")
            recorrido = sistema.recorrido_zonas_bfs(zona)
            if recorrido:
                print(f"\nRecorrido desde '{zona}':")
                print(" → ".join(recorrido))
            else:
                print(f"\nLa zona '{zona}' no existe")
            pausa()
        
        elif opcion == "7":
            print("\n--- CALCULAR RUTA ÓPTIMA (DIJKSTRA) ---")
            origen = input("Zona de origen: ")
            destino = input("Zona de destino: ")
            resultado, mensaje = sistema.calcular_ruta_optima(origen, destino)
            
            if resultado:
                print(f"\n✓ {mensaje}")
                print(f"\nRuta más corta: {' → '.join(resultado['camino'])}")
                print(f"Distancia total: {resultado['distancia_total']} km")
            else:
                print(f"\n✗ {mensaje}")
            pausa()
        
        elif opcion == "8":
            print("\n--- DISTANCIAS DESDE UNA ZONA (DIJKSTRA) ---")
            origen = input("Zona de origen: ")
            resultado = sistema.calcular_todas_rutas(origen)
            
            if resultado:
                print(f"\n✓ Distancias mínimas desde '{origen}':")
                print("\n{:<15} {:<15}".format("Destino", "Distancia (km)"))
                print("-" * 30)
                for zona, distancia in resultado['distancias'].items():
                    if distancia == float('inf'):
                        print(f"{zona:<15} {'Sin ruta':<15}")
                    else:
                        print(f"{zona:<15} {distancia:<15.1f}")
            else:
                print(f"\n✗ La zona '{origen}' no existe")
            pausa()
        
        elif opcion == "0":
            break

def menu_reportes(sistema):
    while True:
        limpiar_pantalla()
        print("\n--- REPORTES Y CONSULTAS ---")
        print("1. Historial de pedidos entregados")
        print("2. Historial de pedidos cancelados")
        print("3. Historial de un cliente")
        print("4. Estadísticas generales")
        print("0. Volver")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            print("\n--- HISTORIAL DE PEDIDOS ENTREGADOS ---")
            pedidos = sistema.listar_pedidos_entregados()
            if pedidos:
                for pedido in pedidos:
                    print(pedido)
                print(f"\nTotal: {len(pedidos)} pedidos entregados")
            else:
                print("No hay pedidos entregados")
            pausa()
        
        elif opcion == "2":
            print("\n--- HISTORIAL DE PEDIDOS CANCELADOS ---")
            pedidos = sistema.listar_pedidos_cancelados()
            if pedidos:
                for pedido in pedidos:
                    print(pedido)
                print(f"\nTotal: {len(pedidos)} pedidos cancelados")
            else:
                print("No hay pedidos cancelados")
            pausa()
        
        elif opcion == "3":
            print("\n--- HISTORIAL DE CLIENTE ---")
            codigo = input("Código del cliente: ")
            historial = sistema.historial_cliente(codigo)
            if historial:
                for pedido in historial:
                    print(pedido)
                print(f"\nTotal: {len(historial)} pedidos")
            else:
                print("El cliente no tiene historial de pedidos")
            pausa()
        
        elif opcion == "4":
            print("\n--- ESTADÍSTICAS GENERALES ---")
            print(f"Clientes registrados: {len(sistema.listar_clientes())}")
            print(f"Restaurantes registrados: {len(sistema.listar_restaurantes())}")
            print(f"Domiciliarios registrados: {len(sistema.listar_domiciliarios())}")
            print(f"Pedidos pendientes: {sistema.pedidos_pendientes.tamano()}")
            print(f"Pedidos en camino: {sistema.pedidos_en_camino.tamano()}")
            print(f"Pedidos entregados: {sistema.historial_entregados.tamano()}")
            print(f"Pedidos cancelados: {sistema.historial_cancelados.tamano()}")
            print(f"Zonas en el mapa: {len(sistema.listar_zonas())}")
            pausa()
        
        elif opcion == "0":
            break

def cargar_datos_prueba(sistema):
    print("\n--- CARGANDO DATOS DE PRUEBA ---")
    
    print("Agregando zonas...")
    sistema.agregar_zona("Norte")
    sistema.agregar_zona("Sur")
    sistema.agregar_zona("Centro")
    sistema.agregar_zona("Este")
    sistema.agregar_zona("Oeste")
    
    print("Agregando conexiones entre zonas...")
    sistema.agregar_conexion_zonas("Norte", "Centro", 5.0)
    sistema.agregar_conexion_zonas("Sur", "Centro", 4.5)
    sistema.agregar_conexion_zonas("Este", "Centro", 6.0)
    sistema.agregar_conexion_zonas("Oeste", "Centro", 5.5)
    sistema.agregar_conexion_zonas("Norte", "Este", 8.0)
    sistema.agregar_conexion_zonas("Sur", "Oeste", 7.0)
    sistema.agregar_conexion_zonas("Norte", "Oeste", 9.0)
    
    print("Registrando clientes...")
    sistema.registrar_cliente("C001", "Juan Pérez", "Norte")
    sistema.registrar_cliente("C002", "María García", "Sur")
    sistema.registrar_cliente("C003", "Carlos López", "Centro")
    sistema.registrar_cliente("C004", "Ana Martínez", "Este")
    
    print("Registrando restaurantes...")
    sistema.registrar_restaurante("R001", "Pizza Italiana", "Centro")
    sistema.registrar_restaurante("R002", "Hamburguesas Gourmet", "Norte")
    sistema.registrar_restaurante("R003", "Sushi Express", "Sur")
    
    print("Agregando items a menús...")
    rest1 = sistema.consultar_restaurante("R001")
    rest1.menu.agregar_entrada("Bruschetta", 8000)
    rest1.menu.agregar_plato_fuerte("Pizza Margarita", 25000)
    rest1.menu.agregar_plato_fuerte("Pizza Pepperoni", 28000)
    rest1.menu.agregar_postre("Tiramisú", 12000)
    rest1.menu.agregar_bebida("Gaseosa", 5000)
    
    rest2 = sistema.consultar_restaurante("R002")
    rest2.menu.agregar_entrada("Alitas BBQ", 15000)
    rest2.menu.agregar_plato_fuerte("Hamburguesa Clásica", 22000)
    rest2.menu.agregar_plato_fuerte("Hamburguesa Doble", 30000)
    rest2.menu.agregar_postre("Helado", 8000)
    rest2.menu.agregar_bebida("Malteada", 10000)
    
    print("Registrando domiciliarios...")
    sistema.registrar_domiciliario("D001", "Pedro Ramírez", "Centro")
    sistema.registrar_domiciliario("D002", "Laura Fernández", "Norte")
    sistema.registrar_domiciliario("D003", "Miguel Ángel", "Sur")
    
    print("\n✓ Datos de prueba cargados exitosamente")
    print("\n--- Mapa de la ciudad generado ---")
    sistema.mostrar_mapa_completo()
    pausa()

def main():
    sistema = SistemaGestionPedidos()
    
    while True:
        limpiar_pantalla()
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            menu_clientes(sistema)
        elif opcion == "2":
            menu_restaurantes(sistema)
        elif opcion == "3":
            menu_domiciliarios(sistema)
        elif opcion == "4":
            menu_pedidos(sistema)
        elif opcion == "5":
            menu_mapa(sistema)
        elif opcion == "6":
            menu_reportes(sistema)
        elif opcion == "7":
            cargar_datos_prueba(sistema)
        elif opcion == "0":
            print("\n¡Gracias por usar el sistema!")
            print("Desarrollado para el curso de Estructuras de Datos 2025-II")
            print("\nEstructuras implementadas:")
            print("  Lista Enlazada Simple")
            print("  Árbol Binario de Búsqueda")
            print("  Cola (FIFO)")
            print("  Pila (LIFO)")
            print("  Grafo con Lista de Adyacencia")
            print("\nAlgoritmos de grafos:")
            print("  BFS (Breadth-First Search)")
            print("  Dijkstra (Camino más corto)")
            break
        else:
            print("\n✗ Opción inválida")
            pausa()

if __name__ == "__main__":
    main()