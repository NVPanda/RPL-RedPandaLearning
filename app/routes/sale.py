from flask import Blueprint, render_template, request, redirect, url_for
from ..models import db, sale, product

bp = Blueprint('sale', __name__, url_prefix='/vendas')


@bp.route('/')
def list():
    # lista todos as vendas do banco de dados
    sales = Sale.query.all()
    return render_template('sale/list.html', sales=sales)


@bp.route('/novo', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        # Cria uma nova venda com base nos dados do formulário
        product_id = int(request.form['product_id'])
        quantity = int(request.form["quantity"])
        product = Product.query.get(product_id)
        sale = Sale(product=product, quantity=quantity)
        db.session.add(sale)
        db.session.commit()
        return redirect(url_for("sales.list"))
    # Lista todos os produtos disponíveis para venda
    products = Product.query.filter(Product.quantity > 0).all()
    return render_template("sale/create.html", products=products)


@bp.route('/editar/<int:id>', methods=('GET', 'POST'))
def edit(id):
    sale = Sale.query.get(id)
    if request.method == "POST":
        # Atualiza a venda com base nos dados do banco de dados
        sale.product_id = int(request.form['product_id'])
        sale.product = Product.query.get(sale.product_id)
        sale.quantity = int(request.form['quantity'])
        db.session.commit()
        return redirect(url_for('sale.list'))
    products = Product.query.all()
    return render_template('sale/edit.html', sale=sale, products=products)