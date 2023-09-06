from flask import Flask, render_template, request
from PIL import Image, ImageTk
import pricer
import tkinter as tk

app = Flask(__name__)

@app.route('/')
def calculadora():
    return render_template('calculadora.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    val_date = request.form.get('val_date')
    vna = float(request.form.get('vna'))
    vencimento = request.form.get('vencimento')
    taxa = float(request.form.get('taxa')) / 100  # Converter a taxa de porcentagem para decimal

    ntnb = pricer.NTNB(val_date, vencimento, taxa, vna, bucketting=True)
    preco = ntnb.price

    return render_template('calculadora.html', resultado=preco)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

    #app.run(debug=True)

#python CalculadoraHTML.py
