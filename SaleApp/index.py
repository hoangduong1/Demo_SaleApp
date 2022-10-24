from flask import render_template, request
from SaleApp import app
import dao


@app.route("/")
def home():
    cates = dao.load_categories()
    return render_template('index.html', categories=cates)


@app.route("/products")
def product_list(cate_id=None):
    cates = dao.load_categories()

    cate_id = request.args.get("category_id")
    prod = dao.load_product(cate_id=cate_id)
    return render_template('products.html', categories=cates, products=prod)


if __name__ == '__main__':
    app.run(debug=True)
