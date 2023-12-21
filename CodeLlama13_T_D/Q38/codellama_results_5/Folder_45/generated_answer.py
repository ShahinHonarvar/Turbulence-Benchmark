
def find_subset_of_length_n(elements):
    return len([i for i in range(len(elements)+1) if sum(map(lambda x: x==0, elements[i:])) == 33])
