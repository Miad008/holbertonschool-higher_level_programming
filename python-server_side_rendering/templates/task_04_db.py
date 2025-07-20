from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def load_json_data():
    with open('products.json') as f:
        return json.load(f)

def load_csv_data():
    data = []
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            data.append(row)
    return data

def load_sql_data():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "category": r[2], "price": r[3]} for r in rows]

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    try:
        if source == 'json':
            products = load_json_data()
        elif source == 'csv':
            products = load_csv_data()
        elif source == 'sql':
            products = load_sql_data()
        else:
            error = "Wrong source"
            return render_template("product_display.html", error=error)
    except Exception:
        error = "Error loading data from " + source
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
