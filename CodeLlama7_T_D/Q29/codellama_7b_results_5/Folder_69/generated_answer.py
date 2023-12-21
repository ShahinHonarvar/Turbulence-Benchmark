
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers
    # by finding their HCF (Highest Common Factor)
    def hcf(a, b):
        if b == 0:
            return a

        else:

            return hcf(b, a % b)

    # Return the HCF of two numbers at indices 894 and 801
    return hcf(my_list[894], my_list[801])
