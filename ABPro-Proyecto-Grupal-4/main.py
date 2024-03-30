import datetime

#Crear clases:
class Cliente():
# idcliente, nombre, apellido, correo, fecha registro, __saldo (encapsulado)
    def __init__(self, idcliente, nombre, apellido, correo, fecha_registro, saldo, convenio="Sin convenio"):
        self.idcliente = idcliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.convenio = convenio
        self.__saldo = saldo

    def infoClientes(self):
        return f"ID: {self.idcliente}\nNombre: {self.nombre}\nApellido: {self.apellido}\nCorreo: {self.correo}\nFecha de registro: {self.fecha_registro}\nSaldo: {self.__saldo}\nConvenio: {self.convenio}"

    def obtener_saldo(self):
        return self.__saldo

    def depositar_saldo(self, monto):
        self.__saldo += monto
        return self.__saldo

    def cambiar_producto(self, producto_entrante, producto_saliente):
        diferencia = producto_saliente.valor_neto - producto_entrante.valor_neto
        if self.obtener_saldo() < diferencia:
            return "Saldo insuficiente"
        else:
            self.depositar_saldo(-diferencia)
            producto_entrante.stock += 1
            producto_saliente.stock -= 1
            return "Producto cambiado con éxito"

    def devolver(self, producto_devuelto, buen_estado=True):
        if buen_estado:
            producto_devuelto.stock += 1
            self.depositar_saldo(producto_devuelto.valor_neto)
            return "Devolución exitosa"
        else:
            return "No se puede devolver un artículo en mal estado"

class Producto():
# sku, nombre, categoria, proveedor, stock, valor_neto, __impuesto = 1.19 (encapsulado)
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, impuesto=1.19, descuento=0):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.descuento = descuento
        self.__impuesto = impuesto

    def infoProducto(self):
        return f"SKU: {self.sku}\nNombre: {self.nombre}\nCategoría: {self.categoria}\nProveedor: {self.proveedor}\nStock: {self.stock}\nValor neto: {self.valor_neto}\nImpuesto: {self.__impuesto}\nDescuento: {self.descuento}"

class Vendedor():
# run, nombre, apellido, seccion, __comision = 0
    def __init__(self, run, nombre, apellido, seccion, comision=0, turno_noche=False):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = comision
        self.turno_noche = turno_noche

    def vender(self, producto, cliente):
        # Calcular si cliente tiene saldo
        if not cliente.obtener_saldo() >= producto.valor_neto:
            return "Saldo insuficiente"
        # Ver si hay existencias del producto
        if producto.stock <= 0:
            return "No hay existencias"
        producto.stock -= 1
        comision = producto.valor_neto * 0.005
        self.__comision += comision
        cliente.depositar_saldo(-producto.valor_neto)
        return "Venta exitosa"

    def canje_comision(self, vendedor, producto):
        if not isinstance(vendedor, Vendedor):
            return "No es un vendedor"
        # Al comprar con comisión se rebaja a un 40%
        valor_producto = producto.valor_neto * 0.6
        if vendedor.__comision >= valor_producto:
            vendedor.__comision -= valor_producto
            self.__comision -= valor_producto
            producto.stock -= 1
            return "Canje exitoso"
        else:
            return "No se puede canjear"

class Proveedor():
# rut, nombre legal, razon social, pais, tipo_persona
    def __init__(self, rut, nombre_legal, razon_social, pais, tipo_persona):
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.tipo_persona = tipo_persona

    def proveer(self, producto, stock_a_proveer):
        if producto.proveedor != self:
            return "Producto no proveido por este proveedor"
        producto.stock += stock_a_proveer
        return "Stock exitosamente agregado"

class OrdenCompra():
    def __init__(self, id_ordencompra, producto, despacho):
        self.id_ordencompra = id_ordencompra
        self.producto = producto
        self.despacho = despacho

    def calcular_total(self):
        if self.despacho:
            total = self.producto.valor_neto + 5000  # Recargo de despacho
        else:
            total = self.producto.valor_neto
        return total
    
# Lógica para reponer productos en la bodega
class Bodega():
    @staticmethod
    def reponer_stock(sucursal):
        for producto in sucursal.productos:
            if producto.stock < 50:
                print(f"Reponiendo productos en {sucursal.nombre}...")
                if Bodega.descontar_stock(producto):
                    sucursal.aumentar_stock(producto, 300)
                    print("Productos repuestos en la sucursal.")
                else:
                    print("No hay suficiente stock en la bodega para reponer.")
            else:
                print("Stock suficiente en la sucursal.")

    @staticmethod
    def descontar_stock(producto):
        if producto.stock >= 300:
            producto.stock -= 300
            return True
        else:
            return False
        
#clases adicionales para Sucursal y ProductoSucursal
class Sucursal():
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def aumentar_stock(self, producto, cantidad):
        producto.stock += cantidad

class ProductoSucursal():
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
    
# VARIABLES GLOBALES
bodega = Bodega()
clientes = []
vendedores = []
proveedores = []
sucursal = Sucursal("Sucursal Principal")

# OPCIONES MENU
menu_base = ["Clientes", "Bodega", "Vendedores", "Proveedores", "Venta"]
menu_clientes = ["Listar", "Crear", "Editar", "Eliminar", "Salir"]
menu_bodega = ["Listar", "Crear", "Editar", "Eliminar", "Producto con más stock", "Buscar", "Salir"]
menu_vendedores = ["Listar", "Crear", "Editar", "Eliminar", "Salir"]
menu_proveedores = ["Listar", "Crear", "Editar", "Eliminar", "Salir"]
menu_ventas = ["Listar", "Realizar", "Salir"]

# Inicio app
print("Bienvenido a Te lo Vendo\n¿Qué desea hacer?")
# Mostrar menu base
while True:
    opcion = input("Seleccione una opción: ")
    for i, opcion in enumerate(menu_base):
        print(f"{i+1}. {opcion}")
    opcion_seleccionada = int(input("Ingrese una opción: "))

    # Opciones del menu base
    while opcion_seleccionada != 0:
        if opcion_seleccionada == 1:
            print("¿Qué desea hacer?")
            for i, opcion in enumerate(menu_clientes):
                print(f"{i+1}. {opcion}")
            opcion_seleccionada_menu = int(input("Ingrese una opción: "))
            
            # Opciones del menu clientes
            while opcion_seleccionada_menu != 0:
                if opcion_seleccionada_menu == 1:
                    if len(clientes) == 0:
                        print("No hay clientes registrados")
                        break
                    for cliente in clientes:
                        print(cliente.infoClientes())
                    opcion_seleccionada_menu = 0
                elif opcion_seleccionada_menu == 2:
                    idcliente = input("Ingrese el ID del cliente: ")
                    nombre = input("Ingrese el nombre del cliente: ")
                    apellido = input("Ingrese el apellido del cliente: ")
                    correo = input("Ingrese el correo del cliente: ")
                    fecha_registro = datetime.now()
                    saldo = int(input("Ingrese el saldo del cliente: "))
                    convenio = input("Ingrese el convenio del cliente: ")
                    cliente = Cliente(idcliente, nombre, apellido, correo, fecha_registro, saldo, convenio)
                    clientes.append(cliente)
                    print("Cliente agregado exitosamente")
                    opcion_seleccionada_menu = 0
                elif opcion_seleccionada_menu == 3:
                    # Opción para editar cliente
                    pass
                elif opcion_seleccionada_menu == 4:
                    # Opción para eliminar cliente
                    pass
                elif opcion_seleccionada_menu == 5:
                    break  # Salir al menu base
                else:
                    print("Opción no válida")
                    break