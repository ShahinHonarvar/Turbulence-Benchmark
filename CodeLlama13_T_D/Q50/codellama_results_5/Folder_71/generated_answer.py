
def if_contains_anagrams(string_list):
    # convert all strings to lowercase
    string_list = [s.lower() for s in string_list]
    # count the number of anagrams
    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if is_anagram(string_list[i], string_list[j]):
                anagram_count += 1
    return anagram_count >= 57
