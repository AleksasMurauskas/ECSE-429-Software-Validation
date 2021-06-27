import tests
import mutatedtests, mutatedtests2, mutatedtests3, mutatedtests4
import re
from shutil import copyfile
import importlib
import time
import threading

operators = ['*','/','+','-']

def copy(mutantline,mutantfile):
    copyfile('tests.py',mutantfile)
    #faultlist = open('mutations.txt', 'r')
    data = ''

    with open('tests.py','r') as newsoftware:
        data = newsoftware.readlines()

    with open('mutations.txt', 'r') as faultlist:
        linenumber = -1
        mutateddata = ''
        for line in faultlist:
            if 'Line:' in line:
                x = re.split('Line: ',line,1)
                linenumber = int(x[1].rstrip('\n'))
            if 'New:' in line and linenumber == mutantline:
                mutateddata = (re.split('New: ',line,1))[1]
                data[linenumber-1] = mutateddata

    with open(mutantfile,'w') as newsoftware:
        newsoftware.writelines(data)

def findvector(ds):
    for i in range(1,10):
        for j in range (1,10):
            for k in range (1,10):
                for l in range (1,10):
                    for m in range (1,10):
                        correct = tests.runtests(i,j,k,l,m)
                        mutated = ds.runtests(i,j,k,l,m) 
                        if correct != mutated:
                            return [i,j,k,l,m]
    return 'Cant kill'
def killmutants(mutatetestfile,type,mutatedmodule):
    kills = []
    with open('mutations.txt', 'r') as mutations:
        linenumber = -1
        for line in mutations:
            if 'Line:' in line:
                x = re.split('Line: ',line,1)
                linenumber = int(x[1].rstrip('\n')) 
            if ('Inserted: ' + type) in line:
                copy(linenumber,mutatetestfile)
                time.sleep(.5)
                ds = importlib.import_module(mutatedmodule)
                importlib.reload(ds)
                importlib.reload(tests)
                result = findvector(ds)
                oldop = ''
                for operator in operators:
                    if operator in line and operator != type:
                        oldop = operator
                kills.append('Line: ' + str(linenumber) + ' ' + str(result) + ' mutant: ' + type + ' on ' + oldop)
    print(str(type) + ' appending ' + str(kills)+'\n')
    data.append(kills)


    # with open('mutationskilled.txt','w+') as mutationskilled:
    #     for item in kills:
    #         mutationskilled.write(item+'\n')

class myThread (threading.Thread):
   def __init__(self, mutantfile, operator,module):
      threading.Thread.__init__(self)
      self.mutantfile = mutantfile
      self.operator = operator
      self.module = module
   def run(self):
      print ("Starting " + self.name+'\n')
      killmutants(self.mutantfile,self.operator,self.module)
      print ("Exiting " + self.name+'\n')

data = []
thread1= myThread('mutatedtests.py','+','mutatedtests')
thread2 = myThread('mutatedtests2.py','-','mutatedtests2')
thread3= myThread('mutatedtests3.py','*','mutatedtests3')
thread4 = myThread('mutatedtests4.py','/','mutatedtests4')
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
with open('mutationskilled.txt','w+') as mutationskilled:
    killfailedcount = 0
    lines = 0.0
    for item in data:
        if 'Cant kill' in item:
            killfailedcount += 1
        for i in item:
            mutationskilled.write(str(i) + '\n')
            lines += 1
            if 'Cant kill' in item:
                killfailedcount += 1
    killratio = (lines - float(killfailedcount))/lines
    mutationskilled.write('Kill ratio: ' + str(killratio))