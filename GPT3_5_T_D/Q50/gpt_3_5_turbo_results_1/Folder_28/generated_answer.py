
def if_contains_anagrams(strings):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) < 3 or len(strings[j]) < 3:
                continue
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count >= 81:
                    return True
    return False
