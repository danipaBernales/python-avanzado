import datetime

#Crear clases:
class Cliente():
# idcliente, nombre, apellido, correo, fecha registro, __saldo (encapsulado)
    def __init__(self, idcliente, nombre, apellido, correo, fecha_registro, saldo, direccion=None):
        self.idcliente = idcliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.__saldo = saldo
        self.direccion = direccion

def obtener_saldo(self):
    return self.__saldo

def depositar_saldo(self, monto):
    self.__saldo += monto
    return self.__saldo

class Proveedor():
    def __init__(self, rut, nombre_legal, razon_social, pais, tipo_persona):
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.tipo_persona = tipo_persona
    
class Producto():
# sku, nombre, categoria, proveedor, stock, valor_neto, __impuesto = 1.19 (encapsulado)
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, impuesto=1.19, descripcion=None):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto = impuesto
        self.descripcion = descripcion

class Vendedor():
# run, nombre, apellido, seccion, __comision = 0
    def __init__(self, run, nombre, apellido, seccion, comision=0):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = comision
        
    def vender(self, producto, cantidad, cliente):
        if producto.stock >= cantidad:
            # Descuenta del stock
            producto.stock -= cantidad
            # Calcula la comisión
            comision_venta = producto.valor_neto * 0.005 * cantidad
            self.__comision += comision_venta
            # Calcula el valor final del producto
            valor_final = producto.valor_neto * cantidad
            # Descuenta el valor final del saldo del cliente
            if cliente.obtener_saldo() >= valor_final:
                cliente.__saldo -= valor_final
                return f"Compra realizada. Comisión: {comision_venta}. Saldo restante: {cliente.obtener_saldo()}"
            else:
                return "Saldo insuficiente para realizar la compra"
        else:
            return "Stock insuficiente"

# crear 5 productos
producto1 = Producto(1, "Zapatillas", "Deportivas", "Adidas", 10, 15000)
producto2 = Producto(2, "Poleras", "Deportivas", "Nike", 5, 10000)
producto3 = Producto(3, "Zapatos", "Deportivos", "Adidas", 8, 20000)
producto4 = Producto(4, "Poleron", "Deportivos", "Nike", 3, 5000)
producto5 = Producto(5, "Chaquetas", "Deportivas", "Adidas", 7, 30000)

# crear 5 vendedores
vendedor1 = Vendedor(1, "Juan", "Perez", "Ventas")
vendedor2 = Vendedor(2, "Maria", "Gomez", "Ventas")
vendedor3 = Vendedor(3, "Pedro", "Rodriguez", "Ventas")
vendedor4 = Vendedor(4, "Ana", "Martinez", "Ventas")
vendedor5 = Vendedor(5, "Luis", "Gonzalez", "Ventas")

# crear 5 clientes
cliente1 = Cliente(1, "Juan", "Perez", "XXXXXXXXXXXXXX", datetime.now(), 5000)
cliente2 = Cliente(2, "Maria", "Gomez", "XXXXXXXXXXXXXX", datetime.now(), 10000)
cliente3 = Cliente(3, "Pedro", "Rodriguez", "XXXXXXXXXXXXXX", datetime.now(), 15000)
cliente4 = Cliente(4, "Ana", "Martinez", "XXXXXXXXXXXXXX", datetime.now(), 20000)
cliente5 = Cliente(5, "Luis", "Gonzalez", "XXXXXXXXXXXXXX", datetime.now(), 25000)

