from flask import Flask, render_template, request, escape
from vsearch import search4letters
import mysql.connector

app = Flask(__name__)


dbconfig = {
    'host': '127.0.0.1',
    'user': 'vsearch',
    'password': 'pass',
    'database': 'vsearchlogDB',
}
# подключение драйвера для баз данных
conn = mysql.connector.connect(**dbconfig)
# подключение курсора- штуки для передачи команд в базу данных
cursor = conn.cursor()
_SQL = ''' show tables'''
cursor.execute(_SQL)


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearchlog', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent,res, file=log, sep='|')


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_title="РЕЗУЛЬТАТ", the_phrase=phrase, the_letters=letters,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Моя первая программа по поиску вхождений букв в фразе')


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearchlog') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title='ВЫВОД ИНФОРМАЦИИ С ЛОГА НА СТРАНИ', the_row_titles=titles, the_data=contents)


if __name__ == '__main__':
    app.run(debug=True)
