print("A love calculater machine")
name1 = input("your name : ")
name2 = input("their name : ")
name1 = name1.lower()
name2 = name2.lower()
print(name1+name2)
a = name1.count("t")
b = name1.count("r")
e = name1.count("u")
f = name1.count("e")
g = name2.count("l")
h = name2.count("o")
i = name2.count("v")
j = name2.count("e")
print(f"T ouccrs {a} times")
print(f"R ouccrs {b} times")
print(f"U ouccrs {e} times")
print(f"E ouccrs {f} times")
print(f"L ouccrs {g} times")
print(f"O ouccrs {h} times")
print(f"V ouccrs {i} times")
print(f"E ouccrs {j} times")
k = a + b + e + f
l = g + h + i + j
print(f"your love parameter is {k}{l} % ") 