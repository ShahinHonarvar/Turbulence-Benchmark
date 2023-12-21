
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 13, 70 and 32
    gcf = my_list[13]
    for i in range(len(my_list)):
        if i != 13:
            gcf = gcd(gcf, my_list[i])
    return gcf

def gcd(a, b):

    # Calculate the greatest common divisor of two positive integers

    while b:

        a, b = b, a % b

    return a
