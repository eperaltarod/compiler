import tkinter as tk
from tkinter import scrolledtext
import ply.lex as lex

# Definimos el lexer
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# Función que recibe texto, lo pasa al lexer y muestra el resultado
def analizar():
    input_text = input_field.get('1.0', tk.END)
    lexer.input(input_text)
    output_field.delete('1.0', tk.END)
    while True:
        tok = lexer.token()
        if not tok:
            break
        output_field.insert(tk.END, f"{tok}\n")

# Crear la ventana principal
window = tk.Tk()
window.title("Analizador Léxico")

# Campo de entrada de texto
tk.Label(window, text="Ingresa el código:").pack()
input_field = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
input_field.pack()

# Botón para ejecutar el análisis
tk.Button(window, text="Analizar", command=analizar).pack()

# Campo de salida para los tokens generados
tk.Label(window, text="Tokens:").pack()
output_field = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
output_field.pack()

# Iniciar la interfaz gráfica
window.mainloop()
