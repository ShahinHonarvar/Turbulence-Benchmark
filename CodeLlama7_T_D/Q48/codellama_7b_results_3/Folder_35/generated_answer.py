 def return_binary_or_hexa(tuple):
    a = tuple[77]
    b = tuple[84]
    if (a + 1) == b:
        return ''

    else:

        sum = 0

        for i in range((a + 1), (b - 1)):
            if not i in tuple[(77):(85)]:
                sum += i

        if sum % 2 == 0:
            return f"{sum:#x}"

        else:

            return f"{sum:#b}"
