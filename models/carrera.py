class Carrera:

    # Construcctor
    def __init__(self, id_carrera, nombre_carrera):
        self.id_carrera = id_carrera
        self.nombre_carrera = nombre_carrera

    def mostrar_info(self):
        return f"ID carrera: {self.id_carrera}, Nombre: {self.nombre_carrera}"