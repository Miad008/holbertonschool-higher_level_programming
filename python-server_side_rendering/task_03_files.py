from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def load_json_data():
    with open('products.json') as f:
        return json.load(f)

def load_csv_data():
    data = []
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])  # ensure id is int
            row['price'] = float(row['price'])  # ensure price is float
            data.append(row)
    return data

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    if source == 'json':
        products = load_json_data()
    elif source == 'csv':
        products = load_csv_data()
    else:
        error = "Wrong source"
        return render_template("product_display.html", error=error)

    if product_id:
        filtered = [p for p in products if p.get("id") == product_id]
        if not filtered:
            error = "Product not found"
            return render_template("product_display.html", error=error)
        products = filtered

    return render_template("product_display.html", products=products)
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
