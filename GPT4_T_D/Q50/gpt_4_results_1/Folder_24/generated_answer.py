
def if_contains_anagrams(strings_list):
    from collections import defaultdict

    string_dict = defaultdict(list)
    count = 0

    for string in strings_list:
        if len(string) < 3:
            continue
        string_dict[''.join(sorted(string.lower()))].append(string)

    for key, values in string_dict.items():
        n = len(values)
        if n > 1:
            count += n * (n - 1) // 2

    return count >= 65
