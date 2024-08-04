def all_variants(text: str):
    x = len(text) + 1
    for i in range(1, x):
        for j in range(x - i):
            yield text[j:j + i]


a = all_variants("abc")
for i in a:
    print(i)
