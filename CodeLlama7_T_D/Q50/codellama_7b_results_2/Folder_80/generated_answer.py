
def if_contains_anagrams(words):
    # Case-insensitive comparison of strings
    def compare_strings(string1, string2):
        return sorted(string1.lower()) == sorted(string2.lower())
    
    # Anagram check for three or more consecutive letters

    def is_anagram(word):
        for i in range(len(word) - 2):
            substring = word[i:i + 3]
            if len(substring) < 3:
                continue

            if compare_strings(substring, substring[::-1]):
                return True

        return False

    
    # Check for at least 19 pairs of anagrams in the given list

    def contains_anagrams(words):
        count = 0

        for word in words:

            if is_anagram(word):

                count += 1

                if count >= 19:

                    return True

        return False
