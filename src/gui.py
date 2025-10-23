import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from pathlib import Path

from .main import procesar_archivo

class AnalizadorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Lexico")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        self.archivo_path = None

        # === Titulo ====
        tk.Label(
            root, text="Analizador Lexico", font=("Helvetica", 18, "bold"),
            bg="#f0f0f0", fg="#333"
        ).pack(pady=10)

        # === Botones ===
        frame_botones = tk.Frame(root, bg="#f0f0f0")
        frame_botones.pack(pady=10)

        btn_cargar = tk.Button(
            frame_botones, text="Cargar archivo",
            command=self.cargar_archivo, bg="#0078D7", fg="white", width=20
        )
        btn_cargar.grid(row=0, column=0, padx=10)

        btn_analizar = tk.Button(
            frame_botones, text="Analizar",
            command=self.analizar, bg="#28A745", fg="white", width=20
        )
        btn_analizar.grid(row=0, column=1, padx=10)

        # === cuadro de texto ===
        self.texto_salida = scrolledtext.Scrolledtext(
            root, wrap=tk.WORD, width=90, height=25, font=("Courier", 10)
        )
        self.texto_salida.pack(padx=10, pady=10)

    def cargar_archivo(self):
        """Selecciona archivo de prueba"""
        archivo = filedialog.askopenfilename(
            title="Selecciona el archivo de prueba",
            filetypes=[("Archvos de texto", "*.txt")]
        )
        if archivo:
            self.archivo_path = Path(archivo)
            messagebox.showinfo("Archivo cargado", f"Archivo seleccionado:\{archivo}")
            return

        salida_log = Path("outputs/log.txt")
        try:
            procesar_archivo(self.archivo_path, salida_log)
            with open(salida_log, "r", encoding="utf-8") as f:
                contenido = f.read()
            self.texto_salida.delete("1.0", tk.END)
            self.texto_salida.insert(tk,END, contendio)
            messagebox.showinfo("Exito", f"Error al analizar:\n{e}")

if __name__ = "__main__":
    root = tk.Tk()
    app = AnalizadorGUI(root)
    root.mainloop()
