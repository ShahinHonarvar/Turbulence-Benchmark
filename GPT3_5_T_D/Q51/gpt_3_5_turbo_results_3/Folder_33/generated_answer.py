
def if_contains_anagrams(strings):
    def count_letters(word):
        letters = [0] * 26
        for char in word.lower():
            if 'a' <= char <= 'z':
                letters[ord(char) - ord('a')] += 1
        return tuple(letters)
    
    def get_anagrams_count(strings):
        counts = {}
        for word in strings:
            if len(word) < 3:
                continue
            letters = count_letters(word)
            if letters in counts:
                counts[letters] += 1
            else:
                counts[letters] = 1
        pairs_count = 0
        for count in counts.values():
            pairs_count += count * (count - 1) // 2
        return pairs_count
    
    return get_anagrams_count(strings) <= 85
