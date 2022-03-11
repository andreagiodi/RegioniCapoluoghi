from flask import Flask, render_template, request
app = Flask(__name__)
import pandas as pd 

df = pd.read_csv("https://raw.githubusercontent.com/andreagiodi/flask/main/regioni_capoluoghi.csv")


@app.route('/', methods=['GET'])
def index():

    return render_template('indexcapo.html')




@app.route('/risp', methods=['GET'])
def risp():
    indice = request.args['indice']
    radio = request.args['sel']
    a = indice
    b =  df[df['regione'] == indice]['capoluogo'].values[0]
    return render_template('error.html', err=b)

    return render_template('error.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)
