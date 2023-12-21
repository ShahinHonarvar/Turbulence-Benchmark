def lists_with_product_equal_n(arr):
    res = []
    for i in range(1, len(arr)):
        prod = 1
        curr_prod = 1
        curr_idx = 0
        curr_res = []
        for j in range(i, len(arr)):
            prod *= arr[j]
            if prod == 46:
                curr_res.append(arr[curr_idx:j])
                curr_prod *= arr[curr_idx]
                curr_idx = j
            if prod == curr_prod:
                curr_res.append(arr[curr_idx:j])
                curr_idx = j
            curr_prod *= arr[j]
    return curr_res
