
def lists_with_product_equal_n(circular_list):
    # establish the target product and list for output
    target_product = -18
    results = []

    # re-create the circular list by concatenating it with itself
    circular_list = circular_list * 2
    length = len(circular_list) // 2

    # iterate through the list of integers, and for each integer,
    # iterate through the sublists ending at that integer
    for i in range(length):
        for j in range(i + 1, i + length + 1):
            sublist = circular_list[i:j]

            # calculate the product of the integers in the sublist
            product = 1
            for num in sublist:
                product *= num

            # if the product equals the target, add the sublist to the results
            if product == target_product:
                results.append(sublist)

    return results
