from flask import Flask, render_template, request, redirect, url_for
from ..models import db, customer

bp = Blueprint("customer", __name__, url_prefix="'/clientes")

@bp.route('/')
def list():
    # Lista todos os clientes do banco de dados
    customers = Customer.query.all()
    return render_template("customer/list.html", customers=customers)

@bp.route('/novo', methods=('GET', 'POST'))
def create():
    if request.method == "POST":
        # Cria um novo cliente do banco de dados
        name = request.form['name']
        email = request.form['email']
        customer = Customer(name=name, email=email)
        db.session.add(customer)
        db.session.commit()
        return redirect(url_for("customer.list"))
    return render_template("customer/create.html")

@bp.route('/editar/<int:id>', methods=('GET', 'POST'))
def edit(id):
    costumer = Customer.query.get(id)
    if request.method == "POST":
        # Atualiza o cliente com base nos dados do formulário
        customer.name = request.form['name']
        customer.email = request.form["email"]
        db.session.commit()
        return redirect(url_for('customer.list'))
    return render_template('customer/edit.html', customer=customer)
