import sys
def sum_of_divisors_in_range(n):
    if n <= 228:
        return 0
    elif n <= 924:
        return n * (n + 1) // 2
    elif n <= 846:
        return n * (n - 1) // 2
    print(sum_of_divisors_in_range(int(sys.stdin.readline().strip())))
