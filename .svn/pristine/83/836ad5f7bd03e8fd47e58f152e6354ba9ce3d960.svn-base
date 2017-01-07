#Anton Gefvert antge210, Aleksi Evansson aleev379
#6. Algoritmer
#Uppgift 6a


"""
vikho 11/20: Ok 
Ser bra ut, inget att anmärka på.
"""


"""
Det vi tänkte var att när vi går in i en lista i sekvensen,
så måste vi också gå in i motsvarande lista i pattern,
förutsatt att vi ej har '--'
"""

from match import *
from books import *

def search(pattern, db):
    """ 
    Searches trough a database with given pattern
    and returns a list of matching entries
    """
    retSeq = []
    for entry in db:
        if match(entry, pattern):
            retSeq.append(entry)
    return retSeq 


if __name__ == "__main__":

    assert search([['författare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['år', '&']], db) == [[['författare', ['john', 'zelle']], ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']], ['år', 2010]], [['författare', ['john', 'zelle']], ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']], ['år', 2009]]]
    assert search(['--', ['år', 2042], '--'], db) == []
    assert search(['--', ['titel', ['&', '&']], '--'], db) == [[['författare', ['armen', 'asratian']], ['titel', ['diskret', 'matematik']], ['år', 2012]]]
