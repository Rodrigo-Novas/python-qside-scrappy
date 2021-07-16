import abc
from re import A
import tkinter as tk
import os
from sqlalchemy.sql.annotation import EMPTY_ANNOTATIONS
from sqlalchemy.sql.expression import text

from sqlalchemy.sql.visitors import ClauseVisitor
from models import user
import db
import datetime
import bcrypt

def ventana_inicio():
    """
        ventana de inicio de la app
    """
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=tk.Tk()
    ventana_principal.geometry("300x250") #  DIMENSIONES DE LA VENTANA
    ventana_principal.title("Calyx loguin prueba de concepto") # TITULO DE LA VENTANA
    tk.Label(text="Escoja su opcion", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()
    tk.Label(text="").pack() # el pack Crea widget en el widget padre
    tk.Button(text="Registrar", height="2", width="30", bg=pestas_color, command=registro).pack()
    tk.Label(text="").pack()
    tk.Button(text="Acceder", height="2", width="30", bg=pestas_color, command=login).pack()
    tk.Label(text="").pack()
    ventana_principal.mainloop()


def registro():
    """
        Registro a la BDD
    """
    global ventana_registro
    ventana_registro=tk.Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x250")
    global email
    global contraseña
    global entrada_email
    global entrada_clave
    email=tk.StringVar()
    contraseña=tk.StringVar()

    tk.Label(ventana_registro, text="Registro", bg="LightGreen").pack()
    tk.Label(ventana_registro, text="").pack()
    etiqueta_email = tk.Label(ventana_registro, text="Nombre de usuario * ")
    etiqueta_email.pack()
    entrada_email = tk.Entry(ventana_registro, textvariable=email)
    entrada_email.pack()
    etiqueta_clave = tk.Label(ventana_registro, text="Contraseña * ")
    etiqueta_clave.pack()
    entrada_clave = tk.Entry(ventana_registro, textvariable=contraseña, show="*")
    entrada_clave.pack()
    tk.Label(ventana_registro, text="").pack
    tk.Button(ventana_registro, text="Registrate", width=10, height=1, bg="LightGreen", command= lambda: registro_usuario(entrada_email, entrada_clave)).pack()

def registro_usuario(email, clave):

    db.base.metadata.create_all(db.engine)
    fecha = datetime.date.today().strftime("%d - %m - %Y")
    clave_encriptada = bcrypt.hashpw(clave.get().encode("utf-8"), bcrypt.gensalt())
    usuario=user(email, clave_encriptada.decode("utf-8"), fecha)
    db.session.add(usuario)
    print(usuario.id)
    db.session.commit()
    entrada_email.delete(0, tk.END)
    entrada_clave.delete(0, tk.END)
    tk.Label(ventana_registro, text="Registro completo", fg="green", font=("calibri", 11)).pack

def login():
    global ventana_login
    ventana_login = tk.Toplevel(ventana_registro)
    ventana_login.title("Acceso a la cuenta")
    tk.Label(ventana_login, text="Introduzca nombre de usuario").pack()
    tk.Label(ventana_login, text="").pack()

    global verifica_usuario
    global verifica_clave

    verifica_usuario = tk.StringVar()
    verifica_clave = tk.StringVar()

    global entrada_login_usuario
    global entrada_login_clave

    tk.Label(ventana_login, text="Nombre usuario *").pack()
    entrada_login_usuario= tk.Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    tk.Label(ventana_login, text="").pack()
    tk.Label(ventana_login, text="Contraseña *").pack()
    entrada_login_clave= tk.Entry(ventana_login, textvariable=verifica_clave, show="*")
    entrada_login_clave.pack()
    tk.Label(ventana_login, text="").pack
    tk.Button(ventana_login, text="Acceder", width=10, height=1, bg="LightGreen", command= lambda: login_usuario(entrada_login_usuario, entrada_login_clave)).pack()

def obtener_usuarios():
    return db.session.query(user).all()

def obtener_usuario(email):
    return db.session.query(user).filter_by(email=email).first()


def login_usuario(email, clave):
    usuario = obtener_usuario(email.get())
    es_clave_valida = bcrypt.checkpw(clave.get().encode("utf-8"), usuario.contraseña.encode("utf-8"))
    if es_clave_valida:
        entrada_email.delete(0, tk.END)
        entrada_clave.delete(0, tk.END)
        tk.Label(ventana_login, text="Usuario correcto", fg="green", font=("calibri", 11)).pack
    else:
        entrada_login_usuario.delete(0, tk.END)
        entrada_login_clave.delete(0, tk.END)
        tk.Label(ventana_login, text="Usuario incorrecto", fg="green", font=("calibri", 11)).pack



if __name__ == "__main__":
    # registro_usuario("robert@gmail.com", "contraseña")
    # print(obtener_usuarios())
    ventana_inicio()