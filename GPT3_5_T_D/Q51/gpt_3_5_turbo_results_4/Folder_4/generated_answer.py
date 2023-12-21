
def if_contains_anagrams(strings):
    def count_frequency(s):
        freq = [0] * 26
        for c in s.lower():
            if c.isalpha():
                freq[ord(c) - ord('a')] += 1
        return tuple(freq)

    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if count_frequency(strings[i]) == count_frequency(strings[j]):
                count += 1
                if count > 84:
                    return False
    return True
