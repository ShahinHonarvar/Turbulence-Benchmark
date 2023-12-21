
def insert_at_index(L):
    return [i for i in L[:990]] + [905, 742] + [i for i in L[990:]] + [i for i in L[2: 990]] + [i for i in L[3:]]
