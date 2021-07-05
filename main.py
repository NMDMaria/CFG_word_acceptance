# citire CFG
fin = open("date.in", 'r')

G = [] # limbajul citit

# nrV = int(fin.readline())
aux = fin.readline()
V = [item for item in aux.split()]
aux = fin.readline()
T = [item for item in aux.split()]
nrP = int(fin.readline())
P = {}
for i in range(nrP):
    rule = fin.readline().strip()
    leftside = rule.split('=')[0]
    if leftside not in P:
        P.update({leftside: []})
    right_side = rule.split('=')[1].split('|')
    for item in right_side:
        P[leftside].append(item)
S = fin.readline().strip()

flip = {}
for item in P:
    for rule in P[item]:
        if rule not in flip:
            flip.update({rule: [item]})
        else:
            flip[rule].append(item)


word = fin.readline()
L = len(word)

table = []
for k in range(L, 0, -1):
    table.append([[] for i in range(k)])
for i in range(L):
    if word[i] in flip:
        table[0][i] = flip[word[i]]

for i in range(1, L):
    for j in range(L - i):
        k = 0
        fs = [0, 0]
        sc = [0, 0]
        while k <= i:
            if fs[0] >= i or sc[0] < 0 or sc[1] >= L:
                break
            if fs == [0, 0] and sc == [0, 0]:
                fs[0] = 0
                fs[1] = j
                sc[0] = i - 1
                sc[1] = j + 1

            for m in table[fs[0]][fs[1]]:
                for n in table[sc[0]][sc[1]]:
                    rule = m + n
                    if rule in flip:
                        for z in flip[rule]:
                            table[i][j].append(z)

            fs[0] += 1
            sc[0] -= 1
            sc[1] += 1
            k += 1
# print(*table, sep ="\n")
fout = open("date.out", "w")
if S in table[L - 1][0]:
    fout.write("accepted")
else: fout.write("not accepted")


