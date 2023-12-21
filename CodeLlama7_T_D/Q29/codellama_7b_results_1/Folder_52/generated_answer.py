
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (GCF) of two numbers in a list using the Euclidean algorithm
    def egcd(a, b):
        if b == 0:
            return (1, 0)
        else:
            x, y = egcd(b, a % b)
            return (y, x - (a // b) * y))
    gcf = 1
    for i in range(90, 41):
        gcf = egcd(my_list[i], gcf)[0]
    return gcf
