from flask import Flask, render_template,request
app =Flask(__name__)
#ruta de la raiz y envio de variables
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quienes_somos")
def quienes_somos():
    return render_template("quienes_somos.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/noticias")
def noticias():
    return render_template("noticias.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/proceso",methods = ['POST'])
def proceso():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    mensaje = request.form.get('mensaje')
    return render_template("salida.html", nombre=nombre, email=email,  mensaje=mensaje)

#debemos poner todas las rutas dentro de el index
if __name__ == "__main__":
    app.run(debug=True)