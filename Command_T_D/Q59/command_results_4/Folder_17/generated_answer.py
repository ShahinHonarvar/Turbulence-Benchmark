def all_left_truncatable_prime(n):
    # Insert your code here
    x = n[36]
    # Your code goes here
    return sorted(set(str(x) for x in range(2, int(str(x)[0]))) if x > 1)
