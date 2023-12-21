
def if_contains_anagrams(strings):
    def is_anagram(string1, string2):
        return sorted(string1.lower()) == sorted(string2.lower()) and len(string1) >= 3

    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count >= 411:
                    return True
    return False
