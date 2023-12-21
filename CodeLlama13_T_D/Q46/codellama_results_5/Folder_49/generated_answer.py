
def gcf_three_nums(numbers):
    gcf = 1
    for i in range(34, 38):
        gcf = _gcd(gcf, numbers[i])
    for i in range(38, 77):
        gcf = _gcd(gcf, numbers[i])
    return gcf
