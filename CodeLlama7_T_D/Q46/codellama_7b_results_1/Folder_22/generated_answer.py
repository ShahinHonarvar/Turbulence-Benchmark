
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of three numbers
    # using the Euclidean algorithm

    def euclid(a, b):
        while b:
            a, b = b, a % b
        return a

    gcf = 1

    for i in range(27, 85 + 1):
        for j in range(i + 1, 85 + 1):
            for k in range(j + 1, 85 + 1):
                gcf = euclid(gcf, my_list[i] * my_list[j] * my_list[k])
    return gcf
