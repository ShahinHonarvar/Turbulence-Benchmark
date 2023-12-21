
def lists_with_product_equal_n(lst):
    return [[i for i in lst if product % n == 0] for n in range(-41, -1)]
