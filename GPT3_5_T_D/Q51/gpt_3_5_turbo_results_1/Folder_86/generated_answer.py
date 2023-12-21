
def if_contains_anagrams(strings):
    def count_frequency(string):
        frequency = [0] * 26
        for char in string.lower():
            if char.isalpha():
                index = ord(char) - ord('a')
                frequency[index] += 1
        return frequency

    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if count_frequency(strings[i]) == count_frequency(strings[j]):
                    anagram_count += 1
                    if anagram_count > 48:
                        return False

    return True
