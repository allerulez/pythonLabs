def double_elements(lst):
    return [e*2 for e in lst]


def all_pairs_ordered(n):
    return [(i,ii) for i in range(n+1) for ii in range(n+1)]


def distribute(e, lst):
    return [sub_lst + [e] for sub_lst in lst]


def choose(n,k):
    if n == k:
        return 1
    elif k == 0:
        return 1
    if k < n/2:
        k = n - k
    return n * choose(n-1,k) // (n - k)


def pascal(n):
    return [[choose(k, i) for i in range(k+1)] for k in range(n)] 


def create_lock(code,msg):
    def unlock(decode):
        if decode == code:
            return msg
        else:
            return "Fel kod!"
    return unlock


def keep_if(func, str):
    if len(str) == 0:
        return ""
    return (str[0] if func(str[0]) else "") + keep_if(func,str[1:])


def foreach(func, lst):
    return [func(e) for e in lst]


def compose(func1, func2):
    return (lambda x : func1(func2(x)))


def repeat(func, n):
    if n == 1:
        return func
    return (lambda x : func(repeat(func,n-1)(x)))


def combine(func,seq):
    if not seq[1:]:
        return seq[0]
    else:
        return func(combine(func,seq[:-1]),seq[-1])

# combine(f, [0, 1, 2, 3]) = f(f(f(0, 1), 2), 3).
# func =    lambda x, y : x + y
# x =       [1,2,3]
def repeat_fold(func, n):
    if n == 1:
        return func
    return (lambda x : combine(repeat_fold(combine(func,x), n-1),x))


if __name__ == "__main__":
    assert double_elements([1, 2, 3, 4]) == [2, 4, 6, 8]
    assert all_pairs_ordered(2) == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    assert distribute('k', [['o'], [0, 1, 2], ['o','o']]) == [['o', 'k'], [0, 1, 2, 'k'], ['o', 'o', 'k']]
    assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
