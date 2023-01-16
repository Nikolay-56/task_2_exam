from flask import Flask, render_template, request

app = Flask(__name__)


result = ''


@app.route('/', methods=["GET", "POST"])
def program():

    if request.method == "POST":
        string = request.form.get('string')

        letters = 'aeiou'
        summa = 0

        for symbol in letters:
            if symbol in string:
                summa += string.count(symbol)

        global result
        result = summa

    return render_template("index.html", result=result)


if __name__ == '__main__':
    app.run()
