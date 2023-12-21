
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers whose product equals n

    for i in range(len(circular_list)):
        product = 1

        for j in range(i, len(circular_list)):
            product *= circular_list[j]

            if product == n:
                sublists.append(circular_list[i:j+1])

                break

            elif product > n:
                break

    return sublists
