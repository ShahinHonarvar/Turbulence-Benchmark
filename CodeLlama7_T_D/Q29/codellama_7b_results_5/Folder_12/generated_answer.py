
def gcf_two_nums(my_list):
    # Calculate the greatest common divisor of two numbers
    def gcd(a, b):
        if b == 0:
            return a

        else:

            return gcd(b, a % b)

    # Return the greatest common factor of two specified indices
    return gcd(my_list[56], my_list[54])
