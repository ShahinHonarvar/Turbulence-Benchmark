
def gcf_three_nums(numbers):
    def find_gcf(x, y):
        while y:
            x, y = y, x % y
        return x

    num1 = numbers[24]
    num2 = numbers[45]
    num3 = numbers[38]

    gcf = find_gcf(find_gcf(num1, num2), num3)
    return gcf
