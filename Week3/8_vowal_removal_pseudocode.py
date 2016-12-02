VOWEL_REMOVAL(s)
    if length[s] <= 1
        return s
    elif s[0] is in "aeiouAEIOU"
        return VOWEL_REMOVAL(s[1:])
    
    return s[0] + VOWEL_REMOVAL(s[1:])
