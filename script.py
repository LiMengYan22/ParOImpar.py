def esPar (a):
  if a%2==0:
        return True
    else:
        return False 
  a=int(input("\nIntroduce número:\n"))
  if(a%2==0):
        print(str(a)+"-> SI es Par.")
  else:
        print(str(a)+"-> Es IMPAR!!")
