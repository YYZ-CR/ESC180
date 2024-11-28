'''f = open('data2.txt')
text = f.read()'''

def dict_to_str(d:dict):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other.
    For example, dict_to_str({1:2, 5:6}) should return "1, 2\n5, 6".
    (the order of the key-value pairs doesn’t matter and can be different
    every time).
    """
    pairs = ''
    for i in range(len(d)):
            pairs += f'{list(d.keys())[i]}, {d[list(d.keys())[i]]}\n'
    return pairs

def dict_to_str_sorted(d:dict):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other, and are sorted in
    ascending order by key.
    For example, dict_to_str_sorted({1:2, 0:3, 10:5}) should
    return "0, 3\n1, 2\n10, 5". The keys in the string must be sorted in ascending order."""
    key_values = sorted(d.keys())
    pairs = ''
    for i in key_values:
            pairs += f'{i}, {d[i]}\n'
    return pairs

def problem_six():
    text = open('Lab_08/textfiletest.txt', encoding='latin-1').read().split()
    wordcounts = {}
    for i in text:
        if i in wordcounts:
            wordcounts[i] += 1
        else: 
            wordcounts[i] = 1
    print(wordcounts)
    print(top10words(wordcounts))

def top10(L):
    return sorted(L,reverse=True)[:10]

def top10words(L):
    return sorted(list(L.items()), reverse=True, key=lambda x: x[1])[:10]

import urllib.request
def question8():
    f = urllib.request.urlopen("http://www.cs.toronto.edu/~guerzhoy/180/hi.html")
    page = f.read().decode("utf-8")
    f.close()
    print(page)
    choose_variant(["top ranked school uoft", "top ranked school waterloo"])

def choose_variant(variants):
    for i in variants:
        f = urllib.request.urlopen(f'https://ca.search.yahoo.com/search?p={urllib.parse.quote(i)}')
        lines = f.read().decode("utf-8").split('\n')
        search_results = ''
        for j in lines:
            if 'search results' in j:
                start = j.find('About ')
                end = j.find(' search results')
                search_results = j[start+6:end]
        print(f'{i}: {search_results}')


def main():
    value = dict_to_str({'a': 1, 'b': 2})
    print(value)
    value = dict_to_str_sorted({1:2, 0:3, 10:5})
    print(value)
    problem_six()
    import random
    numbers = [random.randint(1,100) for i in range(100)]
    print(top10(numbers))
    inv_freq = {6: "the", 12: "a", 1:"hi"}
    print(sorted(inv_freq.items()))
    question8()


if __name__ == '__main__':
    main()
                

