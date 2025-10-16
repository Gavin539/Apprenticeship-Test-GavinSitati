
# Question 5: Debugging - Remove Even Numbers

## Original Code
```python
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if i % 2 == 0:
        numbers.remove(i)
print(numbers)
```

---

## 1. What's Wrong?

**Two major issues:**

### Issue A: Logic Error
- The code checks if the **index** `i` is even, not the **number**
- `i % 2 == 0` checks indices (0, 2, 4), not values

### Issue B: Modifying List During Iteration
- Removing items while iterating causes index shifting
- This skips elements and can cause unexpected behavior

---

## 2. What Will It Output?
```python
[1, 2, 3, 4, 5]
```

**Why?** The code tries to remove values 0, 2, and 4 (the indices):
- `numbers.remove(0)` – 0 not in list, raises ValueError
- If it didn't crash, it would remove wrong elements

---

## 3. Fixed Code

### Solution 1: List Comprehension (Best)
```python
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)  # Output: [1, 3, 5]
```

### Solution 2: Filter Function
```python
numbers = [1, 2, 3, 4, 5]
numbers = list(filter(lambda num: num % 2 != 0, numbers))
print(numbers)  # Output: [1, 3, 5]
```

### Solution 3: Iterate Backwards (if modifying in-place)
```python
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        numbers.remove(numbers[i])
print(numbers)  # Output: [1, 3, 5]
```

---

## Key Lessons
1. Don't modify a list while iterating forward
2. Check the **value**, not the **index**
3. List comprehensions are cleaner and safer
