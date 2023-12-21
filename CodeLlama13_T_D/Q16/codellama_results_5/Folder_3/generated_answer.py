
def sum_even_ints_inclusive(my_list):
    # Use a list comprehension to create a new list of even integers from index 62 to index 92, both inclusive
    even_ints = [i for i in my_list[62:93] if i % 2 == 0]
    # Return the sum of the new list
    return sum(even_ints)
