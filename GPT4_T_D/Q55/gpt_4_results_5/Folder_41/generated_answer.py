
def lists_with_product_equal_n(circular_list):
    def find_sublists(input_list, target_product):
        sublists = []
        for i in range(len(input_list)):
            for j in range(i, len(input_list)):
                if i == j:
                    sublist_product = input_list[i]
                else:
                    sublist_product *= input_list[j]
                
                if sublist_product == target_product:
                    sublists.append(input_list[i:j+1])
        return sublists

    expanded_list = circular_list + circular_list[:-1]
    return find_sublists(expanded_list, -20)
