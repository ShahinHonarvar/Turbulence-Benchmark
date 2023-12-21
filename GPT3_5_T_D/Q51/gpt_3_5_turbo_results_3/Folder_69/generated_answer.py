
def if_contains_anagrams(arr):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    pairs = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if len(arr[i]) < 3 or len(arr[j]) < 3:
                continue
            if is_anagram(arr[i], arr[j]):
                pairs += 1
                if pairs > 58:
                    return False

    return True
