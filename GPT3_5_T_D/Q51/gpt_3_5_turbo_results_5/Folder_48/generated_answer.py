
def if_contains_anagrams(strings):
    def is_anagram(str1, str2):
        if len(str1) != len(str2):
            return False
        str1 = str1.lower()
        str2 = str2.lower()
        
        count = [0] * 26
        for char in str1:
            if char.isalpha():
                count[ord(char) - ord('a')] += 1

        for char in str2:
            if char.isalpha():
                count[ord(char) - ord('a')] -= 1
                if count[ord(char) - ord('a')] < 0:
                    return False

        return True

    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count > 277:
                    return False

    return True
