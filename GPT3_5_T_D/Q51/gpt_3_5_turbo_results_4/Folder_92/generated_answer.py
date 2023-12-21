
def if_contains_anagrams(strings):
    def count_letters(string):
        counts = [0] * 26
        for char in string:
            if 'a' <= char <= 'z':
                counts[ord(char) - ord('a')] += 1
        return counts

    def are_anagrams(string1, string2):
        counts1 = count_letters(string1.lower())
        counts2 = count_letters(string2.lower())
        return counts1 == counts2

    pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and are_anagrams(strings[i], strings[j]):
                pairs += 1

    return pairs <= 34
