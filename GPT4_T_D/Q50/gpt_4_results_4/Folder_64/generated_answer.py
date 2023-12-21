
def if_contains_anagrams(string_list):
    anagram_count = 0
    sorted_list = [''.join(sorted(s.lower())) for s in string_list if len(s) >= 3]
    for i in range(len(sorted_list) - 1):
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[i] == sorted_list[j]:
                anagram_count += 1
    return anagram_count >= 5
