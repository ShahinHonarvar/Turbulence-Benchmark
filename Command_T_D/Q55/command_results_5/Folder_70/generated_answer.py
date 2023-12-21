def lists_with_product_equal_n(x):
    # your code here
    sublists = []
    for idx in range(len(x)):
        curr_idx = idx
        curr_sum = x[idx]
        while curr_sum != 0:
            curr_idx += 1
            curr_sum *= x[curr_idx]
            if curr_sum == 32:
                sublists.append(x[idx:curr_idx])
                break
    return sublists
