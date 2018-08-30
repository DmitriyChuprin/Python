def solution(string, ending):
    # your code here...
    end_len = len(ending)
    li = list(string)
    k = len(li) - end_len
    if ending == ''.join(li[k:]):
        return True
    else:
        return False