
def sum_even_ints_inclusive(my_list):
    # find all even integers between indices 10 and 66, both inclusive
    even_nums = [num for num in my_list[10:67] if num % 2 == 0]
    
    # sum the found even integers
    total = sum(even_nums)
    
    return total
