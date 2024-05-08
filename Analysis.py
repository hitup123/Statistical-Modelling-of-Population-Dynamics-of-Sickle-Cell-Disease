        
import matplotlib.pyplot as mp
import numpy as np
#1-AA TYPE
#2-AS TYPE
def birthRate(pop):#birthrate depedent of the current pop
                brc=0.023   #birth rate constant
                cc=100000#carrying capacity       
                return brc*(1-(pop/cc))

#Human pop 
hpop=200
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
kill=0.0004
#v: Extra mortality due to sickle cell gene complications.
v=0.000003
#Number of mosquitoes:
m=10000
#scale down var
E=1
#mosquito mortality rate
moskill=0.07
#freqency of S gene     
# S=0.2
#frequency of A gene
# A=1-S
#fractions of the new born individuals of TYPE AA
P1=( w[0]+ w[1]/2)**2
P1_copy=( w[0]+ w[1]/2)**2
#fractions of the new born individuals of TYPE AS
P2=( w[0]+ w[1]/2)*( w[1]+ w[2]/2)
P2_copy=( w[0]+ w[1]/2)*( w[1]+ w[2]/2)
#fractions of the new born individuals of TYPE SS
P3=(( w[1]/2)+ w[2])**2
P3_copy=(( w[1]/2)+ w[2])**2
#years./time
years=1500

#fraction of mosquitoes with plasmodium parasite
fm=0.1
#number of infected mosquitoes
Im= m* fm
#probablity of acquiring plasmodium parasite
mpp=[0.05,0.09,0.14]

#probablity of acquiring plasmodium per bite
ppb=[0.04,0.02,0.0]
#addtional mortality rate due to malaria
mkill=[0.0001,0.00005,0.000001]
#biting rate
b=0.2
#recovery rate 
rr=[0.00099,0.00066,0.00033]


