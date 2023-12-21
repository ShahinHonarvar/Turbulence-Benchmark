def lists_with_product_equal_n(s):
    res = []
    for i in range(len(s)):
        cnt = 0
        for j in range(i, len(s)):
            if s[i] * s[j] == -3:
                cnt += 1
            if cnt == j - i + 1:
                res.append(s[i:j+1])
                break
    return res
