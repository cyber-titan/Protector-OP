from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/zeroWidthStego", methods=['GET', 'POST'])
def zero_width_stego():
    return render_template("zeroWidthStego.html")

if __name__ == '__main__':
    app.run(debug=True, port=5001)