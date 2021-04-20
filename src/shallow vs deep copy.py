#shallow copy
import copy
l1=[10,20,[30,40],50]
l2=copy.copy(l1)
l1[0]=888
l1[2][0]=999
l2[3]=123
print('L1:',l1)
print('L2:',l2)
#Deep copy
l1=[10,20,[30,40],50]
l2=copy.deepcopy(l1)
l1[0]=888
l1[2][0]=999
l2[3]=123
l2[2][1]=77
print('L1:',l1)
print('L2:',l2)