arr=[]
Lambda=[]   
S1=[ uip[0]]
S2=[ uip[1]]  
S3=[ uip[2]]  
I1=[ ip[0]]
I2=[ ip[1]]
I3=[ ip[2]]
arr_h1=[]
arr_y1=[]
arr_y2=[]
arr_y3=[]
arr_w1=[]
arr_w2=[]
arr_w3=[]
# print( w[0]," ", w_Copy[2])
y=[(I1[0]/ hpop),(I2[0]/ hpop),(I3[0]/ hpop)]
arr_h1.append( hpop)
arr_y1.append(y[0])
arr_y2.append(y[1])
arr_y3.append(y[2])
arr_w3.append( w_Copy[2])
arr_w2.append( w_Copy[1])
arr_w1.append( w_Copy[0])
h1= hpop
arr_h1.append(h1)
for x in range(0, years):
        # arr.append( h1)
      
        # print(h," ",h)

        Lambda=[ b* ppb[0]* Im/h1, b* ppb[1]* Im/h1, b* ppb[2]* Im/h1]
        # P1=( w[0]+ w[1]/2)**2
        # P2=( w[0]+ w[1]/2)*( w[1]+ w[2]/2)
        # P3=(( w[1]/2)+ w[2])**2
        # roc_S1=(( P1)*( birthRate(h))*h)- kill*(S1[len(S1)-1])-(Lambda[0])*(S1[len(S1)-1])+( rr[0])*(I1[(len(I1)-1)])
        # roc_S2=(( P2)*( birthRate(h))*h)-( kill+ v)*(S2[len(S2)-1])-(Lambda[1])*(S2[len(S2)-1])+( rr[1])*(I2[(len(I2)-1)])
        # roc_S3=(( P3)*( birthRate(h))*h)-( kill+ v*10)*(S3[len(S3)-1])-(Lambda[2])*(S3[len(S3)-1])+( rr[2])*(I3[(len(I3)-1)])

        # roc_I1=(Lambda[0])*(S1[len(S1)-1])-( kill+ rr[0]+ mkill[0])*(I1[(len(I1)-1)])
        # roc_I2=(Lambda[1])*(S2[len(S2)-1])-(( kill+ v)+ rr[1]+ mkill[1])*(I2[(len(I2)-1)])
        # roc_I3=(Lambda[2])*(S3[len(S3)-1])-(( kill+ v*10)+ rr[1]+ mkill[2])*(I3[(len(I3)-1)])



        roc_hpop=h1*(( P1_copy+ P2_copy+P3_copy)*( birthRate(h1)/ E)-( kill/ E)* w_Copy[0]-(( kill+ v)/ E)* w_Copy[1]-( kill+ v*10)* w_Copy[2]-( mkill[0]/ E)*y[0]-( mkill[1]/ E)*y[1]-( mkill[2]/ E)*y[2])
        roc_y1= b* ppb[0]*( m/h1)* fm*(( w_Copy[0]) -y[0])-( E* kill+ rr[0]+ E* mkill[0])*(y[0])-(y[0]*(roc_hpop/h1))* E
        roc_y2= b* ppb[1]*( m/h1)* fm*( w_Copy[1] -y[1])-( E* kill+ rr[1]+ E* mkill[1])*(y[1])-(y[1]*(roc_hpop/h1))* E
        roc_y3= b* ppb[2]*( m/h1)* fm*( w_Copy[2] -y[2])-( E* kill+ rr[2]+ E* mkill[2])*(y[2])-(y[2]*(roc_hpop/h1))* E
        # roc_fm=
        roc_fm=(1- fm)*( b* mpp[0]*y[0]+ b* mpp[1]*y[1]+ b* mpp[2]*y[2])- fm* moskill
        
        roc_w2= P2_copy*( birthRate(h1)/ E)- (( kill+ v)/ E)* w_Copy[1]-(( mkill[1]/ E)*y[1])-( w_Copy[1]*(roc_hpop/h1))
        roc_w3= P3_copy*( birthRate(h1)/ E)- (( kill+ v*10)/ E)* w_Copy[2]-(( mkill[2]/ E)*y[2])-( w_Copy[2]*(roc_hpop/h1))
        roc_w1= P1_copy*(birthRate(h1)/E)-(kill/E)*w_Copy[0]-mkill[0]*y[0]-w_Copy[0]*roc_hpop/h1
        w_Copy[2]+=roc_w3
        w_Copy[1]+=roc_w2  
        w_Copy[0]+=roc_w1
        # roc_hpop=h1*((( P1_copy+ P2_copy)* birthRate(h)/ E)-( kill* w_Copy[0]/ E)-(( kill+ v) * w_Copy[1]/ E)-(( kill+ v*10)* w_Copy[2]* E)-( mkill[0] )*y[0]-( mkill[1]/ E )*y[1]-( mkill[2]/ E )*y[2])
        roc_y1= b* ppb[0]*( m/h1)* fm*(( w_Copy[0]) -y[0])-( kill+ rr[0]+ mkill[0])*(y[0])-(y[0]*(roc_hpop/h1))
        roc_y2= b* ppb[1]*( m/h1)* fm*( w_Copy[1] -y[1])-( kill+ rr[1]+ mkill[1])*(y[1])-(y[1]*(roc_hpop/h1))
        roc_y3= b* ppb[2]*( m/h1)* fm*( w_Copy[2] -y[2])-( kill+ rr[2]+ mkill[2])*(y[2])-(y[2]*(roc_hpop/h1))

        roc_fm=(1- fm)*( b* mpp[0]*y[0]+ b* mpp[1]*y[1]+ b* mpp[2]*y[2])- fm* moskill
        P1_copy=( w_Copy[0]+ w_Copy[1]/2)**2
        P2_copy=( w_Copy[0]+ w_Copy[1]/2)*( w_Copy[1]+ w_Copy[2]/2)
        P3_copy=(( w_Copy[1]/2)+ w_Copy[2])**2
        
        y[0]+=roc_y1
        y[1]+=roc_y2
        y[2]+=roc_y3
        fm+=roc_fm
        h1=h1+roc_hpop
        arr_h1.append(h1)
        arr_y1.append(y[0]*h1)
        arr_y2.append(y[1]*h1)
        arr_y3.append(y[2]*h1)
        arr_w3.append( w_Copy[2])
        arr_w2.append( w_Copy[1])
        arr_w1.append( w_Copy[0])

        # S1.append(roc_S1+S1[len(S1)-1])
        # S2.append(roc_S2+S2[len(S2)-1])
        # S3.append(roc_S3+S3[len(S3)-1])
        # I1.append(roc_I1+I1[len(I1)-1])
        # I2.append(roc_I2+I2[len(I2)-1])
        # I3.append(roc_I3+I3[len(I3)-1])
        # w.clear()
        # w=[(S1[len(S1)-1]+I1[len(I1)-1])/h,(S2[len(S2)-1]+I2[len(I2)-1])/h,(S3[len(S3)-1]+I3[len(I3)-1])/h]

        # roc_pop_DE= ( P1)*( birthRate(h))*h+ ( P2)* birthRate(h)*h -  kill*(S1[len(S1)-1]+I1[len(I1)-1]) - ( kill +  v)*(S2[len(S2)-1] +I2[len(I2)-1])
        #  hpop+=roc_pop_DE
        # roc_pop_DE=roc_I1+roc_I2+roc_S1+roc_S2+roc_I3+roc_S3
        # hpop+=roc_pop_DE


        # roc_pop= ( P1)*( birthRate(h))*h+ ( P2)* birthRate(h)*h -  kill*( uip[0]+ ip[0]) - ( kill +  v)*( uip[1] +  ip[1])
        # hpop+=roc_pop
        # num_S1.append(( uip[0]))
        # num_S2.append(( uip[1]))
        # num_I1.append( ip[0])
        # num_I2.append( ip[1])
       
        print(y[0]*h1," ",y[1]*h1," ", y[2]*h1,' ',x)
        # uip.clear()
        # ip.clear()
        # uip=[ hpop*(1- infectedratefraction)*(1- w), hpop*(1- infectedratefraction)*( w)]
        # ip=[ hpop* infectedratefraction*(1- w), hpop* infectedratefraction* w]
ypoints = arr
xpoints = list(range(0, years+1))
# mp.subplot(1,1,1)
# print(S1)
# print(num_S1 )

# mp.subplot(3,1,1)
# mp.plot(xpoints, ypoints)
# # mp.plot(xpoints,num_S1) 
# # mp.plot(xpoints,num_S2)
# xpoints.append( years+1)
# mp.plot(xpoints,S1)
# mp.plot(xpoints,S2)
# mp.plot(xpoints,S3)

# mp.legend(["Total population","S1 population de","S2 population de","S3 population de"]) 

# mp.subplot(3,1,2)
# mp.plot(xpoints,I1)
# mp.plot(xpoints,I2)
# mp.plot(xpoints,I3)

# xpoints.pop()
# # mp.plot(xpoints,num_I1) 
# # mp.plot(xpoints,num_I2)
# mp.legend(["I1 population de","I2 population de","I3 population de"])
# mp.subplot(3,1,1)
mp.plot(xpoints,arr_y1)
mp.plot(xpoints,arr_y2)
mp.plot(xpoints,arr_y3)
arr_h1.pop()
mp.plot(xpoints,arr_h1)


# mp.legend(["Total population","AA population","AS population","S1 population","S2 population","I1 population","I2 population"]) 
mp.show()
# print(num_S1)
mp.xlabel("Years")
mp.ylabel("Number of People")
print( w[0]," ", w_Copy[2])