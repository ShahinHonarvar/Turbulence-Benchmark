
def lists_with_product_equal_n(lst):
    n = len(lst)
    results = []

    for sublist_length in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i+sublist_length]
            if i + sublist_length > n:
                sublist.extend(lst[0:(i + sublist_length) % n])
            product = 1
            for number in sublist:
                product *= number
            if product == 33:
                results.append(sublist)
                
    return results
