from flask import Flask, render_template, request
from bc.IEEE754 import *


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    x = request.form.get('floating_point_number')
    p = request.form.get('precision')
    output_mode = 0
    if x is not None:
        output_mode = 1
        ieee754rep = IEEE754(float(x), int(p))
        return render_template("index.html", title="IEEE 754 Conversion Tool",
                               outputmode=output_mode, outputx=x,
                               outputhex=ieee754rep.str2hex(),
                               outputbinary=str(ieee754rep))
    else:
        return render_template("index.html", title="IEEE 754 Conversion Tool",
                               outputmode=output_mode)


if __name__ == '__main__':
    app.run()
