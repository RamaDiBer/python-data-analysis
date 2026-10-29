from datos import catalogo
from tabulate import tabulate
from functools import reduce

clientes = []
class Cliente:
    def __init__(self, nombre, localidad):
        self.nombre = nombre
        self.localidad = localidad
        self.pedidos_realizados = []
    def agregar_pedido(self, pedido):
        self.pedidos_realizados.append(pedido)
def listar_productos():
    tabla = []
    for producto in catalogo:
        tabla.append([
            producto["id"],
            producto["nombre"],
            producto["material"],
            producto["precio_base"],
            producto["stock"]
        ])

    headers = ["ID", "Nombre", "Material", "Precio", "Stock"]
    print(tabulate(tabla, headers=headers, tablefmt="github"))

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Listar inventario")
    print("2. Registrar pedido")
    print("3. Analizar métricas")
    print("4. Salir")

def registrar_pedido():
    try:
        nombre = input("Nombre del cliente: ").strip().lower()
        localidad = input("Localidad: ").strip().lower()
        id_producto = int(input("Ingresá el ID del producto: "))
        cantidad = int(input("Ingresá la cantidad: "))
        producto_encontrado = None

        for producto in catalogo:
            if producto["id"] == id_producto:
                producto_encontrado = producto
                break
        if producto_encontrado is None:
            print("❌ Producto no encontrado")
            return
        if cantidad > producto_encontrado["stock"]:
            print("❌ No hay suficiente stock")
            return

        cliente_existente = None

        for cliente in clientes:
            if cliente.nombre == nombre:
                cliente_existente = cliente
                break

        if cliente_existente is None:
            cliente_existente = Cliente(nombre, localidad)
            clientes.append(cliente_existente)

        pedido = {
            "producto": producto_encontrado["nombre"],
            "cantidad": cantidad,
            "total": cantidad * producto_encontrado["precio_base"]
        }
        if cantidad <= 0:
            print("❌ La cantidad debe ser mayor a 0")
            return

        cliente_existente.agregar_pedido(pedido)

        producto_encontrado["stock"] -= cantidad

        print(f"✅ Pedido de {pedido['producto']} registrado para {nombre}. Total: ${pedido['total']:.2f}")

    except ValueError:
        print("❌ Error: ingresá valores numéricos válidos")

def mostrar_localidades_unicas():
    localidades = set()

    for cliente in clientes:
        localidades.add(cliente.localidad)
    print("\n Localidades únicas:")
    for loc in localidades:
        print("-", loc)

def main():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            listar_productos()
        elif opcion == "2":
            registrar_pedido()

        elif opcion == "3":
            print("1. Filtrar por material")
            print("2. Aplicar descuento")
            print("3. Valor total inventario")
            print("4. Ver localidades únicas")
            print("5. Volver al menú principal")
            subopcion = input("Elegí una opción: ")
            if subopcion == "1":
                filtrar_por_material()
            elif subopcion == "2":
                aplicar_descuento()
            elif subopcion == "3":
                valor_total_inventario()
            elif subopcion == "4":
                mostrar_localidades_unicas()
            else:
                print("Opción inválida")
                print("\n--- ANALÍTICA ---")
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intentá de nuevo")

def filtrar_por_material():
    material = input("Ingresá tipo (Repuesto / Servicio): ").strip().capitalize()

    filtrados = list(filter(lambda p: p["material"] == material, catalogo))

    if filtrados:
        tabla = []
        for p in filtrados:
            tabla.append([
                p["id"],
                p["nombre"],
                p["material"],
                p["precio_base"],
                p["stock"]
            ])

        headers = ["ID", "Nombre", "Material", "Precio", "Stock"]
        print(tabulate(tabla, headers=headers, tablefmt="github"))
    else:
        print("No se encontraron productos")

def aplicar_descuento():
    try:
        porcentaje = float(input("Ingresá porcentaje: "))
        tabla = []
        nuevos = list(map(lambda p: (
            p["nombre"],
            p["precio_base"],
            p["precio_base"] * (1 - porcentaje / 100)
        ),
            catalogo
        ))
        for nombre, original, nuevo in nuevos:
            tabla.append([nombre, original, nuevo])

        headers = ["Producto", "Precio Original", "Precio con Descuento"]
        print(tabulate(tabla, headers=headers, tablefmt="github"))

    except ValueError:
        print("Error: ingresá un número válido")

def valor_total_inventario():
    total = reduce(
        lambda acc, p: acc + (p["precio_base"] * p["stock"]),
        catalogo,
        0
    )
    print(f" Valor total del inventario: ${total:.2f}")
5
if __name__ == "__main__":
    main()