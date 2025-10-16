# Question 1: Second Largest Number

## Approach

My function finds the second-largest number using these steps:

1. **Remove duplicates** using `set()` to avoid counting the same number twice
2. **Sort in descending order** to get largest numbers first
3. **Return the second element** (index 1)
4. **Handle edge cases**: 
   - Lists with fewer than 2 elements
   - Lists where all numbers are identical

## Time Complexity
- **O(n log n)** due to sorting

## Alternative Approach
For better performance O(n), I could iterate once and track the largest and second-largest values without sorting.

## Code
See `Q1_SecondLargest.py`
