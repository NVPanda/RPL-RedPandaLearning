from flask import Blueprint, render_template, request, redirect, url_for,
from ..models import db, product

bp = Blueprint('product', __name__, url_prefix='/produtos')

@bp.route('/')
def list():
    # Lista todos os produtos do banco de dados
    products = Product.query.all()
    return render_template('product/list.html', products=products)

@bp.route('/novo', methods=('GET', 'POST'))
def create():
    if request.method == "POST":
        name = request.form['Nome']
        price = float(request.form["Preço"])
        quantity = int(request.form["Quantidade"])
        product = Product(name=name, price=price, quantity=quantity)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for("product.list"))
    return render_template('product/create.html')

@bp.route("/editar/<int:id>", methods=('GET', 'POST'))
def edit(id):
    product = Product.query.get(id)
    if request.method == 'POST':
        # Atualiza o produto conforme dados do formulário.
        product.name = request.form['Nome']
        product.price = float(request.form['price'])
        product.quantity = int(request.form['quantity'])
        db.session.commit()
        return redirect(url_for('product.list'))
    return render_template('product/edit.html', product=product)   