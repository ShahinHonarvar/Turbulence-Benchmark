def palindromes_between_indices(s):
    return set(i[::-1] for i in range(len(s)-5,len(s)-2,-1) if i[0]==i[-1])
