'''Task
Given a string,S , of length N that is indexed from 0 to N-1 , print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).
Sample Input
2
Hacker
Rank

Sample Output
Hce akr
Rn ak'''

N = int(input())
even = []
odd = []
for ind in range(0, N):
    S = input()
    even.clear()
    odd.clear()
    for item, char in enumerate(S):
        if item % 2 == 0:
            even.append(char)
        else:
            odd.append(char)
    print(''.join(even), ''.join(odd))

"""
#     even = s[::2]
#     odd = s[1::2]
#     *:It unpacks container data types like lists, sets, etc. and prints every member at once in order, with whatever separator you set.
for i in range(int(input())):
     s=input(); 
     print(*["".join(s[::2]),"".join(s[1::2])])"""
