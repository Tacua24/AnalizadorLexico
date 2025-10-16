import re
from typing import Optional

RE_IF     = re.compile(r"\bif\s*\([^)]*\)\s*\{")
RE_ELSE   = re.compile(r"\belse\b")
RE_WHILE  = re.compile(r"\bwhile\s*\([^)]*\)\s*\{")
RE_DECL   = re.compile(
    r"\b(?:int|float)\b\s+[A-Za-z_][A-Za-z0-9_]*\s*(?:=\s*[^;]+)?\s*;",
)

def detectar_estructura(linea: str) -> Optional[str]:
    if RE_IF.search(linea):
        return "IF"
    if RE_WHILE.search(linea):
        return "WHILE"
    if RE_ELSE.search(linea):
        return "ELSE"
    return None

def detectar_declaracion(linea: str) -> Optional[str]:
    m = RE_DECL.search(linea)
    if m:
        return m.group(0).strip()
    return None

