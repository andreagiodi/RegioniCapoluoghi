from flask import Flask, render_template, request
app = Flask(__name__)

capoluoghiRegione = {'Abruzzo': 'Aquila', 'Basilicata': 'Potenza', 'Calabria': 'Catanzaro', 'Campania': 'Napoli','Emilia-Romagna': 'Bologna','FriuliVeneziaGiulia': 'Trieste', 'Lazio': 'Roma', 'Liguria': 'Genova','Lombardia': 'Milano','Marche': 'Ancona', 'Molise': 'Campobasso','Piemonte': 'Torino', 'Puglia': 'Bari', 'Sardegna': 'Cagliari', 'Sicilia': 'Palermo', 'Toscana': 'Firenze', 'Trentino-Alto-Adige': 'Trento', 'Umbria': 'Perugia', 'Valle Daosta': 'Aosta', 'Veneto': 'Venezia'}





@app.route('/', methods=['GET'])
def index():
    return render_template('indexcapo.html')


@app.route('/risp', methods=['GET'])
def risp():
    indice = request.args['indice']
    radio = request.args['sel']
    if radio == 'regione':
        if indice in capoluoghiRegione:
            capo = capoluoghiRegione[indice]
            return render_template('indexcapo1.html', capol=capo)
        return render_template('error.html')
    if radio == 'capoluogo':
        dct = {v: k for k, v in capoluoghiRegione.items()}
        if indice in dct:
            capo = dct[indice]
            return render_template('indexcapo1.html', capol=capo)
        return render_template('error.html')
    return render_template('error.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)