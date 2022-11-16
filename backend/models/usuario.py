import mysql.connector
from mysql.connector import Error

class Usuario():
  def __init__(self):
    try:
      self.conexion= mysql.connector.connect(
        host='localhost',
        port=3306,
        user= 'root',
        password='',
        db='lawebdelcafe'
      )
    except Error as ex:
      print('Error al intentar la conexión {0}'.format(ex))
  def listarUsuarios(self):
    if self.conexion.is_connected():
      try:
        cursor= self.conexion.cursor()
        cursor.execute("SELECT * FROM usuarios ORDER BY nombre ASC")
        resultados=cursor.fetchall()
        cursor.close()
        return resultados
      except Error as ex:
        print('Error al intentar la conexión {0}'.format(ex))
  def registrarUsuario(self, usuario):
    if self.conexion.is_connected():
      try:
        cursor=self.conexion.cursor()
        sql= "INSERT INTO usuarios (id_usuario,nombre,apellido,email,contraseña) VALUES ({0},'{1}', '{2}','{3}','{4}')"
        cursor.execute(sql.format(usuario[0],usuario[1], usuario[2], usuario[3], usuario[4]))
        self.conexion.commit()
        cursor.close()
        print("¡Usuario Registrado!\n")
      except Error as ex:
        print('Error al intentar la conexión {0}'.format(ex))
  def actualizarUsuario(self, usuario):
    if self.conexion.is_connected():
      try:
        cursor=self.conexion.cursor()
        sql= "UPDATE usuarios SET nombre = '{0}', apellido = '{1}', email='{2}', contraseña='{3}' WHERE id_usuario={4}"
        cursor.execute(sql.format(usuario[1],usuario[2],usuario[3],usuario[4], usuario[0]))
        self.conexion.commit()
        cursor.close()
        print("¡Usuario Actualizado!\n")
      except Error as ex:
        print('Error al intentar la conexión {0}'.format(ex))
  def eliminarUsuario(self, dniUsuarioEliminar):
    if self.conexion.is_connected():
      try:
        cursor = self.conexion.cursor()
        sql = "DELETE FROM usuarios WHERE id_usuario = '{0}'"
        cursor.execute(sql.format(dniUsuarioEliminar))
        self.conexion.commit()
        cursor.close()
        print("¡usuario eliminado!\n")
      except Error as ex:
        print("Error al intentar la conexión: {0}".format(ex))

def menuPrincipal():
  continuar=True
  while(continuar):
    opcionCorrecta= False
    while(not opcionCorrecta):
      print("=== MENÜ PRINCIPAL ===")
      print("1*- Listar usuarios")
      print("2*- Registrar usuario")
      print("3*- Actualizar usuario")
      print("4*- Eliminar usuario")
      print("5*- Salir")
      print("===")
      opcion =int(input("Seleccione una opción: "))
      if opcion <1 or opcion >5:
        print("Elige una opción correcta...")
      elif opcion == 5:
        continuar=False
        print("Gracias por usar este sistema!")
        break
      else:
        opcionCorrecta=True
        ejecutarOpcion(opcion)
      
    

def ejecutarOpcion(opcion):
  conexion=Usuario()
  if opcion == 1:
    try:
      usuarios= conexion.listarUsuarios()
      if len(usuarios)>0:
        listarUsuarios(usuarios)
      else:
        print('No hay usuarios')
    except:
      print('Ocurrio un Error')
  elif opcion == 2:
    usuario = pedirDatosRegistro()
    try:
      conexion.registrarUsuario(usuario)
    except:
      print('Ocurrio un Error')
  elif opcion == 3:
    try:
      usuarios= conexion.listarUsuarios()
      if len(usuarios) > 0:
        usuario = pedirDatosActualizacion(usuarios)
        if usuario:
          conexion.actualizarUsuario(usuario)
        else:
          print("DNI de usuario a actualizar no encontrado..")
      else:
        print("No se encontraron usuarios")
    except:
      print('Ocurrio un Error')
  elif opcion == 4:
    try:
      usuarios= conexion.listarUsuarios()
      if len(usuarios) > 0:
        idEliminar=pedirDatosEliminacion(usuarios)
        if not(idEliminar==""):
          conexion.eliminarUsuario(idEliminar)
        else:
          print("Id no encontrado...\n")
      else:
        print("No se encontraron usuarios")
    except:
      print('Ocurrio un Error')
  else:
    print("Opcion no valida...")



def listarUsuarios(usuarios):
  print('\nUsuarios\n')
  contador=1
  for usuario in usuarios:
    datos="{0}. Id:{1} | Nombre: {2}, Apellido: {3}, Email: {4}, Contraseña: {5}"
    print(datos.format(contador, usuario[0],usuario[1],usuario[2],usuario[3],usuario[4]))
    contador = contador +1
print(" ")

def pedirDatosRegistro():
  id_usuario= int(input("Ingrese el id: "))
  nombre= input("Ingrese el nombre: ")
  apellido= input("Ingrese el apellido: ")
  email= input("Ingrese el email: ")
  contraseña= input("Ingrese la contraseña: ")
  usuario= (id_usuario,nombre,apellido, email,contraseña)
  return usuario

def pedirDatosActualizacion(usuarios):
  listarUsuarios(usuarios)
  existeId=False
  idEditar=int(input("Ingrese el id del usuario a editar: "))
  for usuario in usuarios:
    if usuario[0] == idEditar:
      existeId=True
      break
  if existeId:
    nombre= input("Ingrese el nombre a modificar: ")
    apellido= input("Ingrese el apellido a modificar: ")
    email= input("Ingrese el email a modificar: ")
    contraseña= input("Ingrese la contraseña a modificar: ")

    usuario= (idEditar,nombre,apellido,email,contraseña)
  else:
    usuario=None

  return usuario

def pedirDatosEliminacion(usuarios):
  listarUsuarios(usuarios)
  existeId=False
  idEliminar=int(input("Ingrese el id del usuario a eliminar: "))
  for usuario in usuarios:
    if usuario[0] == idEliminar:
      existeId=True
      break
  if not existeId:
    idEliminar=""
    
  return idEliminar

menuPrincipal()