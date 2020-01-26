import re

from flask import Flask, request
from flask import render_template
import NGD
app = Flask(__name__, template_folder='./templates')


@app.route('/', methods=['GET','POST'])
def index():
    print(request.form.get('term1'))
    if request.method == 'POST':
        term1 = request.form.get('term1')
        term2 = request.form.get('term2')
        source = request.form.get('source')
        result = NGD.similarity(term1,term2,source)
        N = sum([1 for i in re.findall(r'[^.]+.', source.lower())])
        return render_template('index.html',term1=term1, term2=term2, source=source, N=N,result=result)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=4000)
