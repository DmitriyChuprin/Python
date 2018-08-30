"""Given a dictionary/hash/object of languages and your respective test results, return the list of languages where your test score is at least 60, in descending order of the results.

Note: There will be no duplicate values.

Examples
{"Java": 10, "Ruby": 80, "Python": 65} - -> ["Ruby", "Python"]
{"Hindi": 60, "Dutch": 93, "Greek": 71} - -> ["Dutch", "Greek", "Hindi"]
{"C++": 50, "ASM": 10, "Haskell": 20} - -> []
"""


def my_languages(results):
    # your code here
    win_list = []
    sort_list = []
    for keys, values in results.items():
        sort_list.append(values)
    sort_list.sort()
    sort_list.reverse()
    for i in sort_list:
       for keys, values in results.items():
           if values >= 60:
                if values == i:
                    if keys not in win_list:
                        win_list.append(keys)

    return win_list
