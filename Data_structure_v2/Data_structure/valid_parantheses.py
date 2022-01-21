def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    lst = list(parens)
    parantheses =[]
    res=[]
    
    if len(lst)%2!=0:
        return False
    elif len(lst) ==2:
        return lst[0]=='(' and lst[1]==')'
    else:
        for i in range(int(len(lst)/2)):
            parantheses.append([lst[i],lst[-1-i]])        
        
        for i in range(len(parantheses)):
            if i != len(parantheses)-1:
                res.append(parantheses[i][0]=='(' and parantheses[i][1]==')')
            else:
                res.append(parantheses[i][0]==')' and parantheses[i][1]=='(')
        if False in res:
            return False
        else:
            return True

        
                            

    
    
print(valid_parentheses("()"))
print(valid_parentheses("()()"))
print(valid_parentheses("(()())"))
print(valid_parentheses(")()"))
print(valid_parentheses("())"))
print(valid_parentheses("((())"))
print(valid_parentheses(")()("))
