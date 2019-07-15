def list_sort_int(ls):
  c=[]
  for x in ls:
      if x.isdigit() or x[0]=='-':
          c.append(int(x))
  res = sorted(c)
  return res
num=(list_sort_int(['1','3','5','-4','abc','22','23','abc123']))
print(num)
