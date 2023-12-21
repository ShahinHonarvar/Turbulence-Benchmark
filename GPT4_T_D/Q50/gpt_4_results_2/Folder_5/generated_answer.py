
def if_contains_anagrams(str_list):
    anagrams = {}
    count = 0

    for i in str_list:
        if len(i) >= 3:
            i_lower = i.lower()
            sorted_str = ''.join(sorted(i_lower))
            if sorted_str in anagrams.keys():
                anagrams[sorted_str].append(i_lower)
            else:
                anagrams[sorted_str] = [i_lower]

    for v in anagrams.values():
        n = len(v)
        if n > 1:
            count += n*(n-1)//2

    if count >= 21:
        return True
    return False
