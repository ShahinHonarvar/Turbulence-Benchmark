
def if_contains_anagrams(string_list):
    import itertools
    counter = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
                if ''.join(sorted(string_list[i].lower())) == ''.join(sorted(string_list[j].lower())):
                    counter += 1
                    if counter > 276:
                        return False
    return True
