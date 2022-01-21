def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lst = phrase.split(' ')
    l = [i.lower().capitalize() for i in lst]
    return ' '.join(l)

print(titleize('this is awesome'))
print( titleize('oNLy cAPITALIZe fIRSt'))
