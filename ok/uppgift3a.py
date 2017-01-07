#Anton Gefvert antge210, Aleksi Evansson aleev379
#3. Bearbetning av listor
#Uppgift 3A

"""
vikho394: OK!
Enkelt och bra. Inga konstigheter. Ni har dock docstrings som är längre än 79
tecken. De bör göras radbrytningar :) om man ska vara petig
"""

def split_it(string):
    """ 
    Given a string, returns two new strings, where the first contains all lowercase letters, "." and "_"
    and the second contains all uppercase letters, " " and "|", iteratively 
    """
    ret_str1 = ""
    ret_str2 = ""
    for char in string:
        if char.islower() or char in "_.":
            ret_str1 += char
        elif char.isupper() or char in " |":
            ret_str2 += char
    return ret_str1, ret_str2


def split_rec(string):
    """
    Given a string, returns two new strings, where the first contains all lowercase letters, "." and "_"
    and the second contains all uppercase letters, " " and "|", recursively
    """
    if not string:
        return "",""
    left,right = split_rec(string[1:])
    if string[0].islower() or string[0] in "_.":
        return string[0] + left, right
    elif string[0].isupper() or string[0] in " |":
        return left, string[0] + right
    return left, right
