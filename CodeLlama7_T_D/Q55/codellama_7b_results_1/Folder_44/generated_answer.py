
def lists_with_product_equal_n(circulist):
    # check if the given circulist is empty or not
    if len(circulist) == 0:
        return []

    # initialize an empty list to store the sublists with product equal to n
    sublists = []

    # loop through the given circulist and find all the contiguous integers whose product equals n
    for i in range(len(circulist)):
        current_sum = 1
        current_product = circulist[i]
        for j in range(i+1, len(circulist)):
            current_sum *= circulist[j]
            if current_sum == n:
                sublists.append([circulist[k] for k in range(i, j+1)])

    # return the list of sublists with product equal to n
    return sublists
