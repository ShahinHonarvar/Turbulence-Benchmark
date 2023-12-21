
def lists_with_product_equal_n(lst):
    def find_sublists_with_product_equal_n(lst):
        result = []
        for i in range(len(lst)):
            product = 1
            for j in range(i, len(lst) + i):
                product *= lst[j % len(lst)]
                if product == -93:
                    result.append(lst[i:j+1])
        return result

    return find_sublists_with_product_equal_n(lst)
