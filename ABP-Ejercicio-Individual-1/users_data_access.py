import random
import re

class Usuario:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

class Funcionario(Usuario):
    def __init__(self, nombre, telefono, cargo):
        super().__init__(nombre, telefono)
        self.cargo = cargo

    @staticmethod
    def acceso_datos_sensibles(func):
        def wrapper(self, *args, **kwargs):
            if self.cargo == "Administrativo":
                return func(self, *args, **kwargs)
            else:
                return "Acceso denegado. Función solo disponible para funcionarios administrativos."
        return wrapper

    def registrar_nuevo_usuario(self):
        # Lógica para registrar un nuevo usuario
        pass

    def enviar_solicitud_informacion_adicional(self):
        # Lógica para enviar una solicitud de información adicional
        pass

class Paciente(Usuario):
    def __init__(self, nombre, telefono, edad):
        super().__init__(nombre, telefono)
        self.edad = edad

    def acceso_datos_sensibles(self):
        return "Acceso denegado. Los pacientes no tienen acceso a datos sensibles."

    def registrar_nueva_cita(self):
        # Lógica para registrar una nueva cita
        pass

    def solicitar_receta_medica(self):
        # Lógica para solicitar una receta médica
        pass

class OrganizacionSocial(Usuario):
    def __init__(self, nombre, telefono, tipo):
        super().__init__(nombre, telefono)
        self.tipo = tipo

    @staticmethod
    def acceso_datos_sensibles(func):
        def wrapper(self, *args, **kwargs):
            if self.tipo == "ONG":
                return func(self, *args, **kwargs)
            else:
                return "Acceso denegado. Función solo disponible para organizaciones de tipo ONG."
        return wrapper

    def enviar_solicitud_ayuda(self):
        # Lógica para enviar una solicitud de ayuda
        pass

    def registrar_voluntario(self):
        # Lógica para registrar un nuevo voluntario
        pass

class ManejadorUsuarios:
    def __init__(self):
        self.usuarios = {}

    def agregar_usuario(self, usuario):
        self.usuarios[usuario.nombre] = usuario

    def mostrar_usuarios(self):
        for usuario in self.usuarios.values():
            print(f"Nombre: {usuario.nombre}, Teléfono: {usuario.telefono}")

    def buscar_usuario(self, nombre):
        return self.usuarios.get(nombre)

    def listar_usuarios(self):
        return list(self.usuarios.values())

def generar_contraseña():
    """Genera una contraseña aleatoria."""
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    return ''.join(random.choice(caracteres) for _ in range(12))  # Aumenta la longitud de la contraseña

def validar_contraseña(contraseña):
    """Valida si una contraseña cumple con los criterios de tener al menos una letra minúscula, una letra mayúscula, un número y un carácter especial."""
    regex_minuscula = re.compile('[a-z]')
    regex_mayuscula = re.compile('[A-Z]')
    regex_numero = re.compile('[0-9]')
    regex_especial = re.compile('[!@#$%^&*()]')
    return bool(regex_minuscula.search(contraseña) and regex_mayuscula.search(contraseña) and regex_numero.search(contraseña) and regex_especial.search(contraseña))

def validar_telefono(telefono):
    """Valida si un número de teléfono tiene exactamente 8 dígitos."""
    return telefono.isdigit() and len(telefono) == 8

def obtener_datos_usuario(usuario_tipo):
    """Obtiene los datos del usuario (nombre de usuario y teléfono) de manera interactiva."""
    nombre_usuario = input(f"Ingrese el nombre de usuario para {usuario_tipo}: ")
    telefono = input(f"Ingrese el número telefónico para {nombre_usuario}: ")
    while not validar_telefono(telefono):
        print("Número telefónico inválido. Debe contener exactamente 8 dígitos numéricos.")
        telefono = input("Ingrese el número telefónico válido: ")
    return nombre_usuario, telefono

def crear_cuentas(usuarios, manejador_usuarios):
    """Crea cuentas de usuario para los tipos de usuario proporcionados."""
    for usuario_tipo, cantidad in usuarios.items():
        for _ in range(cantidad):
            nombre_usuario, telefono = obtener_datos_usuario(usuario_tipo)
            contraseña = generar_contraseña()
            while not validar_contraseña(contraseña):
                contraseña = generar_contraseña()
            if usuario_tipo == "Funcionario":
                cargo = input("Ingrese el cargo del funcionario: ")
                funcionario = Funcionario(nombre_usuario, telefono, cargo)
                manejador_usuarios.agregar_usuario(funcionario)
            elif usuario_tipo == "Paciente":
                edad = int(input("Ingrese la edad del paciente: "))
                paciente = Paciente(nombre_usuario, telefono, edad)
                manejador_usuarios.agregar_usuario(paciente)
            elif usuario_tipo == "Organización social":
                tipo = input("Ingrese el tipo de organización social: ")
                organizacion_social = OrganizacionSocial(nombre_usuario, telefono, tipo)
                manejador_usuarios.agregar_usuario(organizacion_social)

def mostrar_cuentas(manejador_usuarios):
    """Muestra las cuentas de usuario creadas."""
    print("Cuentas creadas exitosamente:")
    manejador_usuarios.mostrar_usuarios()

def main():
    # Definir los tipos de usuarios y la cantidad deseada para cada uno
    usuarios = {
        "Funcionario": 2,
        "Paciente": 2,
        "Organización social": 2
    }

    manejador_usuarios = ManejadorUsuarios()

    # Crear las cuentas de usuario
    crear_cuentas(usuarios, manejador_usuarios)

    # Mostrar las cuentas creadas
    mostrar_cuentas(manejador_usuarios)

if __name__ == "__main__":
    main()
