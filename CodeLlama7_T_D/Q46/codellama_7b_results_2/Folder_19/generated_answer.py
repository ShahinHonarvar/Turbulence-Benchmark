
def gcf_three_nums(my_list):
    # find the greatest common factor of the elements at indices 40, 15 and 99
    gcf = 1
    for i in range(40, 100):
        if i != 99:
            gcf = gcd(gcf, my_list[i])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
