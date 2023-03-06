from app import create_app, db
from app.models import Product, Customer, Sale

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Product': Product, 'Customer': Customer, 'Sale': Sale}

if __name__ == '__main__':
    app.run()
