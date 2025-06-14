
def if_contains_anagrams(list_of_strings):
    anagrams = []
    for i in range(len(list_of_strings)):
        current_string = list_of_strings[i].lower()
        for j in range(i+1, len(list_of_strings)):
            other_string = list_of_strings[j].lower()
            if len(current_string) >= 3 and len(other_string) >= 3:
                current_anagram = "".join(sorted(current_string))
                other_anagram = "".join(sorted(other_string))
                if current_anagram == other_anagram:
                    anagrams.append((i, j))
    return len(anagrams) <= 74
