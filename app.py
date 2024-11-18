from flask import Flask, render_template

app = Flask(__name__) #esta variable se utiliza para crear las rutas del servidor

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/mapa_his')
def mapa_his():
    return render_template('mapa_his.html')

@app.route('/mapa_pred')
def mapa_pred():
    return render_template('mapa_pred.html')

@app.route('/predicciones')
def predicciones():
    return render_template('prediccion.html')

@app.route('/graficos')
def graficos():
    return render_template('graficas.html')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='localhost', port=5000)