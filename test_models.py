from models import Product, Order

def test_product_repr():
    p = Product(name='Apples', price=1.99, description='Fresh apples from local farms')
    assert repr(p) == '<Product Apples>'

def test_order_repr():
    o = Order(items='[{"id": 1, "name": "Apples", "price": 1.99, "description": "Fresh apples from local farms", "quantity": 2}]', total=3.98, payment_id='pi_123')
    assert repr(o) == '<Order 1>'