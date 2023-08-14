def generator():
    n = 1
    while True:
        yield n
        n += 1
        yield 66
        print()

ob = generator()

print(next(ob))
print(next(ob))
print(5555555555555555)
print(next(ob))
print(next(ob))
print(next(ob))
print(next(ob))