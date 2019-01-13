from flask import Flask, render_template, request

from compound import compound

app = Flask(__name__)


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

