#addition of  two list
n1=[1,2,3,4]
n2=[5,6,7,8]
print(n1+n2)
#addition of two tuple
my_tuple=(1,2,3)
my_tuple1=(4,5,6)
print(my_tuple+my_tuple1)
#add of set
set={56,67}
set1={45,67}
print(set-set1)
#add of fs
frozenset={1,23,34}
frozenset1={23,45,67}
print(frozenset-frozenset1)
#add of dict
stud_db={}
stud_db[1]="jay"
stud_db[2]="viru"
stud_db[3]="manu"
stud_db[4]="deep"
class_db={}
class_db[1]="aardhya"
class_db[2]="yash"
#addition of different datatypes
print('stud_db'+'class_db') 
print(n1+my_tuple)
print(set+frozenset)
print(my_tuple+set)
print(True+True)