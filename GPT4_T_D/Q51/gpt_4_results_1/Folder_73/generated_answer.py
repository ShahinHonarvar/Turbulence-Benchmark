
def if_contains_anagrams(word_list):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    count = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if len(word_list[i]) >= 3 and len(word_list[j]) >= 3 and is_anagram(word_list[i], word_list[j]):
                count += 1
                if count > 279:
                    return False
    return True
