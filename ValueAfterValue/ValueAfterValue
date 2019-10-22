z = int(input("Enter number of Integers:"));
n = int(input("Enter Value to Duplicate:"));
x = list(map(int, input("\n Enter the Integers: ").strip().split()))[:z]
print("Original List: ", x)

i = 0;
while (i < z):
    if (x[i]==n):
        x.insert(i+1, n)
        del x[len(x)-1]
        i += 2
    else:
        i += 1

print("New List: ", x)
