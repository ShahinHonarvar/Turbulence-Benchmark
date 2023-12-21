
def gcf_two_nums(my_list):
    return gcd(my_list[8], my_list[9])

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
