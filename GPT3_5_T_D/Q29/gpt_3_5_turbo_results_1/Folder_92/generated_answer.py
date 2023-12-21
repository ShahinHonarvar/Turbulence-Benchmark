
def gcf_two_nums(numbers):
    a = numbers[0][0]
    b = numbers[0][1]
    while b:
        a, b = b, a % b
    return a
