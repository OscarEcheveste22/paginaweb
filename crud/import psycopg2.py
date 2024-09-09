import psycopg2

# Crear la conexión a la base de datos PostgreSQL
def conectar():
    try:
        conn = psycopg2.connect(
            host="dpg-crd2tojv2p9s73dethng-a.oregon-postgres.render.com",  # Cambia si usas otro host
            database="basededatos1",  # Cambia por el nombre de tu base de datos
            user="oscar22",  # Cambia por tu usuario de PostgreSQL
            password="Xy6l3AAL7sBM7DqOna1tCB3fH8AxJ43e"  # Cambia por tu contraseña
        )
        return conn
    except Exception as e:
        print(f"Error conectando a la base de datos: {e}")
        return None

# Crear la tabla de usuarios
def crear_tabla(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                edad INT NOT NULL
            )
        ''')
        conn.commit()
        cursor.close()
        print("Tabla 'usuarios' creada.")
    except Exception as e:
        print(f"Error creando la tabla: {e}")

# Crear un nuevo usuario
def crear_usuario(conn, nombre, edad):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nombre, edad) 
            VALUES (%s, %s)
        ''', (nombre, edad))
        conn.commit()
        cursor.close()
        print(f'Usuario {nombre} creado.')
    except Exception as e:
        print(f"Error creando el usuario: {e}")

# Leer todos los usuarios
def leer_usuarios(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()
        cursor.close()
        for usuario in usuarios:
            print(usuario)
    except Exception as e:
        print(f"Error leyendo los usuarios: {e}")

# Actualizar la edad de un usuario
def actualizar_usuario(conn, id_usuario, nueva_edad):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE usuarios 
            SET edad = %s 
            WHERE id = %s
        ''', (nueva_edad, id_usuario))
        conn.commit()
        cursor.close()
        print(f'Usuario con ID {id_usuario} actualizado.')
    except Exception as e:
        print(f"Error actualizando el usuario: {e}")

# Eliminar un usuario por ID
def eliminar_usuario(conn, id_usuario):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM usuarios 
            WHERE id = %s
        ''', (id_usuario,))
        conn.commit()
        cursor.close()
        print(f'Usuario con ID {id_usuario} eliminado.')
    except Exception as e:
        print(f"Error eliminando el usuario: {e}")

# Cerrar la conexión
def cerrar_conexion(conn):
    conn.close()

# Ejemplo de uso
if __name__ == '__main__':
    conn = conectar()

    if conn:
        crear_tabla(conn)

        # Crear usuarios
        crear_usuario(conn, 'Juan', 25)
        crear_usuario(conn, 'Ana', 30)

        # Leer todos los usuarios
        print('Lista de usuarios:')
        leer_usuarios(conn)

        # Actualizar un usuario
        actualizar_usuario(conn, 1, 26)  # Cambiar la edad de Juan

        # Leer todos los usuarios después de la actualización
        print('Lista de usuarios después de la actualización:')
        leer_usuarios(conn)

        # Eliminar un usuario
        eliminar_usuario(conn, 2)  # Eliminar a Ana

        # Leer todos los usuarios después de la eliminación
        print('Lista de usuarios después de la eliminación:')
        leer_usuarios(conn)

        # Cerrar la conexión a la base de datos
        cerrar_conexion(conn)
        