
def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            first_string = strings[i].lower()
            second_string = strings[j].lower()
            if sorted(first_string) == sorted(second_string):
                anagram_count += 1
                
    return anagram_count <= 61
