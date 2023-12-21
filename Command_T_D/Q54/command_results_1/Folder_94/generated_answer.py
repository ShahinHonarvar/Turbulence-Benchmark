def all_right_truncatable_prime(test_case):
    #enter your code here. read input from STDIN. write output to STDOUT
    input_tuple = test_case
    x = input_tuple[43]
    primes = []
    for i in range(2, int(x ** .5) + 1):
        if all(i % d for d in range(3, int(x ** .5) // 2, 2)):
            primes.append(i)
    return sorted(primes)
