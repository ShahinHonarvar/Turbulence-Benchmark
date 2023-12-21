
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers using Euclid's algorithm
    def euclid(a, b):
        while b:
            a, b = b, a % b
        return a

    return euclid(my_list[29], my_list[74])
