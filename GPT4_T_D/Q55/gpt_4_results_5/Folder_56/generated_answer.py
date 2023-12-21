
def lists_with_product_equal_n(c_list):
    N = len(c_list)
    seqs = [c_list[i:j] for i in range(N) for j in range(i+1, i+N+1)]
    return [seq for seq in seqs if prod(seq) == -65]

def prod(lst):
    result = 1
    for item in lst:
        result *= item
    return result
