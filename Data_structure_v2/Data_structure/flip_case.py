def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    text =''
    for i in phrase:
        if i==to_swap and i.isupper():
            text = text+i.lower()
        elif i==to_swap.lower():
            text=text+i.upper()
        elif i==to_swap.upper():
            text = text+ i.lower()
        elif  i==to_swap and i.islower():
            text = text +i.upper()
        else:
            text +=i
    return text

print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))


