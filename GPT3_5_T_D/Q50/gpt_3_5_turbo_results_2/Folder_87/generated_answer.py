
def if_contains_anagrams(strings):
    # count the frequency of each string after converting it to lowercase
    count = {}
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            count[sorted_string] = count.get(sorted_string, 0) + 1

    # check if there are at least 88 pairs of anagrams
    count_pairs = 0
    for freq in count.values():
        count_pairs += freq * (freq - 1) // 2

    return count_pairs >= 88
