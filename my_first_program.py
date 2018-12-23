from random import randint

print("Hello World")
print("Elouan")
print("Mayeul")
print("Neil")
print("Sterenn")
print("Guillaume")
print("lord of the rings")
print("program")

ring_dark = "\nSauron\n"
print(ring_dark)

a = 1000
b = 52
c = a + b
d = a * b

print(c)
print(d)

my_score = 1000
message = "\nI score %s points"
print(message % my_score)

for _ in range(10):
    my_score = randint(1, 1000)
    print(message % my_score)


famille = ["Guillaume", "Sterenn", "Elouan", "Mayeul", "Neil", "Gandalf"]
print(famille)
print(len(famille))
print("\n")

for i in range(10):
    print(i)
    a = randint(0, len(famille) - 1)
    b = randint(0, len(famille) - 1)
    print(famille[a] + " aime " + famille[b])
