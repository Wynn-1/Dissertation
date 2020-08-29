import numpy as np
from numpy import random as rm
import math
import matplotlib.pyplot as plt



list_optimal_profit=[]
list_price_1=[]
list_price_2=[]



for q in np.arange(0.01,0.02,0.02):

    
    for price_1 in np.arange(50,55,10):
        p2=[]
        Profit_Curve=[]
        list_Abandonment_1=[]
        list_Abandonment_2=[]
        list_num_nonenter=[]
        list_num_enter=[]
        list_num_matching_pair=[]
        list_num_queue_a1=[]
        list_num_queue_a2=[]
        
        
        
        for price_2 in np.arange(50,55,10):
            
            

            p2.append(price_2)
            profit=0
            Termination=2000
            Sub_period=30
            a1=rm.exponential(1,1)
            a2=rm.exponential(1,1)
            queue_a1=[]
            queue_a2=[]
            cost_of_abandonment_1=10
            cost_of_abandonment_2=10
            number_matching=0
            EC0=[a1[0]]  #arrival time of a1
            EC1=[a2[0]]  #arrival time of a2
            EC2=[Termination]  #Termination
            EC=EC0+EC1+EC2
            TNOW=0
            TNEXT=min(EC)
            AreaQ1=0
            AreaQ2=0
            AreaCurve1=[0]
            AreaCurve2=[0]
            Abandonment1 = 0
            Abandonment2 = 0
            t=[0]
            number_nonenter=0
            
            n=0  #Then number of customers
        

            while TNEXT<Termination:
                length_int=TNEXT-TNOW
                TNOW=TNEXT
                AreaQ1=AreaQ1+len(queue_a1)*length_int
                AreaQ2=AreaQ2+len(queue_a2)*length_int
                AreaCurve1.append(AreaQ1/TNOW)
                AreaCurve2.append(AreaQ2/TNOW)
                t.append(TNOW)

                
                if EC.index(TNOW)==0: #Tnow is the arrival time of a1
                    EC[0]=(TNOW+rm.exponential(1,1))[0]
                    willingness_to_pay=rm.uniform(0,100)

                    
                    if willingness_to_pay < price_1:
                        number_nonenter +=1
                    else:
                        n += 1
                        profit=profit+price_1
                        if queue_a2==[]:     #check whether there are people in queue_a2
                            queue_a1.append(TNOW)   # if there is no person in queue_a2, the person join the queue_a1
                            EC.append(Sub_period+TNOW) # add the abandonment time of the person
                        else:
                            
                            rv=rm.uniform(0,1)   
                            if rv<=math.pow(1-q,len(queue_a2)):
                                queue_a1.append(TNOW)
                                EC.append(Sub_period+TNOW)
                            else:
                                l=math.floor(rm.uniform(0,len(queue_a2)))
                                EC.remove(queue_a2[l]+Sub_period)    #remove the abandonment time of the person of a2
                                queue_a2.pop(l)              #remove the matching person from the queue_a2
                                number_matching += 1   

                        
                elif EC.index(TNOW)==1:# Tnow is the arrival time of a2
                    EC[1]=(TNOW+rm.exponential(1,1))[0]
                    willingness_to_pay=rm.uniform(0,100)

                    if willingness_to_pay < price_2:
                        number_nonenter +=1
                    else:
                        n += 1
                        profit=profit+price_2
                        if queue_a1==[]:     #check whether there are people in queue_a1
                            queue_a2.append(TNOW)   # if there is no person in queue_a1, the person join the queue_a1
                            EC.append(Sub_period+TNOW) # add the abandonment time of the person
                        else:
                            rv=rm.uniform(0,1)
                            if rv<=math.pow(1-q,len(queue_a2)):
                                queue_a2.append(TNOW)
                                EC.append(Sub_period+TNOW)
                            else:
                                l=math.floor(rm.uniform(0,len(queue_a1)))
                                EC.remove(queue_a1[l]+Sub_period)
                                queue_a1.pop(l)
                                number_matching += 1   

                else:  
                    EC.remove(TNOW)  #Tnow is the time of the end of subscription of one person
                    i = TNOW-Sub_period     #remove the person from the queue    
                    for j in queue_a1:  #check the type of the person
                        if abs(j-i)<0.000001:  #the error of expectation is allowed
                            profit = profit - cost_of_abandonment_1
                            queue_a1.remove(j)
                            Abandonment1 += 1

                    for j in queue_a2:
                        if abs(j-i)<0.000001:
                            profit = profit - cost_of_abandonment_2
                            queue_a2.remove(j) 
                            Abandonment2 += 1

            
                TNEXT=min(EC)
                  
            
            Profit_Curve.append(profit/Termination)
            list_Abandonment_1.append(Abandonment1)
            list_Abandonment_2.append(Abandonment2)
            list_num_nonenter.append(number_nonenter)
            list_num_enter.append(n)
            list_num_matching_pair.append(number_matching)
            list_num_queue_a1.append(len(queue_a1))
            list_num_queue_a2.append(len(queue_a2))
            
        x=t
        y=AreaCurve1
        z=AreaCurve2
        
        type1,=plt.plot(x,y,linewidth=2.0)
        type2,=plt.plot(x,z,linewidth=2.0)
        plt.xlabel('t')
        plt.ylabel('Average number in system')
        plt.legend(handles=[type1,type2],labels=['type-1 users','type-2 users'])
        plt.title("Termination time is 2000")










