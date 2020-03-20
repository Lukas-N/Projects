def bubblesort(listin):
    for i in range(len(listin)-1,0,-1):
        for j in range(i):
            if listin[j]>listin[j+1]:
                temp = listin[j]
                listin[j] = listin[j+1]
                listin[j+1] = temp

listin = [5,52,3,523,52,35,2]
bubblesort(listin)
print(listin)
