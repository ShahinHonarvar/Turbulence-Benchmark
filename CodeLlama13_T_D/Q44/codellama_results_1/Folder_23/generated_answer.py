
def composite_nums_between_indices(mylist):
    return {i for i in mylist[20:31] if len(set(range(1, i+1))) != len(set(range(1, i)))}
