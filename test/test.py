"""
theAccountingGame testing file
	@randybrown
"""

class theRoles(object):
        def __init__(self,*args):
            print("Testing class Roles 1")
            print("type(args)",type(args))
            print("args: ",args)
            self.stuff = args
            print("__init__ end \n")
            
        def printRoles(self,*args):    
            print("loop start")
            for i,role in enumerate(args):            
                print(i,role)
            print("self.stuff: ",self.stuff)
            print("printRoles end \n")

    
class theSheet(theRoles):
        def __init__(self,*args):
            print("Testing class Sheet 1")
            print("__init__ end \n")
        def printSheet(self,*args):
            for i,role in enumerate(args):            
                print(i,role)

if __name__=="__main__":

    ir=theRoles().__init__("aaa","bbb")
    r=theRoles().printRoles("aaa","bbb")

    b=theSheet().printSheet("ccc","ddd")


"""
The result
================

Testing class Roles 1
type(args) <class 'tuple'>
args:  ()
__init__ end 

Testing class Roles 1
type(args) <class 'tuple'>
args:  ('aaa', 'bbb')
__init__ end 

Testing class Roles 1
type(args) <class 'tuple'>
args:  ()
__init__ end 

loop start
0 aaa
1 bbb
self.stuff:  ()
printRoles end 

Testing class Sheet 1
__init__ end 

0 ccc
1 ddd

==============
"""



