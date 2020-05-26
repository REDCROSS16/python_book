from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    return render_template('results.html', the_title="РЕЗУЛЬТАТ", the_phrase=phrase, the_letters=letters,
                           the_results=str(search4letters(phrase, letters)))


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Моя первая программа по поиску вхождений букв в фразе')


if __name__ == '__main__':
    app.run(debug=True)
