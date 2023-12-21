
def lists_with_product_equal_n(circular_list):
    def get_sublists(lis):
        sublists = []
        for i in range(len(lis)):
            for j in range(len(lis)):
                if i != j and j != (i + len(lis) - 1) % len(lis) and not {i, (i + len(lis) - 1) % len(lis)} & set(range(j, (j + len(lis)) % len(lis))):
                    sublists.append(lis[j:(j + len(lis)) % len(lis)])
        return sublists

    result = []
    circular_list = circular_list * 2
    for sublist in get_sublists(circular_list):
        product = 1
        for num in sublist:
            product *= num
        if product == 10:
            result.append(sublist)
    return result
