from flask import Flask, render_template, request
from abbreviations import schwartz_hearst

app = Flask(__name__)


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        in_text = request.form['in_text']
        out_text = '\n'

        abrev_dict = schwartz_hearst.extract_abbreviation_definition_pairs(doc_text=in_text)

        for key in abrev_dict.keys():
            out_text += str(key) + ' : '
            out_text += str(abrev_dict[key]) + '\n'
        out_text = out_text.split('\n')
    else:
        in_text = ''
        out_text = ''

    return render_template('index.html', out_text=out_text, in_text=in_text)


if __name__ == "__main__":
    app.run()
