from flask import(
    Flask,
    redirect,
    render_template,
    request
)
import sqlite3


app = Flask(__name__)

product = {}

@app.route('/', methods=['GET','POST'])
def get_main():
    if request.method == 'POST':
        title = request.form.get('title', type=str)
        price = request.form.get('price', type=int)
        if title and price:
            product[title] = price
        return render_template('index.html', product =product)
    return render_template('index.html', product =product)

@app.route('/log', methods=['GET','POST'])
def get_log():
    if request.method == 'POST':
        name = request.form.get('name', type=str)
        age = request.form.get('age', type=int)
        
        # Открытие нового соединения для каждого запроса
        conn = sqlite3.connect('users.db', check_same_thread=False)
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO user (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        conn.close()  
        
        return render_template('reg.html', name=name, age=age)
    return render_template('reg.html')


@app.route('/reg', methods=['GET','POST'])
def get_reg():

    return render_template('reg.html')




if __name__ == '__main__':
    app.run(debug=True)

#структура более менее ясно но на логин не додумался