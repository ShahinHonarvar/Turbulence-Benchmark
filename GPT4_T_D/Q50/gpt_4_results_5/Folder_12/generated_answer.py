
def if_contains_anagrams(input_list):
    anagram_count = 0
    input_list = [''.join(sorted(word.lower())) for word in input_list if len(word) >= 3]
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] == input_list[j]:
                anagram_count += 1
                if anagram_count >= 69:
                    return True
    return False
