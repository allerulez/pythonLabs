#Anton Gefvert antge210, Aleksi Evansson aleev379
#3. Bearbetning av listor
#
#Uppgift 3B

"""
vikho394: OK!
Bra modulär lösning, bra uppdelning!
Ni har dock rader som är längre än 79 tecken. De bör göras radbrytningar :) 
om man ska vara petig
"""

def logic_and(logic, values):
    """ Returns "true" if the first and third value in the list is "true", else return "false" """
    if interpret(logic[0],values) == "true" and interpret(logic[2],values) == "true":
        return "true"
    else:
        return "false"


def logic_or(logic, values):
    """ Returns "true" if the first or third value in the list is "true", else return "false" """
    if interpret(logic[0],values) == "true" or interpret(logic[2],values) == "true":
        return "true"
    else:
        return "false"


def logic_not(logic, values):
    """ Returns "false" if the second value in the list is "true", else return "true" """
    if interpret(logic[1],values) == "true":
        return "false"
    else:
        return "true"


def interpret(logic, values):
    """ Returns the result of a logical operation in "logic" by comparing values in "values", in strings """
    if isinstance(logic,str):
        if logic in values:
            return values[logic]
        else:
            return logic
    elif len(logic) == 2:
        return logic_not(logic, values)
    elif logic[1] == "OR":
        return logic_or(logic, values)
    else:
        return logic_and(logic, values)


if __name__  == "__main__":

    # Tests interpret
    assert interpret(["door_open", "AND", "cat_gone"], 
                           {"door_open" : "false", "cat_gone" : "true", "cat_asleep" : "true"}) == "false"
    assert interpret(["cat_asleep", "OR", ["NOT", "cat_gone"]],
                       {"door_open" : "false", "cat_gone" : "true", "cat_asleep" : "true"}) == "true"
    assert interpret(["true", "OR", "true"], {}) == "true"
    assert interpret("cat_gone", {"door_open": "false", "cat_gone": "true"}) == "true"
    assert interpret(["NOT", ["NOT", ["NOT", ["cat_asleep", "OR", ["NOT", "cat_asleep"]]]]],
                       {"cat_asleep": "false"}) == "false"
