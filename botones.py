from tkinter import *
from functools import partial

import validacion_de_usuario as vdu
import programa.juego as jg


def codigo_boton_jugar(raiz):
    raiz.destroy()
    jg.main()


def codigo_boton_envio_registro(v_registro, entry_usuario, entry_contra_uno, entry_contra_dos):
    # Recopilacion de datos de usuario
    usuario = entry_usuario.get()
    entry_usuario.delete(0, "end")
    lista_contras = [entry_contra_uno.get(),
                     entry_contra_dos.get()]
    entry_contra_uno.delete(0, "end")
    entry_contra_dos.delete(0, "end")

    v_registro.destroy()

    vdu.registro_usuario_nuevo(usuario, lista_contras)


def codigo_boton_registro():

    v_registro = Tk()
    v_registro.title("Registro")
    v_registro.geometry('500x230')
    v_registro.config(bg="#FF6800")
    v_registro.iconbitmap("archivos/zanahoria.ico")

    v_registro_frame = Frame(v_registro, width=1200, height=600)
    v_registro_frame.config(bg="#FF6800")
    v_registro_frame.grid(row=0, column=0)

    # Labels - Registro
    # TITULO
    label_titulo_registro = Label(
        v_registro_frame, text="Registre un usuario", font=("Arial Black", 10))

    label_titulo_registro.config(bg="#FF6800")
    label_titulo_registro.grid(row=0, column=1, padx=10, pady=10)

    # USUARIO
    label_usuario_registro = Label(
        v_registro_frame, text="USUARIO", font=("Arial Black", 9))

    label_usuario_registro.config(bg="#FF6800")
    label_usuario_registro.grid(row=1, column=0, padx=10, pady=10)

    # CONTRASEÑA 1
    label_contra_uno_registro = Label(
        v_registro_frame, text="CONTRASEÑA", font=("Arial Black", 9))
    label_contra_uno_registro.config(bg="#FF6800")
    label_contra_uno_registro.grid(row=2, column=0, padx=10, pady=10)

    # CONTRASEÑA 2
    label_contra_dos_registro = Label(
        v_registro_frame, text="REPITA LA CONTRASEÑA", font=("Arial Black", 9))

    label_contra_dos_registro.config(bg="#FF6800")
    label_contra_dos_registro.grid(row=3, column=0, padx=10, pady=10)

    # Entry - Registro
    # Usuario
    entry_usuario_registro = Entry(v_registro_frame)
    entry_usuario_registro.grid(row=1, column=1, padx=10, pady=10)

    # CONTRASEÑA
    # 1
    entry_contra_uno_registro = Entry(v_registro_frame)
    entry_contra_uno_registro.grid(row=2, column=1, padx=10, pady=10)
    entry_contra_uno_registro.config(show="*")
    # 2
    entry_contra_dos_registro = Entry(v_registro_frame)
    entry_contra_dos_registro.grid(row=3, column=1, padx=10, pady=10)
    entry_contra_dos_registro.config(show="*")

    boton_envio_registro = Button(v_registro_frame, text="Registrarse", font=(
        "Arial Black", 9), command=partial(codigo_boton_envio_registro, v_registro, entry_usuario_registro, entry_contra_uno_registro, entry_contra_dos_registro))

    boton_envio_registro.grid(row=4, column=1, padx=10, pady=10)
    boton_envio_registro.config(bg="#FCA468", relief="solid", bd=1.5)


def codigo_boton_ingreso(raiz, entry_usuario, entry_contra_uno):
    # Recopilacion de datos de usuario
    usuario = entry_usuario.get()
    entry_usuario.delete(0, "end")
    # En caso de ingreso
    contra = entry_contra_uno.get()
    entry_contra_uno.delete(0, "end")
    vdu.validar_usuario_y_contrasenia(raiz, usuario, contra)
