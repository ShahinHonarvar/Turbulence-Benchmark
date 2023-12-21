
def if_contains_anagrams(str_list):
    from collections import defaultdict

    def sorted_str(s):
        return "".join(sorted(s.lower()))
    
    str_dict = defaultdict(list)

    for s in str_list:
        if len(s) >= 3:
            str_dict[sorted_str(s)].append(s)

    count = 0
    for k, v in str_dict.items():
        if len(v) > 1:
            count += len(v) * (len(v) - 1) // 2

    return count >= 194
