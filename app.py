from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = [
        {"id": 1, "name": "VR Headset", "price": "$299.99", "image": "images/1_VR.png"},
        {"id": 2, "name": "Smartphone", "price": "$699.99", "image": "images/1-2-iphone-png-picture-png-clipart.png"},
        {"id": 3, "name": "Laptop", "price": "$999.99", "image": "images/laptop.png"},
        {"id": 4, "name": "Iron", "price": "$499.99", "image": "images/3_Iron.png"},
        {"id": 5, "name": "Iphone", "price": "$199.99", "image": "images/2-2-iphone-png-picture.png"},
        {"id": 6, "name": "Iphone", "price": "$149.99", "image": "images/4-2-iphone-png-picture-png-image.png"},
        {"id": 7, "name": "Camera", "price": "$799.99", "image": "images/Nikon_Camera.png"},
        {"id": 8, "name": "Washing machine", "price": "$499.99", "image": "images/43_Washing_Machine.png"},
        {"id": 9, "name": "Refrigerator", "price": "$99.99", "image": "images/434_Refrigerator.png"},
        {"id": 10, "name": "Camera", "price": "$129.99", "image": "images/Canon_Camera.png"},
        {"id": 11, "name": "Drone", "price": "$899.99", "image": "images/53_drone.png"},
        {"id": 12, "name": "Flash Drive", "price": "$89.99", "image": "images/cruzer-force-usb-flash-drive-250x250.png"}
    ]


# Home page to display products
@app.route('/')
def home():
    return render_template('index.html', products=products)


# Payment page to select the payment method
@app.route('/pay/<int:product_id>', methods=['GET', 'POST'])
def pay(product_id):
    if request.method == 'POST':
        payment_method = request.form['payment_method']
        return redirect(url_for('confirmation', product_id=product_id, payment_method=payment_method))

    return render_template('pay.html', product_id=product_id)


# Order confirmation page with feedback option
@app.route('/confirmation/<int:product_id>/<payment_method>', methods=['GET', 'POST'])
def confirmation(product_id, payment_method):
    feedback = None
    recommended_products = get_recommended_products(product_id)  # Fetch recommended products

    if request.method == 'POST':
        feedback = request.form.get('feedback', '')  # Default to empty string if no feedback
        # You can store feedback or log it here
        return render_template('feedback_submitted.html', feedback=feedback, product_id=product_id,
                               payment_method=payment_method)

    return render_template('confirmation.html', product_id=product_id, payment_method=payment_method,
                           recommended_products=recommended_products)


# Get recommended products based on product_id
def get_recommended_products(product_id):
    # Example recommendation logic: You can update this with a more complex algorithm if needed
    recommendations = {
        1: [
            {"name": "VR headset", "image": "/static/images/1_VR.png", "price": 25.99, "link": "/pay/2"},
            {"name": "Drone", "image": "/static/images/53_drone.png", "price": 45.99, "link": "/pay/11"}
        ],
        2: [
            {"name": "Printer", "image": "/static/images/38_Printers.png", "price": 15.99, "link": "/pay/4"},
            {"name": "Laptop", "image": "/static/images/Laptop.png", "price": 30.99, "link": "/pay/3"}
        ],
        3: [
            {"name": "Camera", "image": "/static/images/Canon_Camera.png", "price": 150.00, "link": "/pay/10"},
            {"name": "Smartphone", "image": "/static/images/1-2-iphone-png-picture-png-clipart.png", "price": 699.99, "link": "/pay/2"}
        ],
        4: [
            {"name": "Iron", "image": "/static/images/3_Iron.png", "price": 49.99, "link": "/pay/1"},
            {"name": "Washing machine", "image": "/static/images/43_Washing_Machine.png", "price": 499.99, "link": "/pay/8"}
        ],
        # Add more recommendations for other products as needed
    }

    # Return empty list if no recommendations for this product
    return recommendations.get(product_id, [])


if __name__ == '__main__':
    app.run(debug=True)
