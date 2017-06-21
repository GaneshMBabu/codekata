my_char = input("Enter a Char to check")
the_vowel = "aeiou"

if my_char[0].lower() in the_vowel:
    print('Given Char is a vowel')
else:
    print('Given Char is Not vowel')
