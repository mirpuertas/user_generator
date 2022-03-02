from generator import User
from generator import Database



def generator_bot():
  print("Bienvenido al sistema de gestión de usuarios!")
  Database.create_table()
  menu()
  

def menu():
    res = input('Quiere crear, eliminar o buscar un usuario? \n[a] Crear \n[b] Eliminar \n[c] Buscar \n> ')
    if res == "a":
        return create_user()
    elif res == "b":
        return delete_user()
    elif res == "c":
        return get_user()
    else:
        print_message()
        return menu()


def create_user():
    name = input("Ingrese el nombre: ", ).capitalize()
    surname = input("Ingrese el apellido: ", ).capitalize()
    area = input("Ingrese el área: ", ).upper()
    user1 = User(name, surname)
    username = user1.username()
    codigo = username.encode('utf-8').hex()[:6].upper()
    vm = virtual_machine(codigo, area)
    data = Database(name, surname, area, username, vm)
    data.put_in()
    print("Usuario creado satisfactoriamente... ")
    data.get_user(username)
    close_question()


    
def virtual_machine(codigo, area):
    res = input("Por favor, seleccione el Sistema Operativo de la VM: \n[a] Windows \n[b] Linux \n>")
    if res == "a":
        return "VMW" + codigo + area[:3] + str(User.today.month)
    elif res == "b":
        return "VML" + codigo + area[:3] + str(User.today.month)
    else:
        print_message()
        virtual_machine()


def delete_user():
    res = input('Por favor ingrese el nombre de usuario que desea eliminar: ', )
    Database.get_user(res)
    query = Database.delete(res)
    close_question()


def get_user():
    res = input('Por favor ingrese el nombre de usuario que desea buscar: ', )
    Database.get_user(res)
    close_question()


def print_message():
  print("Selección equivocada, por favor vuelva a seleccionar.")


def close_question():
    res = input('Desea hacer algo más? \n[a] Si \n[b] No \n> ')
    if res == "a":
        return menu()
    elif res == "b":
        print("Usted ha finalizado sesión.")
    else:
        print_message()
        return close_question()




generator_bot()
