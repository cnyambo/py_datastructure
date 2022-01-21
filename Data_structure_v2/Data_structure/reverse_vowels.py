def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    ind = []
    t = list(s)
    for i in range(len(s)):
        if s[i].lower() in 'aeiou':
            ind.append(i) 
      
    for i in range(int(len(ind)/2)):
        temp = t[ind[i]]
        t[ind[i]] = t[ind[-1-i]]
        t[ind[-1-i]] = temp
    return ''.join(t)
        
print(reverse_vowels("Hello!"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))
print( reverse_vowels("why try, shy fly?"))
