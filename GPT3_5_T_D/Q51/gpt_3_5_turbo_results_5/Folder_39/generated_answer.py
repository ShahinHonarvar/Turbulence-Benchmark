
def if_contains_anagrams(strings):
    anagram_count = 0

    def is_anagram(str1, str2):
        str1_sorted = sorted(str1.lower())
        str2_sorted = sorted(str2.lower())
        return str1_sorted == str2_sorted

    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) < 3 or len(strings[j]) < 3:
                continue
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 257:
                    return False

    return True
