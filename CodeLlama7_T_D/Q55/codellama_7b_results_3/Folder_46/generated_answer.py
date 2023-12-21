
def lists_with_product_equal_n(lst, n):
    # Check if the product of all elements in lst is equal to n
    if prod(lst) == n:
        return [lst]  # Return a list with the given list as its only element
    else:
        return []  # Return an empty list if there are no sublists with the desired property
