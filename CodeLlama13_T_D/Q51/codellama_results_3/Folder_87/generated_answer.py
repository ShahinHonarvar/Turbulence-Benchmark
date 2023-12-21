
def if_contains_anagrams(my_list):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    anagram_pairs = 0
    for s1 in my_list:
        s2 = list(s1)
        for i in range(len(s2)):
            c = s2[i]
            if c.lower() in english_letters:
                s2[i] = ''
                for s3 in my_list:
                    if len(s3) >= 3 and set(s3).issubset(english_letters):
                        anagram_pairs += 1
    return anagram_pairs <= 392
