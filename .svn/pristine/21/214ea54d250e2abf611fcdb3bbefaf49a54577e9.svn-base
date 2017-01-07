#Anton Gefvert antge210, Aleksi Evansson aleev379
#4. Funktionell programmering
#Uppgift 4a

"""
vikho 20/10: Ok!
Bra lösning, inget att klaga på
"""

def powerset(lst):
	""" Returns the powerset of given list lst """
	if not lst:
		return [[]]
	next_lst = powerset(lst[1:])
	return [[lst[0]] + x for x in next_lst] + next_lst

if __name__ == "__main__":
    assert  powerset([1]) == [[1], []]
    assert powerset(["ridcully", "librarian"]) == [[], ['ridcully'], ['librarian'], ['ridcully', 'librarian']]