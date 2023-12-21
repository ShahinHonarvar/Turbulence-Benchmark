
def if_contains_anagrams(string_list):
    import collections
    counter = collections.Counter()
    count = 0
    for string in string_list:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            counter[key] += 1
            if counter[key] == 2:
                count += 1
                if count > 69:
                    return False
    return True
