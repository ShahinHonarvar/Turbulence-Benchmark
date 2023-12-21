def if_contains_anagrams(input_str):
    input_str = set(input_str)
    input_str = sorted(input_str)
    input_str = input_str[:-2]
    return input_str[1:].count(input_str[0]) >= 41
