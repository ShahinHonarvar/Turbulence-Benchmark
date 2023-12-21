
def lists_with_product_equal_n(circular_list):

    def multiply(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    result = []

    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j+1]
            if multiply(sublist) == -30:
                result.append(sublist)

    return result
