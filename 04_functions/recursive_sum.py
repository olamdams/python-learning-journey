def total (n):
    """Calculate the sum of all integers from 1 to n."""
    if n < 0:
        raise ValueError("Total is not defined for negative numbers.")
    elif n == 0:
        return 0
    else:
        return n + total(n - 1)
 print(total(5))  # Output: 15

