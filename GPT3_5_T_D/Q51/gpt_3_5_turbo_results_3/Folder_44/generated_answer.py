
def if_contains_anagrams(strings):
    def count_occurrences(string):
        occurrences = [0] * 26
        for char in string.lower():
            if char.isalpha():
                occurrences[ord(char) - ord('a')] += 1
        return occurrences

    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            occurrences1 = count_occurrences(strings[i])
            occurrences2 = count_occurrences(strings[j])
            if occurrences1 == occurrences2:
                anagram_count += 1
                if anagram_count > 75:
                    return False
    return True
