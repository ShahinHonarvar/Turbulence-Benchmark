
def return_nth_smallest_ascii(s):
    ascii_dict = {}
    for i in range(len(s)):
        if s[i] in ascii_dict:
            ascii_dict[s[i]].append(i)
        else:
            ascii_dict[s[i]] = [i]
    min_indices = sorted(list(range(17, 57)), key=lambda x: ascii_dict[x])
    min_indices.sort()
    return s[min_indices[8]]
