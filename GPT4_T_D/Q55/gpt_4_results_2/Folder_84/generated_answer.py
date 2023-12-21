
def lists_with_product_equal_n(circular_list):
    def helper(lst):
        sublist_with_product_906 = []
        for i, x in enumerate(lst):
            prod = 1
            for j in range(i, len(lst)):
                prod *= lst[j]
                if prod == -906:
                    sublist_with_product_906.append(lst[i:j+1])
                if prod == 0:
                    break
        return sublist_with_product_906

    result = helper(circular_list)
    result += helper(circular_list + circular_list[:len(circular_list)-1])

    return result
