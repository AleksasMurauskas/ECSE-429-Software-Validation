from time import sleep
from subprocess import Popen
import os
Popen('python mutator.py')
if not os.path.exists('mutatedtests.py'):
    file=open('mutatedtests.py', 'w')
    file.close()
if not os.path.exists('mutatedtests2.py'):
    file=open('mutatedtests2.py', 'w')
    file.close()
if not os.path.exists('mutatedtests3.py'):
    file=open('mutatedtests3.py', 'w')
    file.close()
if not os.path.exists('mutatedtests4.py'):
    file=open('mutatedtests4.py', 'w')
    file.close()
sleep(2)
Popen('python mutantkiller.py')
exit()