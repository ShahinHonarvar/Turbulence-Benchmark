
def gcf_two_nums(numbers):
    def find_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    return find_gcf(numbers[18], numbers[37])
