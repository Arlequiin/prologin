with open("sample-input.txt") as f:
    content=f.readlines()#remove first char in case of the presence of a digit, like 3 or 4 before the pas-malin-dromes
    for i in range(len(content)):
        content[i]=(content[i].replace("\n",""))
    amount=0
    for element in content:
      if len(element)>1000:
        pass
      else:
        lowercases=[]
        uppercases=[]
        digits=[]
        for char in element:
            if char.isdigit():
                digits.append(char)
            elif char.isupper():
                uppercases.append(char)
            else:
                if char!=' ':
                 lowercases.append(char)
        #if 0 not in [len(lowercases),len(uppercases),len(digits)]:
        if lowercases[::-1]==lowercases and uppercases[::-1]==uppercases and digits[::-1]==digits and len(element)!=1:
            #print(element)
            amount+=1
        else:
            #print(uppercases,lowercases,digits)
            pass
print(amount)