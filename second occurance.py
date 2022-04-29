def getIndex(listOfIntegers,NumericVariable): 
  try: listOfIntegers.remove(NumericVariable) 
    try: k=listOfIntegers.index(NumericVariable) 
      return k+1 
    except: 
      return 0
    except: 
      return 0
if __name__=="__main__": 
  l=[] n=int(input()) 
  for i in range(n): 
    a=int(input())
    l.append(a)
  num=int(input()) 
  print(getIndex(l,num))
