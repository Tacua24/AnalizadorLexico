import re
from typing import List, Tuple
from .tokens import Token, PALABRAS_RESERVADAS, DELIMITADORES

PATRONES: List[Tuple[str, str]] = [
    ("COMENTARIO_BLOQUE", r"/\*[\s\S]*?\*/"),       
    ("COMENTARIO_LINEA",  r"//[^\n]*"),
    ("CADENA",            r'"[^"\n]*"'),
    ("OPERADOR",          r"==|!=|<=|>=|&&|\|\|"),
    ("OPERADOR",          r"[+\-*/<>!=]"),          
    ("DELIMITADOR",       r"[(){},;]"),
    ("NUMERO",            r"\d+(?:\.\d+)?"),
    ("IDENTIFICADOR",     r"[A-Za-z_][A-Za-z0-9_]*"),
    ("ESPACIO",           r"\s+"),
]

PATRONES_COMP = [(tipo, re.compile(p)) for tipo, p in PATRONES]

def analizar_linea(linea: str, num_linea: int):
    tokens = []
    i = 0
    L = len(linea)

    while i < L:
        match = None
        for tipo, regex in PATRONES_COMP:
            m = regex.match(linea, i)
            if m:
                lexema = m.group(0)
                if tipo == "ESPACIO":
                    i = m.end()
                    match = True
                    break
                if tipo == "IDENTIFICADOR" and lexema in PALABRAS_RESERVADAS:
                    tokens.append(Token("PALABRAS_RESERVADAS", lexema, num_linea, i + 1))
                else:
                    if tipo == "DELIMITADOR" and lexema not in DELIMITADORES:
                        tokens.append(Token("ERROR", lexema, num_linea, i + 1))
                    else:
                        tokens.append(Token(tipo, lexema, num_linea, i + 1))
                i = m.end()
                match = True
                break
        if not match:
            tokens.append(Token("ERROR", linea[i], num_linea, i + 1))
            i += 1
    return tokens
