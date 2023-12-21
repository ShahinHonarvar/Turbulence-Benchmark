
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by iteratively dividing both numbers until
    # they are equal or one is greater than the other.
    num1 = my_list[56]
    num2 = my_list[88]
    if num1 > num2:
        while num1 != num2:
            num1 -= 1
            num2 += 1
        return num1
    else:
        while num1 != num2:
            num1 += 1
            num2 -= 1
        return num1
