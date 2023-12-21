
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    result = []

    for starting_index in range(length):
        for ending_index in range(starting_index,length+starting_index):

            product = circular_list[starting_index % length]
            
            for index in range(starting_index + 1, ending_index + 1):
                product *= circular_list[index % length]

            if product == 48:
                sublist = []
                for index in range(starting_index, ending_index + 1):
                    sublist.append(circular_list[index % length])
                result.append(sublist)
    return result
