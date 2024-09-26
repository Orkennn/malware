from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

products = [
    {"id": 1, "name": "Stylish Shoes", "description": "Comfortable and stylish shoes for everyday wear.", "price": 59.99, "image": "https://via.placeholder.com/150"},
    {"id": 2, "name": "Classic Watch", "description": "A timeless classic watch for any occasion.", "price": 129.99, "image": "https://via.placeholder.com/150"},
    {"id": 3, "name": "Leather Bag", "description": "Durable leather bag for your daily needs.", "price": 89.99, "image": "https://via.placeholder.com/150"},
    {"id": 4, "name": "Smartphone", "description": "Latest smartphone with advanced features.", "price": 699.99, "image": "https://via.placeholder.com/150"},
    {"id": 5, "name": "Wireless Headphones", "description": "Enjoy music with high-quality wireless headphones.", "price": 149.99, "image": "https://via.placeholder.com/150"},
    {"id": 6, "name": "Smart Fitness Watch", "description": "Stylish watch for health and fitness.", "price": 129.99, "image": "https://via.placeholder.com/150"}

]

@app.get("/", response_class=HTMLResponse)
async def get_form():
    product_cards = ''.join(
        f"""
        <div class="product">
            <img src="{product['image']}" alt="{product['name']}"/>
            <h3>{product['name']}</h3>
            <p>{product['description']}</p>
            <p class="price">Price: ${product['price']:.2f}</p>
            <button onclick="alert('Added {product['name']} to cart!')">Add to Cart</button>
        </div>
        """ for product in products
    )
    return f"""
    <html>
        <head>
            <title>Online Store - Simple XSS Test</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f3f4f6;
                }}
                .container {{
                    width: 80%;
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px;
                    background: white;
                    border-radius: 8px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    text-align: center;
                    color: #333;
                }}
                .products {{
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: space-between;
                }}
                .product {{
                    border: 1px solid #e5e5e5;
                    border-radius: 5px;
                    padding: 15px;
                    margin: 15px 0;
                    width: calc(30% - 20px);
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    background: #fff;
                }}
                .product img {{
                    max-width: 100%;
                    height: auto;
                    border-radius: 5px;
                }}
                .product h3 {{
                    color: #007bff;
                }}
                .price {{
                    font-weight: bold;
                    color: #28a745;
                }}
                input[type="text"] {{
                    width: calc(100% - 22px);
                    padding: 10px;
                    margin: 5px 0 10px;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                    font-size: 16px;
                }}
                input[type="submit"] {{
                    background-color: #007bff;
                    color: white;
                    border: none;
                    padding: 10px;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                    transition: background-color 0.3s;
                }}
                input[type="submit"]:hover {{
                    background-color: #0056b3;
                }}
                .reviews {{
                    margin-top: 20px;
                }}
                .review {{
                    margin: 10px 0;
                    padding: 10px;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                    background: white;
                }}
                .button-container {{
                    margin-top: 20px;
                    text-align: center;
                }}
                .reset-button {{
                    background-color: #dc3545;
                    padding: 10px;
                    border-radius: 4px;
                    border: none;
                    color: white;
                    cursor: pointer;
                    transition: background-color 0.3s;
                }}
                .reset-button:hover {{
                    background-color: #c82333;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to Our Online Store!</h1>
                <div class="products">
                    {product_cards}
                </div>
                <h2>Leave a Comment:</h2>
                <form action="/submit" method="post">
                    <label for="name">Enter your comment:</label>
                    <input type="text" id="name" name="name" required />
                    <input type="submit" value="Submit" />
                </form>
                <h2>User Reviews:</h2>
                <div class="reviews" id="reviews">
                    <div class="review">Great products! Highly recommend.</div>
                    <div class="review">I love the quality of the items!</div>
                </div>
            </div>
        </body>
    </html>
    """

@app.post("/submit", response_class=HTMLResponse)
async def submit_form(name: str = Form(...)):
    return f"""
    <html>
        <head>
            <title>Comment Submitted - Online Store</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f3f4f6;
                }}
                .container {{
                    width: 80%;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background: white;
                    border-radius: 8px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    text-align: center;
                    color: #333;
                }}
                .result {{
                    margin-top: 20px;
                    padding: 15px;
                    background: #f8f9fa;
                    border-radius: 5px;
                    border: 1px solid #dee2e6;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }}
                a {{
                    display: inline-block;
                    margin-top: 15px;
                    text-decoration: none;
                    color: #007bff;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                .button-container {{
                    margin-top: 20px;
                    text-align: center;
                }}
                .reset-button {{
                    background-color: #dc3545;
                    padding: 10px;
                    border-radius: 4px;
                    border: none;
                    color: white;
                    cursor: pointer;
                    transition: background-color 0.3s;
                }}
                .reset-button:hover {{
                    background-color: #c82333;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Comment Submitted</h1>
                <div class="result">
                    <p>Your comment: {name}</p> <!-- В этой строке XSS-уязвимость -->
                </div>
                <div class="button-container">
                    <a href="/">Go back to store</a>
                    <button class="reset-button" onclick="window.location.href='/'">Reset</button>
                </div>
            </div>
        </body>
    </html>
    """
