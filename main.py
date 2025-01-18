#program to print numbers from 1 to 10
#recursive function that will print numbers till we reach 10
def print1to10(n):
    #base case to stop the recursion
    if n>10:
        return
    print(n)
    print1to10(n+1)
print1to10(1)