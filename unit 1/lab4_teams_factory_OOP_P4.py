class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_impuesto(self):
        return 1.00

    def precio_final(self):
        return self.precio * self.obtener_impuesto()


class ProductoElectronico(Producto):
    def obtener_impuesto(self):
        return 1.16


class ProductoRopa(Producto):
    def obtener_impuesto(self):
        return 1.08


class ProductoAlimento(Producto):
    def obtener_impuesto(self):
        return 1.00


class ProductoFactory:
    @staticmethod
    def crear_producto(tipo, nombre, precio):
        if tipo == "electronico":
            return ProductoElectronico(nombre, precio)
        elif tipo == "ropa":
            return ProductoRopa(nombre, precio)
        elif tipo == "alimento":
            return ProductoAlimento(nombre, precio)
        else:
            raise ValueError(f"Tipo de producto no válido: {tipo}")


class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.productos = []
        self.estado = "CREADO"

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0

        for producto in self.productos:
            total += producto.precio_final()

        return total

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_pedido(self):
        print(f"\nPedido #{self.numero}")
        print(f"Cliente: {self.cliente}")
        print(f"Estado: {self.estado}")

        print("\nProductos:")

        for producto in self.productos:
            print(
                f"- {producto.nombre}: "
                f"${producto.precio:.2f}"
            )

        print(f"\nTotal: ${self.calcular_total():.2f}")


# main program

pedido = Pedido(1001, "Ana")

pedido.agregar_producto(
    ProductoFactory.crear_producto("electronico", "Laptop", 15000)
)

pedido.agregar_producto(
    ProductoFactory.crear_producto("ropa", "Playera", 500)
)

pedido.agregar_producto(
    ProductoFactory.crear_producto("alimento", "Cereal", 100)
)

pedido.mostrar_pedido()

pedido.cambiar_estado("ENVIADO")

print("\nNuevo estado:", pedido.estado)