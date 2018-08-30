def is_isogram(string):
    string = string.lower()
    for i in range(0, len(string)):
        for k in range(i+1, len(string)):
            if string[k] == string[i]:
                return False
    return True


print(is_isogram("aba"))