n = int(input("Enter Number of Instances: "))
c = 0
while(1):
    p = list(map(int, input("Enter Number of Elements in List & Sub-Array Sum: ").strip().split()))[:2]
    x = list(map(int, input("Enter Elements: ").strip().split()))[:p[0]]
    s = p[1]
    z = p[0]
    for i in range(0, z-1, 1):
        y = 0;
        for j in range(i, z-1, 1):
            y += x[j]
            if (y==s):
                print("({},{})".format(i,j))
                break;
    c += 1
    if (c == n):
        break;

