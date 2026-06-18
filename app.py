from dao.libro_dao import LibroDAO

def main():
    try:
        libro_dao = LibroDAO()
        libros = libro_dao.obtener_todo()

        if len(libros) == 0:
            print("No hay libros registrados")
        else:
            for libro in libros:
                print(f"id: {libro.id} {libro.titulo} {libro.autor} {libro.isbn} {libro.disponible}" )
        print("\n Conexion exitosa con la base de datos")

    except Exception as e:
        print("Error")
        print(e)

if  __name__ == "__main__":
    main()