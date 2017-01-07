#Anton Gefvert antge210, Aleksi Evansson aleev379
#4. Funktionell programmering
#Uppgift 4d

"""
vikho 6/11: Ok!
Ser bra ut, ni har korrekterat felen och snyggat upp koden överlag.
"""

# Given tree functions --- Start
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
# Given tree functions --- End


def key(lst):
	"""Returns the key of an tree"""
	return lst if is_leaf(lst) else lst[1]

#Predefined functions for traverse asserts --- Start
def empty_tree_fn():
	return 0 


def leaf_fn(key): 
	return key**2 


def inner_node_fn(key, left_value, right_value): 
	return key+left_value
#Predefined functions for traverse asserts --- End


def traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn):
	"""Traverses through a tree and calls corresponding given functions"""
	if is_empty_tree(tree):
		return empty_tree_fn()
	elif is_leaf(tree):
		return leaf_fn(tree)
	return inner_node_fn(key(tree),
		traverse(left_subtree(tree),inner_node_fn,leaf_fn,empty_tree_fn),
		traverse(right_subtree(tree),inner_node_fn,leaf_fn,empty_tree_fn))


def contains_key(try_key, tree):
	"""Checks if a tree contains the key 'try_key'"""
	empty_tree_fn = lambda : False
	leaf_fn = lambda key : key == try_key
	inner_node_fn = lambda key, left_value, right_value : left_value or right_value or leaf_fn(key)
	return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)


def tree_size(tree):
	"""Returns the amount of leaves in a tree"""
	empty_tree_fn = lambda : 0
	leaf_fn = lambda key : 1
	inner_node_fn = lambda key,left_value,right_value : left_value + right_value + leaf_fn(key)
	return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)


def tree_depth(tree):
	"""Return the amount of levels in a tree"""
	empty_tree_fn = lambda : 0
	leaf_fn = lambda key : 1
	inner_node_fn = lambda key, left_value, right_value : max(1 + left_value, 1 + right_value)
	return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)



if __name__  == "__main__":

    assert traverse([6, 7, 8], inner_node_fn, leaf_fn, empty_tree_fn) == 43
    assert contains_key(6, [6, 7, 8])
    assert contains_key(2, [6, 7, [[2, 3, 4], 0, []]])
    assert not contains_key(2, [[], 1, 5]) 
    assert contains_key(5, [1,5,8])
    assert tree_size([2, 7, []]) == 2
    assert tree_size([]) == 0
    assert tree_size([[1, 2, []], 4, [[], 5, 6]]) == 5
    assert tree_depth(9) == 1
    assert tree_depth([1, 5, [10, 7, 14]]) == 3
    assert tree_depth([[1,2,3],4,5]) == 3
    assert tree_depth([]) == 0