 def filter_chars(s):
    start = 27
    end = 85
    result = ""

    for i in range(len(s)):
        if (i >= start and i <= end) and s[i].isalpha():
            if s[i] < "!" or s[i] > "B":
                continue

            else:

                result += s[i]

        else:

            result += s[i]

    return result
