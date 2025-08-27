from flask import Flask , render_template

app=Flask (__name__)

@app.route('/')
def home():
    return render_template ("index.html")

@app.route('/about')
def home():
    return render_template ("about.html")

@app.route('/pi')
def home():
    return render_template ("pilotos.html")

@app.route('/tri')
def home():
    return render_template ("tripulantes.html")

if __name__ == 'main':
    app.run(debug=True)