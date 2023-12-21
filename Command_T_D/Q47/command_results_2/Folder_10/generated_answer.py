def palindromes_of_specific_lengths(text):
    return set(
        "".join(
            list(
                str(i).lower()
                for i in range(16, 40)
                if str(i).lower() in str(i).lower()
            )
        )
        for i in range(16, 60)
        if str(i).lower() in str(i).lower()
    )
