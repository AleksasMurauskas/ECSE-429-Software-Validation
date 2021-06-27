test_input=open("input.txt","r");
mutation_list=open("mutation_list.txt","r");
"""a= 3*4
b= 5+5
c= 12/4
d= 39-5"""
operators = ["+","-","*","/"]
input_lines= test_input.read().splitlines()
input_num = len(input_lines)
test_lines =mutation_list.read().splitlines()
test_num = len(test_lines)
copy_lines=input_lines

for x in range(0,test_num):
	for y in range(0,input_num):
		copy_lines[y] =input_lines[y].encode().decode()
	active_line = test_lines[x]
	parsed_line = active_line.split()

	mutated_line = int(parsed_line[1])
	mutant = str(parsed_line[2])
	"""print("line"+ str(mutated_line)+ "mutant"+ mutant)"""
	placeholder = copy_lines[mutated_line-1]
	for oper1 in operators:
		test_line =copy_lines[mutated_line-1]
		new_line =test_line
		found =test_line.find(oper1);
		if(found != -1):
			new_line= test_line[:found] + mutant+ test_line[found+1:]
			copy_lines[mutated_line-1]= new_line
		"""Inject mutant"""
	test_file= open("test"+str(x+1)+".txt","w+")
	for line in copy_lines:
		test_file.write(line+"\n")
	copy_lines[mutated_line-1] = placeholder
