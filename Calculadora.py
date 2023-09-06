import tkinter as tk
from tkinter import Label, Entry, Button, StringVar
from PIL import Image, ImageTk
import pricer
import pandas as pd
import numpy as np

class BondPricerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Preços de Ativos de Renda Fixa")

        # Definir o tamanho inicial da janela
        #self.root.geometry("800x600")

        # Variáveis de entrada
        self.val_date_var = StringVar()
        self.vna_var = StringVar()
        self.vencimento_var = StringVar()
        self.taxa_var = StringVar()
        self.result_var = StringVar()

        # Rótulos e entradas
        Label(root, text="Data da Liquidação:").grid(row=0, column=0)
        Entry(root, textvariable=self.val_date_var).grid(row=0, column=1)

        Label(root, text="VNA:").grid(row=1, column=0)
        Entry(root, textvariable=self.vna_var).grid(row=1, column=1)

        Label(root, text="Vencimento:").grid(row=2, column=0)
        Entry(root, textvariable=self.vencimento_var).grid(row=2, column=1)

        Label(root, text="Taxa (%):").grid(row=3, column=0)
        Entry(root, textvariable=self.taxa_var).grid(row=3, column=1)

        # Logo
        logo_image = Image.open("logo.png")  # Substitua "logo.png" pelo caminho para o seu logo.
        logo_image.thumbnail((100, 100))  # Redimensione para 100x100 pixels.
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = Label(root, image=logo_photo)
        logo_label.grid(row=0, column=3, rowspan=4, padx=10)  # Ajuste a posição e o tamanho conforme necessário.

        # Botão para calcular o preço
        Button(root, text="Calcular Preço", command=self.calcular_preco).grid(row=4, column=0, columnspan=2)

        # Resultado
        Label(root, text="Preço do Ativo:").grid(row=5, column=0)
        Label(root, textvariable=self.result_var).grid(row=5, column=1)

    def calcular_preco(self):
        val_date = self.val_date_var.get()
        vna = float(self.vna_var.get())
        vencimento = self.vencimento_var.get()
        taxa = float(self.taxa_var.get()) / 100  # Converter a taxa de porcentagem para decimal

        ntnb = pricer.NTNB(val_date, vencimento, taxa, vna, bucketting=True)
        preco = ntnb.price

        self.result_var.set(str(preco))

if __name__ == "__main__":
    root = tk.Tk()
    app = BondPricerApp(root)
    root.mainloop()