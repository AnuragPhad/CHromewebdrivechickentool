In="""7
3 1 1 1 6 5 4"""
p=[]
for i in In:
    if i.isdigit():
        p.append(i)

num=p[0]
arrayi=p[1:len(p)]



def sum_(ipo):
    op=0
    for i in ipo:
        op=op+int(i)
    return op

opo=sum_(arrayi)

to=int(num)

for i in range(to):
    value=int(arrayi[i])*to
    if value>opo:
        print(int(arrayi[i]))
        break
