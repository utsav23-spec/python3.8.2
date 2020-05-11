i = input("Enter the characters:")
s = len(i)**5
print("Total passwds generated:",s)
for j in range(len(i)):
    k = 0 
    for k in range(len(i)):
        l = 0
        for l in range(len(i)):
            m = 0
            for m in range(len(i)):
                n = 0
                for n in range(len(i)):
                    p = i[j] + i[k] + i[l] + i[m] + i[n]
                    print(p)
                    n += 1
                m += 1
            l += 1
        k += 1
    j += 1
