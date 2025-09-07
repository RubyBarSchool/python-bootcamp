def is_prime(num: int) -> bool:
    """
    Returns True if num is a prime number, otherwise False.
    Optimized using 6k ± 1 rule and early returns for small numbers.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    limit = int(num ** 0.5) + 1
    while i <= limit:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
