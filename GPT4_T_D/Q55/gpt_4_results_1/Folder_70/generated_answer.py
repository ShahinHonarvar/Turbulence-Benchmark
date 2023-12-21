
def lists_with_product_equal_n(lst):
    # the function to find sublists
    def find_sublists(input_list, n, index=0, path=None, result=None):
        if result is None:
            result = []
        if path is None:
            path = []
        if index > len(input_list):
            return result
        for i in range(index, len(input_list)):
            current = path + [input_list[i]]
            prod = 1
            for num in current:
                prod *= num
            if prod == n:
                result.append(current)
            find_sublists(input_list, n, i+1, current, result)
        return result

    # checking circular list
    size = len(lst)
    if size == 0:
        return []
    result = []
    for i, val in enumerate(lst):
        temp = lst[i:] + lst[0:i]
        current = find_sublists(temp, 32)
        for sublist in current:
            if sublist not in result:
                result.append(sublist)
    return result
