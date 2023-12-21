
def if_contains_anagrams(strings):
    def count_letters(string):
        letter_count = [0] * 26
        for char in string:
            if char.isalpha():
                char = char.lower()
                index = ord(char) - ord('a')
                letter_count[index] += 1
        return tuple(letter_count)
    
    anagrams = {}
    count = 0
    for string in strings:
        if len(string) >= 3:
            key = count_letters(string)
            if key in anagrams:
                count += anagrams[key]
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    
    return count <= 73
