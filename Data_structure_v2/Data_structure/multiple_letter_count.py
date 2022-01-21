def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    result ={}
    result = {i:phrase.count(i) for i in phrase if i not in result}
    return result
print( multiple_letter_count('yay'))
print( multiple_letter_count('Yay'))
