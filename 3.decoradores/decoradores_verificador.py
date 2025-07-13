
usuarios = []


def validar_usuario(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if len(arg) < 5:
                print("El usuario debe contener minimo 5 caracteres")
                return
        return func(*args, **kwargs)
    return wrapper


@validar_usuario
def agregar_usuario(usuario):
    return usuarios.append(usuario)


for _ in range(3):
    usuario = input("Usuario: ")
    agregar_usuario(usuario)

if len(usuarios) != 0:
    print(usuarios)
