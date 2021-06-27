code_under_test=open("tests.py","r")

"""a=1+3
b= a*2
c= b/2
d= c-1"""
f= open("mutations.txt","w+")
lines=code_under_test.read().splitlines()
operations=["+","-","*","/"]
dict= {"+":0,"-":0,"*":0,"/":0}


#creates a string with all the info about the mutation made and updates the mutation count
def createmutantinfo(line,original,inserted,new,originalop):
    info = 'Line: ' + str(line) + '\n'
    info += 'Original: ' + original + '\n'
    info += 'Inserted: ' + inserted + ' on ' + originalop + '\n'
    info += 'New: ' + new + '\n'
    #numbers[inserted] += 1
    return info
    
def convert_op(operation):
    if operation=="/":
        return "div_"
    return operation
    
for i in range (2,len(lines)):
    line= lines[i]
    for op in operations:
        for j in range (0,len(line)): 
            char=line[j];
            if op==char:
                for new_op in [y for y in operations if y!=op ]: #all operations except the one we were looking for 
                    newline=line[0:j]+new_op+line[j+1:]
                    infostring = createmutantinfo(i+1, line, new_op, newline,op)
                    f.write(infostring + '\n')
                    dict[new_op]=dict[new_op]+1# count the number of mutants of each type generated by the program
                    
f.write('\n Number of each created: \n')
#f.write("4. Total number of mutants of each type generated by your program: \n")
#f.write(str(dict))
for key in dict:
    f.write(key + ': ' + str(dict[key]) + '\n')
    
f.close()
            
