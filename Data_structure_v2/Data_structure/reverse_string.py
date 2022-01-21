def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    text = list(phrase)
    text.reverse()
    return ''.join(text)
            
print(reverse_string('awesome'))
print( reverse_string('sauce'))
