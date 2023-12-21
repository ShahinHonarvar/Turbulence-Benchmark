
def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if ''.join(sorted(strings[i].lower())) == ''.join(sorted(strings[j].lower())):
                    count += 1
    if count <= 75:
        return True
    else:
        return False
