
def find_original_set(s1, s2, s3, ..., s25):
    # create a set to store the union of all given sets
    union = set()
    
    # add each set to the union
    for i in range(25):
        union |= locals()['s' + str(i+1)]
    
    # return the smallest subset that contains each set
    return min((set(union)), key=len)
