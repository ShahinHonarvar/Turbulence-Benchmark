
def if_contains_anagrams(strings_list):
    anagrams_count = 0
    processed_strings = [''.join(sorted(s.lower())) for s in strings_list if len(s)>=3]
    for index, word in enumerate(processed_strings):
        for comparison_word in processed_strings[index+1:]:
            if word == comparison_word:
                anagrams_count += 1
    if anagrams_count >= 17:
        return True
    return False
