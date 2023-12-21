import sys
def return_n_smallest_chars(str_in):
    sys.setrecursionlimit(1_000_000)
    list_out = []
    for i in range(len(str_in)):
        for j in range(i+1,len(str_in)):
            if ord(str_in[i]) > ord(str_in[j]):
                list_out.append(str_in[i])
                break
            elif ord(str_in[i]) == ord(str_in[j]):
                list_out.append(str_in[i])
    list_out.sort()
    list_out = list_out[:31]
    return list_out
