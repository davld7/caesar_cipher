import tkinter as tk

alfabeto_minusculas = 'abcdefghijklmnñopqrstuvwxyz'
alfabeto_mayusculas = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'


def cifrado(texto, clave):
    cifrado = ''
    for letra in texto:
        if letra in alfabeto_minusculas:
            indice = (alfabeto_minusculas.index(letra) +
                      clave) % len(alfabeto_minusculas)
            cifrado += alfabeto_minusculas[indice]
        elif letra in alfabeto_mayusculas:
            indice = (alfabeto_mayusculas.index(letra) +
                      clave) % len(alfabeto_mayusculas)
            cifrado += alfabeto_mayusculas[indice]
        else:
            cifrado += letra
    return cifrado


def descifrado(texto, clave):
    descifrado = ''
    for letra in texto:
        if letra in alfabeto_minusculas:
            indice = (alfabeto_minusculas.index(letra) -
                      clave) % len(alfabeto_minusculas)
            descifrado += alfabeto_minusculas[indice]
        elif letra in alfabeto_mayusculas:
            indice = (alfabeto_mayusculas.index(letra) -
                      clave) % len(alfabeto_mayusculas)
            descifrado += alfabeto_mayusculas[indice]
        else:
            descifrado += letra
    return descifrado


def cifrar_texto():
    texto_original = entrada_texto.get()
    clave = int(entrada_clave.get())
    texto_cifrado = cifrado(texto_original, clave)
    entrada_resultado_cifrado.delete(0, tk.END)
    entrada_resultado_cifrado.insert(0, texto_cifrado)


def descifrar_texto():
    texto_cifrado = entrada_texto.get()
    clave = int(entrada_clave.get())
    texto_descifrado = descifrado(texto_cifrado, clave)
    entrada_resultado_descifrado.delete(0, tk.END)
    entrada_resultado_descifrado.insert(0, texto_descifrado)


ventana = tk.Tk()
ventana.title('Cifrado César')

ventana.geometry('400x350')

etiqueta_texto = tk.Label(ventana, text='Texto:')
entrada_texto = tk.Entry(ventana)
entrada_texto.insert(0, "Hola Mundo!")

etiqueta_clave = tk.Label(ventana, text='Clave:')
entrada_clave = tk.Entry(ventana)
entrada_clave.insert(0, "1")

etiqueta_resultado_cifrado = tk.Label(ventana, text='Texto Cifrado:')
etiqueta_resultado_descifrado = tk.Label(ventana, text='Texto Descifrado:')

entrada_resultado_cifrado = tk.Entry(ventana)
entrada_resultado_descifrado = tk.Entry(ventana)

etiqueta_texto.pack(padx=10, pady=5, anchor='w')
entrada_texto.pack(fill='x', padx=10, pady=5)
etiqueta_clave.pack(padx=10, pady=5, anchor='w')
entrada_clave.pack(fill='x', padx=10, pady=5)

boton_cifrar = tk.Button(ventana, text='Cifrar', command=cifrar_texto)
boton_descifrar = tk.Button(ventana, text='Descifrar', command=descifrar_texto)

boton_cifrar.pack(padx=10, pady=10, fill='x')
boton_descifrar.pack(padx=10, pady=10, fill='x')

etiqueta_resultado_cifrado.pack(padx=10, pady=5, anchor='w')
entrada_resultado_cifrado.pack(fill='x', padx=10, pady=5)

etiqueta_resultado_descifrado.pack(padx=10, pady=5, anchor='w')
entrada_resultado_descifrado.pack(fill='x', padx=10, pady=5)

ventana.mainloop()
