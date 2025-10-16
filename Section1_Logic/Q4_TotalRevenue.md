# Question 4: Total Revenue Calculation

## Approach

Calculate total revenue by:
1. Looping through each item in the sales data
2. Multiplying `price × quantity` for each item
3. Summing all individual revenues

## Formula
```
Total Revenue = Σ (price × quantity)
```

## Calculation Breakdown
- Pen: 20 × 3 = 60
- Book: 200 × 2 = 400
- Bag: 800 × 1 = 800
- **Total: 1260**

## Time Complexity
- **O(n)** where n is the number of items

## Code
See `Q4_TotalRevenue.py`
