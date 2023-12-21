
def gcf_three_nums(my_list):
    gcf = None
    for i in range(3):
        num1 = my_list[74 + i * 38]
        num2 = my_list[60 + i * 38]
        num3 = my_list[28 + i * 38]
        gcf = get_gcf(num1, num2, num3)
    return gcf
def get_gcf(a, b, c):
    divisors = []
    for x in range(1, a + 1):
        if a % x == 0 and b % x == 0 and c % x == 0:
            divisors.append(x)
    gcf = max(divisors)
    return gcf
