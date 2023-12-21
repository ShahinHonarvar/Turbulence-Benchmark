
def insert_after_index(lst):
    return lst[:28] + [lst[28] for i in range(len(lst[28]))] + [41, 69] + lst[28+1:-1] + lst[-1]
