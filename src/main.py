import sys
from collections import Counter, defaultdict
from pathlib import Path

from .lexer import analizar_linea
from .recognizers import detectar_estructura, detectar_declaracion

def procesar_archivo(ruta_entrada: Path, ruta_log: Path):
    conteo = Counter()
    errores = []
    lineas_estructura = []
    lineas_declaracion = []

    with ruta_entrada.open(encoding="utf-8") as f_in, ruta_log.open("w", encoding="utf-8") as f_log:
        for num_linea, linea in enumerate(f_in, start=1):
            # Tokenizar y log por linea
            tokens = analizar_linea(linea, num_linea)
            for t in tokens:
                if t.tipo != "ESPACIO":
                    conteo[t.tipo] += 1
                    f_log.write(f"Línea {t.linea}: '{t.lexema}' → {t.tipo}\n")
                if t.tipo == "ERROR":
                    errores.append((t.linea, t.columna, t.lexema))

            estructura = detectar_estructura(linea)
            if estructura:
                lineas_estructura.append((num_linea, estructura))
                f_log.write(f"Línea {num_linea}: ESTRUCTURA_CONTROL → {estructura}\n")

            declaracion = detectar_declaracion(linea)
            if declaracion:
                lineas_declaracion.append((num_linea, declaracion))
                f_log.write(f"Línea {num_linea}: ESTRUCTURA_CONTROL → {declaracion}\n")

        # resumen
        f_log.write("\n=====RESUMEN=====\n")
        for tipo, cnt in sorted(conteo.items()):
            f_log.write(f"{tipo}: {cnt}\n")

        if errores:
            f_log.write("\n===== ERRORES LEXICOS=====\n")
            for ln, col, sym in errores:
                f_log.write(f"Linea {ln}, col {col}: ERROR -> simbolo '{sym}' no reconocido\n")

    # salida consola
    print("analisis completo")
    print(f" archivo de entrada: {ruta_entrada}")
    print(f" Log generado en : {ruta_log}")
    if errores:
        print(f"   Errores léxicos   : {len(errores)} (ver detalle en el log)")
    else:
        print(" errores lexicos : 0")

def main():
    if len(sys.argv) < 2:
        print("uso: python -m src.main <ruta_archivo_entrada")
        sys.exit(1)

    ruta_entrada = Path(sys.argv[1])
    if not ruta_entrada.exists():
        print(f"No existe el archivo de entrada: {ruta_entrada}")
        sys.exit(1)

    outputs = Path("outputs")
    outputs.mkdir(exist_ok=True)
    ruta_log = outputs / "log.txt"

    procesar_archivo(ruta_entrada, ruta_log)

if __name__ == "__main__":
    main()
