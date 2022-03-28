d2b = lambda x : list(map(int, bin(x).__str__()[2:]))[-8:]

print(d2b(2138))