from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", num=1, color='blue')

@app.route('/play')
def level1():
    return render_template("index.html", num=3, color='blue')

@app.route('/play/<int:num>')
def level2(num):
    return render_template("index.html", num=num, color='blue')
    
@app.route("/play/<int:num>/<string:color>")
def level3(num, color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)

