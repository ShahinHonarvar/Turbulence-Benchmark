
def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for i in range(len(list_of_strings)):
        current_string = list_of_strings[i].lower()
        for j in range(i+1, len(list_of_strings)):
            next_string = list_of_strings[j].lower()
            if len(current_string) >= 3 and len(next_string) >= 3:
                if "".join(sorted(current_string)) == "".join(sorted(next_string)):
                    anagram_pairs += 1
    return anagram_pairs >= 43
