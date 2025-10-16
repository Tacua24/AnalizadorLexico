class Token:
    __slots__ = ("tipo","lexema","linea","columna")
    def __init__(self, tipo: str, lexema: str, linea: int, columna: int):
        self.tipo = tipo
        self.lexema = lexema
        self.linea = linea
        self.columna = columna

    def __repr__(self):
        return f"<{self.tipo}, '{self.lexema}' linea {self.linea}, col {self.columna}>"

TIPOS = {
    "PALABRA_RESERVADA",
    "IDENTIFICADOR",
    "OPERADOR",
    "DELIMITADOR",
    "NUMERO",
    "CADENA",
    "COMENTARIO_LINEA",
    "COMENTARIO_BLOQUE",
    "ESPACIO",
    "ERROR",
}

PALABRAS_RESERVADAS = {
    "int", "float", "if", "else", "while", "return"
}

DELIMITADORES = {"(",")", "{","}", ",",";"}
