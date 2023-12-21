
def if_contains_anagrams(string_list):
    from collections import defaultdict

    string_dict = defaultdict(list)
    for string in string_list:
        string_dict[''.join(sorted(string.lower()))].append(string)

    count = 0
    for key, value in string_dict.items():
        if len(key) >= 3 and len(value) >= 2:
            count += 1

    return count >= 4
