test_input=open("input.txt","r");
"""a= 3*4
b= 5+5
c= 12/4
d= 39-5"""
operators = ["+","-","*","/"]
results = open("results.txt", "w")
input_lines= test_input.read().splitlines()
lines = len(input_lines)
mutants_created = {"+":0,"-":0,"*":0,"/":0}

def create_line_output(line_num,inline,oper1,oper2):
	out1 = "Line Tested: "+ str(line_num)+"\n"
	out2 = "Original Arithmetic before mutation: "+inline+" The operator "+ oper1+ " will be replaced\n"
	out3 = "The mutant operator being inserted: "+oper2 +"\n"
	out4 = "The resulting arithmetic: "+ inline.replace(oper1,oper2) +"\n\n\n"
	retval = out1+out2+out3+out4
	return retval;

for a in range(0, lines):
	active_line =input_lines[a]
	for oper1 in operators:
		for mem in active_line:
			if oper1==mem:
				for oper2 in operators:
					if(oper2 !=oper1):
						mutants_created[oper2] =mutants_created[oper2]+1
						results.write(create_line_output(str(a),active_line,oper1,oper2))
results.write("The following line displays the total number of times each mutant type were generated: \n")
results.write(str(mutants_created))