class Menu:
    def __init__(self):
        self.bodega = self.bodega_virtual()
        self.clientes = {}
        
    def bodega_virtual(self):
        return {
            1: {"nombre": "ZAPATILLAS", "cantidad": 20},
            2: {"nombre": "POLERAS", "cantidad": 10},
            3: {"nombre": "ZAPATOS", "cantidad": 15},
            4: {"nombre": "POLERÓN", "cantidad": 3},
            5: {"nombre": "CHAQUETA", "cantidad": 5},
            6: {"nombre": "GUANTES", "cantidad": 4}
        }
        
    def menu(self):
        print("1. Ver unidades totales disponibles 📈")
        print("2. Ver unidades disponibles de un producto en particular 🔍")
        print("3. Ver productos con más de un número de unidades en stock 📦")
        print("4. Ingresar usuario 🧑")
        print("5. Mostrar cantidad de usuarios registrados en la tienda 👪")
        print("6. Solicitar compra 🏪")
        print("7. Listar usuarios")
        print("8. Salir")
        opcion = int(input("Selecciona una opción 🙂: "))
        return opcion

    def iniciar(self):
        while True:
            opcion = self.menu()
            if opcion == 1:
                print("Unidades disponibles para cada producto: ", self.unidades_disponibles())
            elif opcion == 2:
                id_producto = int(input("Ingresa el ID del producto: "))
                self.ver_unidades_producto(id_producto)
            elif opcion == 3:
                cantidad = int(input("Ingresa el número de unidades solicitadas: "))
                self.productos_mas_unidades(cantidad)
            elif opcion == 4:
                nuevo_cliente_id = self.ingresar_usuario()
                print("Usuario registrado con ID: ", nuevo_cliente_id)
            elif opcion == 5:
                print("Total usuarios registrados: ", self.clientes_registrados())
            elif opcion == 6:
                self.solicitar_compra()
            elif opcion == 7:
                self.listar_usuarios()
            elif opcion == 8:
                break
            else:
                print("Opción inválida. Elige una opción disponible en el menú.")

    def almacenar_stock(self, id_producto, cantidad):
        if id_producto in self.bodega:
            self.bodega[id_producto]["cantidad"] += cantidad
        else:
            print("Producto no existe")

    def actualizar_stock(self, id_producto, cantidad):
        if id_producto in self.bodega:
            self.bodega[id_producto]["cantidad"] = cantidad
        else:
            print("Producto no existe")

    def unidades_disponibles(self):
        return {producto["nombre"]: producto["cantidad"] for producto in self.bodega.values()}
        
    def stock_disponible_producto(self, id_producto):
        if id_producto in self.bodega:
            return self.bodega[id_producto]["cantidad"]
        else: 
            return 0

    def producto_unidad_usuario(self, cantidad):
        return [producto["nombre"] for producto in self.bodega.values() if producto["cantidad"] > cantidad]
    def unidades_disponibles(self):
        return {producto["nombre"]: producto["cantidad"] for producto in self.bodega.values()}
        
    def ver_unidades_producto(self, id_producto):
        if id_producto in self.bodega:
            print("Unidades disponibles del producto", id_producto, ":", self.bodega[id_producto]["cantidad"])
        else:
            print("Producto no existe")

    def productos_mas_unidades(self, cantidad):
        productos_sobre_cantidad = [producto["nombre"] for producto in self.bodega.values() if producto["cantidad"] > cantidad]
        if productos_sobre_cantidad:
            print("Productos con más de", cantidad, "unidades:", productos_sobre_cantidad)
        else:
            print("No hay productos con más de ", cantidad, " unidades disponibles")

    def ingresar_usuario(self):
        nombre = input("Ingresa el nombre del cliente: ")
        apellido = input("Ingresa el apellido del cliente: ")
        correo = input("Ingresa el correo del cliente: ")
        fecha_registro = datetime.datetime.now().strftime("%d/%m/%Y")
        id_cliente = max(self.clientes.keys()) + 1 if self.clientes else 1
        nuevo_cliente = Cliente(id_cliente, nombre, apellido, correo, fecha_registro, 0)
        self.clientes[id_cliente] = nuevo_cliente
        return id_cliente

    def listar_usuarios(self):
        print("Lista de usuarios registrados:")
        for cliente in self.clientes.values():
            print(f"{cliente.idcliente} - {cliente.nombre} {cliente.apellido} - {cliente.correo} - {cliente.fecha_registro}")

    def clientes_registrados(self):
        return len(self.clientes)

    def solicitar_compra(self):
        id_cliente = int(input("Ingresa el ID del usuario: "))
        id_producto = int(input("Ingresa el ID del producto: "))
        cantidad = int(input("Ingresa la cantidad a comprar: "))
        cliente = self.clientes.get(id_cliente)
        if cliente:
            producto = self.bodega.get(id_producto)
            if producto:
                stock_disponible = producto["cantidad"]
                if stock_disponible >= cantidad:
                    producto["cantidad"] -= cantidad
                    print("Compra aprobada y en camino 🛻")
                else:
                    print("No hay suficiente stock, compra cancelada 😔")
            else:
                print("Producto no existe")
        else:
            print("Cliente no existe")

# Ejemplo de uso
menu = Menu()
menu.iniciar()