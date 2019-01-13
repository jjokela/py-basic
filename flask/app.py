from flask import Flask, Markup, render_template, request
from compound import compound

app = Flask(__name__)

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]


@app.route('/line')
def line():

    present_value = float(request.args.get('present_value'))
    rate = float(request.args.get('interest_rate'))
    time = int(request.args.get('time'))

    line_labels = list(range(0, int(time) + 1))
    line_values = [compound(present_value, rate, x) for x in line_labels]

    return render_template('line_chart.html',
                           title='Compounding Interest',
                           max=line_values[-1],
                           min=line_values[0],
                           labels=line_labels,
                           values=line_values)


if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=True)

