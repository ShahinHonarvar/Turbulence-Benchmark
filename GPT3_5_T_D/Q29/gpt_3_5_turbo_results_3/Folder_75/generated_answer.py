
def gcf_two_nums(num_list):
    def find_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    index_1 = 42
    index_2 = 25
    num_1 = num_list[index_1]
    num_2 = num_list[index_2]

    return find_gcf(num_1, num_2)
