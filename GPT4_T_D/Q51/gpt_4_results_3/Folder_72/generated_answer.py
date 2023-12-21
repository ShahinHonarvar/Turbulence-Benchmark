
def if_contains_anagrams(string_list):
    anagrams = {}
    pair_count = 0
    for word in string_list:
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) < 3:
            continue
        if sorted_word in anagrams:
            pair_count += 1
            if pair_count > 188:
                return False
        else:
            anagrams[sorted_word] = 1
    return True
