
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 818, 606 and 873
    gcf = 1
    for i in range(818, 874):
        if gcf == 1:
            gcf = my_list[i]
        else:
            gcf = gcd(gcf, my_list[i])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
