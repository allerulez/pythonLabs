def show_wordlist(num):
    for e in num:
        print(e, "-", num[e])

def all_pairs(lst):
    retlst=[]
    for e in lst:
        for ee in lst:
            retlst.append((e,ee))
    return retlst

def unordered_pairs(lst):
    retlst=[]
    for e in lst:
        for ee in lst:
            if ee >= e:
                retlst.append((e,ee))
    return retlst

def distribute(c, lst):
    retlst = lst
    for e in retlst:
        e.append(c)
    return retlst
    
def extend_each(c, lst):
    for e in lst:
        e.append(c)

def push_strings(lst):
    retlst = []
    temp = 0
    for e in lst:
        if isinstance(e,str):
            retlst.append(temp)
            temp = e
        else:
            retlst.append(e)
    return retlst


def push_stringsi(lst):
    retlst = []
    temp = 0
    for i in range(len(lst)):
        if isinstance(lst[i],str):
            retlst.append(temp)
            temp = lst[i]
        else:
            retlst.append(lst[i])
    return retlst

def sum_all_numbers(lst):
    if not lst:
        return 0
    if isinstance(lst[0], list):
        return sum_all_numbers(lst[0]) + sum_all_numbers(lst[1:])
    elif isinstance(lst[0], int):
        return lst[0] + sum_all_numbers(lst[1:])
    return sum_all_numbers(lst[1:])

def exists(c, lst):
    if not lst:
        return False
    if lst[0] == c:
        return True
    elif isinstance(lst[0], list):
        inner = exists(c,lst[0])
        return inner if inner else exists(c,lst[1:])
    else:
        return exists(c,lst[1:])

def without_vowels(lst):
    if not lst:
        return []
    if isinstance(lst[0], list):
        return [without_vowels(lst[0])] + without_vowels(lst[1:])
    elif lst[0].lower() in "aeiyou":
        return without_vowels(lst[1:])
    else:
        return [lst[0]] + without_vowels(lst[1:])

# encoding: iso-8859-1

# TDDD73 Lab 3, binary tree

def is_empty_tree(tree):
    return isinstance(tree, list) and not tree

def is_leaf(tree):
    return isinstance(tree, int)

def create_tree(left_tree, key, right_tree):
    return [left_tree, key, right_tree]
    
def left_subtree(tree):
    return tree[0]

def right_subtree(tree):
    return tree[2]

def key(lst):
    return lst if is_leaf(lst) else lst[1]

def is_treelike(tree):
    if isinstance(tree,list):
        return len(tree) in [3,0]
    return is_leaf(tree)

def is_proper_tree(tree):
    if not is_treelike(tree):
        return False
    if len(tree) != 0:
        if not is_leaf(key(tree)):
            return False
        elif isinstance(left_subtree(tree),list):
            return is_proper_tree(left_subtree(tree))
        elif isinstance(right_subtree(tree),list):
            return is_proper_tree(right_subtree(tree))
    return True

def exists_in_tree(i,tree):
    if key(tree) == i:
        return True
    if is_treelike(tree) and not isinstance(tree,int):
        if key(tree) > i:
            return exists_in_tree(i, left_subtree(tree))
        elif key(tree) < i:
            return exists_in_tree(i, right_subtree(tree))
    return False

def insert(i,tree):
    if not tree and isinstance(tree,list):
        return i
    elif is_leaf(tree):
        if key(tree) > i:
            return create_tree(i,key(tree),[])
        elif key(tree) < i:
            return create_tree([],key(tree),i)
    elif is_treelike(tree):
        if key(tree) > i:
            return create_tree(insert(i,left_subtree(tree)),key(tree),right_subtree(tree))
        elif key(tree) < i:
            return create_tree(left_subtree(tree),key(tree),insert(i,right_subtree(tree)))
if __name__  == "__main__":



    # Tests is_treelike
    assert is_treelike([])
    assert is_treelike(42)
    assert not is_treelike([42, 3]) 
    assert is_treelike([1, 2, ['fel','data']])
    assert is_treelike([[1, 3, []], 5, 6])
    # Tests is_proper_tree
    assert is_proper_tree([])
    assert is_proper_tree([[1, 3, []], 5, 6])
    assert not is_proper_tree([[[]], 5, 6])
    # Tests exists_in_tree
    assert exists_in_tree(6, [[1, 3,[]], 5, [6, 7, 8] ])
    assert not exists_in_tree(666, [[1, 3,[]], 5, [6, 7, 8] ])
    assert exists_in_tree(7, [[1, 3,[]], 5, [6, 7, 8] ])
