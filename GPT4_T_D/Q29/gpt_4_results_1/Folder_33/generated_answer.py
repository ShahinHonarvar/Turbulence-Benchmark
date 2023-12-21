
def gcf_two_nums(numbers):
    def gcf(n, m):
        while m != 0:
            n, m = m, n % m
        return n

    return gcf(numbers[166], numbers[106])
