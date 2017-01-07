#Anton Gefvert antge210, Aleksi Evansson aleev379
#6. Algoritmer
#Uppgift 6b
"""
vikho 11/30: Ok
Bra lösning, det enda som jag skulle göra annorlunda är att förenkla basfallet
något:

if len(seq) == 1:
    return seq
elif not seq:
    return []

är ekvivalent med:

if not seq or not seq[1:]:
    return seq

vilket gör koden lite kortare.
Det andra som jag skulle anmäkra på är att era val av varibelnamn är lite sisådär
i, left och right bör ha mer självdokumenterande namn så som elem, lesser och
greater_equal.

"""



def quicksort(seq):
"""
Sorts a list of values by arranging them to the left or right of a pivot value;
to the left if they're smaller and to the right if they're greater. 
This is then repeated for both sides until there is only a single value to compare.  
"""
    if len(seq) == 1:
        return seq
    elif not seq:
        return []
    pivot = seq[0]
    left = []
    right = []
    for i in seq[1:]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    return quicksort(left) + [pivot] +quicksort(right)

if __name__ == "__main__":
    assert quicksort([45, 17, 39]) == [17, 39, 45]
    assert quicksort([26, 4, 18, 27, 6, 4, 12]) == [4, 4, 6, 12, 18, 26, 27]

