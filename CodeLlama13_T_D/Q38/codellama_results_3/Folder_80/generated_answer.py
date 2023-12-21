
def find_subset_of_length_n(elements):
    return len([1 for i in range(len(elements)+1) for j in range(i+1,len(elements)+1) for k in range(j+1,len(elements)+1)])
