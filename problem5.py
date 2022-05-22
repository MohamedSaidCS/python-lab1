vowels = ['a', 'e', 'i', 'o', 'u']


def remove_vowels(string):
    for vowel in vowels:
        string = string.lower().replace(vowel, '')

    return string


print(remove_vowels('mobile'))
