print("Anem a fer que mos digues 10 numeros")
c_num=0 
sumanum=0
positius= 0
while True:
    numeros=int(input("Dis-me numeros hasta que arribem a 10: "))
  

    if numeros ==0:
        print ("Hem dit que volem numeros positius o negatius")
        continue 
   
    if numeros >0:
        sumanum+=numeros 
        positius+=1
    c_num+=1 
    if c_num==10:
         break


if sumanum >0:
    print ("La mitja dels 10 numeros es",sumanum/positius )
else:
    print ("No podem fer la mitja de negatius")

