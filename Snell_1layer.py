import math
import numpy as np # type: ignore

e1=1
e2=list(np.arange(10,50,0.1))
e3=34.988

final_list=[]
# keni_list=[None,None,None]
for i in range (len(e2)):

    n12=math.sqrt(e2[i]/e1)
    n23=math.sqrt(e3/e2[i])

    n=n12*n23
    final_list.append([e1,e2[i],e3,n12,n23,n])

final_list.sort(key=lambda x: x[-1].real, reverse=True)
print(final_list[0])