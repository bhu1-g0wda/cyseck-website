s="bhuvann"
t=[]
for i in s:
    if i not in t:
        t+=i
q=""
for i in t:
   q+="".join(i)

print(q)