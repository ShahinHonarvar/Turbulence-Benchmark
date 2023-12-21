
def if_contains_anagrams(strings):
    def are_anagrams(str1, str2):
        count1 = [0] * 26
        count2 = [0] * 26

        for char in str1.lower():
            if char.isalpha():
                count1[ord(char) - ord('a')] += 1

        for char in str2.lower():
            if char.isalpha():
                count2[ord(char) - ord('a')] += 1

        return count1 == count2

    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and are_anagrams(strings[i], strings[j]):
                count += 1

    return count <= 188
