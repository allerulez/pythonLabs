#Anton Gefvert antge210, Aleksi Evansson aleev379
#6. Algoritmer
#Uppgift 6a
def match(seq, pattern):
    """ 
    Checks wether the given sequence matches the given pattern 
    Added functionality handles nestled list
    """
    if not pattern:
        return not seq
    elif pattern[0] == '--':
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)
    elif not seq: 
        return False 
    elif isinstance(pattern[0], list) or isinstance(seq[0],list):
        return match(seq[0],pattern[0]) and match(seq[1:],pattern[1:])
    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])
    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])
    else:
        return False
