
import matplotlib.pyplot as mp
import numpy as np
#1-AA TYPE
#2-AS TYPE
def birthRate(pop):#birthrate depedent of the current pop
                brc=0.016949    #birth rate constant
                cc=100000#carrying capacity       
                return brc*(1-(pop/cc))

#Human pop 
hpop=20000
#fraction of people affected from malaria
infectedratefraction=0.25
#fraction of individual
w=[0.8,0.16,0.04]
w_Copy=[0.8,0.16,0.04]
# #uip: number of UNINFECTED people
uip=[ hpop*(1- infectedratefraction)*( w[0]), hpop*(1- infectedratefraction)*( w[1]), hpop*(1- infectedratefraction)*( w[2])]#S1,S2
# #ip:NUMBER of INFECTED people
ip=[ hpop* infectedratefraction*( w[0]), hpop* infectedratefraction* w[1], hpop* infectedratefraction* w[2]]#I1,I2
#natural MORTALITY  RATE
kill=0.00189
#v: Extra mortality due to sickle cell gene complications.
v=0.00003
#Number of mosquitoes:
m=10000
#scale down var
E=1
#mosquito mortality rate
moskill=0.0007
#freqency of S gene     
# S=0.2
#frequency of A gene
# A=1-S
#fractions of the new born individuals of TYPE AA
P1=( w[0]+ w[1]/2)**2
#fractions of the new born individuals of TYPE AS
P2=( w[0]+ w[1]/2)*( w[1]+ w[2]/2)

#fractions of the new born individuals of TYPE SS
P3=(( w[1]/2)+ w[2])**2
P3_copy=(( w[1]/2)+ w[2])**2
#years./time
years=3000
#fraction of mosquitoes with plasmodium parasite
fm=0.1
#number of infected mosquitoes
Im= m* fm
#probablity of acquiring plasmodium parasite
mpp=[0.05,0.09,0.14]

#probablity of acquiring plasmodium per bite
ppb=[0.05,0.06,0.08]
#addtional mortality rate due to malaria
mkill=[0.0001,0.00005,0.000001]
#biting rate
b=0.2
#recovery rate 
rr=[0.033,0.066,0.099]


arr=[]
Lambda=[]   
S1=[ uip[0]]
S2=[ uip[1]]  
S3=[ uip[2]]  
I1=[ ip[0]]
I2=[ ip[1]]
I3=[ ip[2]]

# print( w[0]," ", w_Copy[2])
y=[(I1[0]/ hpop),(I2[0]/ hpop),(I3[0]/ hpop)]
for x in range(0, years):
        arr.append( hpop)
        h= hpop
        # print(h," ",h)
        # if (w[0]+w[1]+w[2]==1):
        print("yes",x,w[0]+w[1]+w[2])
        Lambda=[ b* ppb[0]* Im/h, b* ppb[1]* Im/h, b* ppb[2]* Im/h]
        P1=( w[0]+ w[1]/2)**2
        P2=( w[0]+ w[1]/2)*( w[1]+ w[2]/2)
        P3=(( w[1]/2)+ w[2])**2
        roc_S1=(( P1)*( birthRate(h))*h)- kill*(S1[-1])-(Lambda[0])*(S1[-1])+( rr[0])*(I1[(-1)])
        roc_S2=(( P2)*( birthRate(h))*h)-( kill+ v)*(S2[-1])-(Lambda[1])*(S2[-1])+( rr[1])*(I2[(-1)])
        roc_S3=(( P3)*( birthRate(h))*h)-( kill+ v*10)*(S3[-1])-(Lambda[2])*(S3[-1])+( rr[2])*(I3[(-1)])

        roc_I1=(Lambda[0])*(S1[-1])-( kill+ rr[0]+ mkill[0])*(I1[(-1)])
        roc_I2=(Lambda[1])*(S2[-1])-(( kill+ v)+ rr[1]+ mkill[1])*(I2[(-1)])
        roc_I3=(Lambda[2])*(S3[-1])-(( kill+ v*5)+ rr[1]+ mkill[2])*(I3[(-1)])
        S1.append(round(roc_S1+S1[-1]))
        S2.append(round(roc_S2+S2[-1]))
        S3.append(round(roc_S3+S3[-1]))
        I1.append(round(roc_I1+I1[-1]))
        I2.append(round(roc_I2+I2[-1]))
        I3.append(round(roc_I3+I3[-1])) 
        w.clear()
        w=[(S1[-1]+I1[-1])/h,(S2[-1]+I2[-1])/h,(S3[-1]+I3[-1])/h]
        
        roc_fm=(1- fm)*( b* mpp[0]*y[0]+ b* mpp[1]*y[1]+ b* mpp[2]*y[2])- fm* moskill
        Im= m* fm       

        roc_pop_DE=roc_I1+roc_I2+roc_S1+roc_S2+roc_I3+roc_S3
        hpop+=roc_pop_DE

# arr.append( hpop)

ypoints = arr
xpoints = list(range(0, years))
# mp.subplot(1,1,1)
# print(S1)
# print(num_S1 )
# print(len(arr),len(xp))
mp.subplot(2,1,1)
mp.plot(xpoints, ypoints)
# mp.plot(xpoints,num_S1) 
# mp.plot(xpoints,num_S2)
xpoints.append( years+1)
mp.plot(xpoints,S1)
mp.plot(xpoints,S2)
mp.plot(xpoints,S3)
# mp.plot(xpoints,arr)
mp.xlabel("Years")
mp.ylabel("Number of People")
mp.legend(["Total population","S1 population de","S2 population de","S3 population de"]) 

mp.subplot(2,1,2)
mp.plot(xpoints,I1)
mp.plot(xpoints,I2)
mp.plot(xpoints,I3)

xpoints.pop()
# # mp.plot(xpoints,num_I1) 
# # mp.plot(xpoints,num_I2)
mp.xlabel("Years")
mp.ylabel("Number of People")

mp.legend(["I1 population de","I2 population de","I3 population de"])
# mp.subplot(3,1,3)
# mp.plot(xpoints,arr_y1)
# mp.plot(xpoints,arr_y2)
# mp.plot(xpoints,arr_y3)
# arr_h1.pop()
# mp.plot(xpoints,arr_h1)


# mp.legend(["Total population","AA population","AS population","S1 population","S2 population","I1 population","I2 population"]) 
mp.show()

