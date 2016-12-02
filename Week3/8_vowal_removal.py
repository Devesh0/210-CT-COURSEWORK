def vowel_removal(s):
    if (len(s) <= 1): # base case
        return s
    elif s[0] in "aeiouAEIOU": 
        return vowel_removal(s[1:]) 
    return s[0] + vowel_removal(s[1:])

print(vowel_removal("beautiful"))

