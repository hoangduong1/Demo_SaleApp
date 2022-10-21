from flask import render_template
from SaleApp import app
import dao


@app.route("/")
def home():
    cates = dao.load_categories()
    prod = dao.load_product()
    return render_template('index.html', categories=cates, products=prod)


if __name__ == '__main__':
    app.run(debug=True)
