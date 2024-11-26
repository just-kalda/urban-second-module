first, second, third = int(input()), int(input()), int(input())
if first == second and first == third and second == third:
    print(3)
elif (first == second or first == third) or (second == first or second == third) or (third == first or third == second):
    print(2)
else:
    print(0)
