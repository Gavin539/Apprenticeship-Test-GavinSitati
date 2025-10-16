def calculate_total_revenue(sales_data):
    """
    Calculate total revenue from sales data.
    Revenue = price × quantity for each item, then sum all.
    """
    total = 0
    
    for item in sales_data:
        revenue = item['price'] * item['quantity']
        total += revenue
        print(f"{item['item']}: {item['price']} × {item['quantity']} = {revenue}")
    
    return total


# Store dataset
sales_data = [
    {"item": "Pen", "price": 20, "quantity": 3},
    {"item": "Book", "price": 200, "quantity": 2},
    {"item": "Bag", "price": 800, "quantity": 1}
]

print("=" * 50)
print("Total Revenue Calculation")
print("=" * 50)

total_revenue = calculate_total_revenue(sales_data)

print("=" * 50)
print(f"TOTAL REVENUE: {total_revenue}")
print("=" * 50)
