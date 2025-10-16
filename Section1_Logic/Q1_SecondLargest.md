def second_largest(numbers):
    """
    Returns the second-largest number in a list.
    Approach: Remove duplicates, sort in descending order, return second element.
    """
    if len(numbers) < 2:
        return None  # Not enough numbers
    
    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort(reverse=True)     # Sort descending
    
    if len(unique_numbers) < 2:
        return None  # All numbers are the same
    
    return unique_numbers[1]


# Test cases
test_lists = [
    [10, 20, 4, 45, 99],
    [1, 1, 1, 1],
    [5, 3, 8, 3, 8, 10],
    [7],
    [15, 15, 20, 20, 25]
]

print("=" * 50)
print("Second Largest Number - Test Results")
print("=" * 50)

for i, test_list in enumerate(test_lists, 1):
    result = second_largest(test_list)
    print(f"Test {i}: {test_list}")
    print(f"Second Largest: {result}")
    print("-" * 50)
