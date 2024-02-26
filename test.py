
def sum(a, b):
    return a + b


dct = {
    'x': 4,
    'b': 5
}

print(
    sum(**dct)
)