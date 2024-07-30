# to draw star pattern


def star_pattern():
    n = int(input("Enter the row till you want pattern: "))
    for i in range(0,n+1):
        for j in range(0, i):
            print("* ", end=" ")
        print()

star_pattern()