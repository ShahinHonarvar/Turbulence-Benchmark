
def gcf_two_nums(numbers):
    def gcf(a, b):
        while(b):
            a, b = b, a % b
        return a
    return gcf(numbers[42], numbers[25])
