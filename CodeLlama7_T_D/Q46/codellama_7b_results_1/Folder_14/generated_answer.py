
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 17, 88 and 35
    num1 = my_list[17]
    num2 = my_list[88]
    num3 = my_list[35]
    gcf = num1 if num1 == num2 else (num1 * num2) // gcd(num1, num2)
    return gcf
