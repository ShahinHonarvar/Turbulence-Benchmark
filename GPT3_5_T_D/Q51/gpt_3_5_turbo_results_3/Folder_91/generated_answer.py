
def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        count = [0] * 26
        for char in str1:
            count[ord(char.lower()) - ord('a')] += 1
        for char in str2:
            count[ord(char.lower()) - ord('a')] -= 1
        return all(elem == 0 for elem in count)

    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                count += 1
                if count > 88:
                    return False
    
    return True
