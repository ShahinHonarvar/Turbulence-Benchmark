def find_sum_of_multiples(n):
    # Write your code here
    multiple = 1
    total = 0
    while multiple <= n:
        total += n*multiple
        multiple += 1
    return total
