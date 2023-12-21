def find_divisors_in_range(x):
    # Function to find divisors in a range
    # x is the number to find divisors for
    # Returns a list of divisors in the range
    # 372 <= x <= 494
    # If no divisors exist in the range, an empty list is returned
    divisors = []
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(x // i)
    if x % 2 == 0:
        divisors.append(2)
    if x % 3 == 0:
        divisors.append(3)
    if x % 5 == 0:
        divisors.append(5)
    return divisors
