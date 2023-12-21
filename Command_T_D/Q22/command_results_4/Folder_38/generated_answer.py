def find_sum_of_multiples(n):
    # Given a number n, find the sum of the first 77 multiples of n
    # e.g. find_sum_of_multiples(12) returns 77*13+...+77*144
    # Note that 1*n+2*n+3*n+...+77*n can be replaced with (n+1)*77
    return (n+1)*77
