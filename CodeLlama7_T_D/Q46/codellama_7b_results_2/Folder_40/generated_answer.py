
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 1, 6 and 8
    return gcf(my_list[1], my_list[6], my_list[8])
# Helper function to calculate the greatest common factor
def gcf(a, b, c):
    # Calculate the least common multiple of a and b
    lcm = (a * b) / gcd(a, b)
    # Calculate the least common multiple of c and lcm
    return lcm_c(lcm, c)
# Helper function to calculate the greatest common factor of two numbers
def gcd(a, b):
    if b == 0:
        return a

    else:
        return gcd(b, a % b)

# Helper function to calculate the least common multiple of three numbers
def lcm_c(lcm, c):
    return (lcm * c) / gcd(lcm, c)
