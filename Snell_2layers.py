import math
import numpy as np

e1=1
e2=list(np.arange(10,50,0.1))
e3=list(np.arange(10,50,0.1))
e4=34.988

final_list=[]
# keni_list=[None,None,None]
for i in range (len(e2)):
    for j in range (len(e3)):
        n12=math.sqrt(e2[i]/e1)
        n23=math.sqrt(e3[j]/e2[i])
        n34=math.sqrt(e4/e3[j])
        n=n12*n23*n34
        final_list.append([e1,e2[i],e3[j],e4,n12,n23,n34,n])

final_list.sort(key=lambda x: x[-1].real, reverse=True)
print(final_list[0])