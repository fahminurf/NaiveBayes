# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 07:02:58 2019

@author: King
"""

import pandas as pd

#Importing Data
dataTrain = pd.read_csv("TrainsetTugas1ML.csv")
#print(dataTrain.head())
#print(dataTrain)
dataTest = pd.read_csv("TestsetTugas1ML.csv")
#print(dataTest.head())
#print(dataTest)



incgrtr50= len(dataTrain[dataTrain['income'] == ">50K"])
incless50= len(dataTrain[dataTrain['income'] == "<=50K"])

#AGE TO INCOME
ageoldgrt50 = len(dataTrain[(dataTrain['age'] == "old") & (dataTrain['income'] == ">50K")] )
ageadltgrt50 = len(dataTrain[(dataTrain['age'] == "adult") & (dataTrain['income'] == ">50K")] )
ageynggrt50 = len(dataTrain[(dataTrain['age'] == "young") & (dataTrain['income'] == ">50K")] )

ageoldless50 = len(dataTrain[(dataTrain['age'] == "old") & (dataTrain['income'] == "<=50K")] )
ageadltless50 = len(dataTrain[(dataTrain['age'] == "adult") & (dataTrain['income'] == "<=50K")] )
ageyngless50 = len(dataTrain[(dataTrain['age'] == "young") & (dataTrain['income'] == "<=50K")] )

#WORKCLASS TO INCOME
wrkclsprvgrt50 = len(dataTrain[(dataTrain['workclass'] == "Private") & (dataTrain['income'] == ">50K")] )
wrkclsprvless50 =len(dataTrain[(dataTrain['workclass'] == "Private") & (dataTrain['income'] == "<=50K")] )

wrkclslclgrt50 = len(dataTrain[(dataTrain['workclass'] == "Local-gov") & (dataTrain['income'] == ">50K")] )
wrkclslclless50 = len(dataTrain[(dataTrain['workclass'] == "Local-gov") & (dataTrain['income'] == "<=50K")] )

wrkclsssengrt50 = len(dataTrain[(dataTrain['workclass'] == "Self-emp-not-inc") & (dataTrain['income'] == ">50K")] )
wrkclsssenless50 = len(dataTrain[(dataTrain['workclass'] == "Self-emp-not-inc") & (dataTrain['income'] == ">50K")] )

#EDU TO INCOME

edubclgrt50 = len(dataTrain[(dataTrain['education'] == "Bachelors") & (dataTrain['income'] == ">50K")] )
edubclless50 = len(dataTrain[(dataTrain['education'] == "Bachelors") & (dataTrain['income'] == "<=50K")] )

edubsmcgrt50 = len(dataTrain[(dataTrain['education'] == "Some-college") & (dataTrain['income'] == ">50K")] )
edusmcless50 = len(dataTrain[(dataTrain['education'] == "Some-college") & (dataTrain['income'] == "<=50K")] )

eduhsggrt50 = len(dataTrain[(dataTrain['education'] == "HS-grad") & (dataTrain['income'] == ">50K")] )
eduhsgless50 = len(dataTrain[(dataTrain['education'] == "HS-grad") & (dataTrain['income'] == "<=50K")] )

#marital status to income

msmcsgrt50= len(dataTrain[(dataTrain['marital-status'] == "Married-civ-spouse") & (dataTrain['income'] == ">50K")] )
msmcsless50 = len(dataTrain[(dataTrain['marital-status'] == "Married-civ-spouse") & (dataTrain['income'] == "<=50K")] )

msnmgrt50= len(dataTrain[(dataTrain['marital-status'] == "Never-married") & (dataTrain['income'] == ">50K")] )
msnmless50 = len(dataTrain[(dataTrain['marital-status'] == "Never-married") & (dataTrain['income'] == "<=50K")] )

msdivgrt50= len(dataTrain[(dataTrain['marital-status'] == "Divorced") & (dataTrain['income'] == ">50K")] )
msdivless50 = len(dataTrain[(dataTrain['marital-status'] == "Divorced") & (dataTrain['income'] == "<=50K")] )

#occupation to income

occprofgrt50= len(dataTrain[(dataTrain['occupation'] == "Prof-specialty") & (dataTrain['income'] == ">50K")] )
occprofless50 = len(dataTrain[(dataTrain['occupation'] == "Prof-specialty") & (dataTrain['income'] == "<=50K")] )

occcrftgrt50= len(dataTrain[(dataTrain['occupation'] == "Craft-repair") & (dataTrain['income'] == ">50K")] )
occcrftless50 = len(dataTrain[(dataTrain['occupation'] == "Craft-repair") & (dataTrain['income'] == "<=50K")] )

occexecgrt50= len(dataTrain[(dataTrain['occupation'] == "Exec-managerial") & (dataTrain['income'] == ">50K")] )
occexecless50 = len(dataTrain[(dataTrain['occupation'] == "Exec-managerial") & (dataTrain['income'] == "<=50K")] )

#relationship to income

rlthsbgrt50= len(dataTrain[(dataTrain['relationship'] == "Husband") & (dataTrain['income'] == ">50K")] )
rlthsbless50 = len(dataTrain[(dataTrain['relationship'] == "Husband") & (dataTrain['income'] == "<=50K")] )

rltnifgrt50= len(dataTrain[(dataTrain['relationship'] == "Not-in-family") & (dataTrain['income'] == ">50K")] )
rltnifless50 = len(dataTrain[(dataTrain['relationship'] == "Not-in-family") & (dataTrain['income'] == "<=50K")] )

rltowcgrt50= len(dataTrain[(dataTrain['relationship'] == "Own-child") & (dataTrain['income'] == ">50K")] )
rltowcless50 = len(dataTrain[(dataTrain['relationship'] == "Own-child") & (dataTrain['income'] == "<=50K")] )

#hours per week to income


hpwnorgrt50= len(dataTrain[(dataTrain['hours-per-week'] == "normal") & (dataTrain['income'] == ">50K")] )
hpwnorless50 = len(dataTrain[(dataTrain['hours-per-week'] == "normal") & (dataTrain['income'] == "<=50K")] )

hpwlowgrt50= len(dataTrain[(dataTrain['hours-per-week'] == "low") & (dataTrain['income'] == ">50K")] )
hpwlowless50 = len(dataTrain[(dataTrain['hours-per-week'] == "low") & (dataTrain['income'] == "<=50K")] )


hpwmanygrt50= len(dataTrain[(dataTrain['hours-per-week'] == "many") & (dataTrain['income'] == ">50K")] )
hpwmanyless50 = len(dataTrain[(dataTrain['hours-per-week'] == "many") & (dataTrain['income'] == "<=50K")] )


#---------------------
#hitungmean
#income
meanincmgrtr50 =incgrtr50/len(dataTrain)
meanincmless50 =incless50/len(dataTrain)

#mean age to income
meanageadltgrt50 = ageadltgrt50/incgrtr50
meanageadltless50 = ageadltless50/incless50

meanagaoldtgrt50 = ageoldgrt50/incgrtr50
meanageoldless50 = ageoldless50/incless50

meanageynggrt50 = ageynggrt50/incgrtr50
meanageyngless50 = ageyngless50/incless50

#mean workclass to income
meanprvgrt50 = wrkclsprvgrt50/incgrtr50
meanprvless50 = wrkclslclless50/incless50

meanlclgrt50 = wrkclslclgrt50/incgrtr50
meanlclless50 = wrkclsprvless50/incless50

meansengrt50 = wrkclsssengrt50/incgrtr50
meansenless50 = wrkclsssenless50/incless50

#mean edu to income
meanbclgrt50 = edubclgrt50/incgrtr50
meanbclless50 = edubclless50/incless50

meansmcgrt50 = edubsmcgrt50/incgrtr50
meansmcless50 = edusmcless50/incless50

meanhsggrt50 = eduhsggrt50/incgrtr50
meanhsgless50 = eduhsgless50/incless50

#mean marital status to income
meanmcsgrt50 = msmcsgrt50/incgrtr50
meanmcsless50 = msmcsless50/incless50

meannmgrt50 = msnmgrt50/incgrtr50
meannmless50 = msnmless50/incless50

meandivgrt50 = msdivgrt50/incgrtr50
meandivless50 = msdivless50/incless50

#mean occupation to income
meanprofgrt50 = occprofgrt50/incgrtr50
meanprofless50 = occprofless50/incless50

meancrftgrt50 = occcrftgrt50/incgrtr50
meancrftless50 = occcrftless50/incless50

meanexecgrt50 = occexecgrt50/incgrtr50
meanexecless50 = occexecless50/incless50


#mean relationship to income
meanhsbgrt50 = rlthsbgrt50/incgrtr50
meanhsbless50 = rlthsbless50/incless50

meannifgrt50 = rltnifgrt50/incgrtr50
meannifless50 = rltnifless50/incless50

meanowcgrt50 = rltowcgrt50/incgrtr50
meanowcless50 = rltowcless50/incless50


#mean hours per week to income
meannorgrt50 = hpwnorgrt50/incgrtr50
meannorless50 = hpwnorless50/incless50

meanlowgrt50 = hpwlowgrt50/incgrtr50
meanlowless50 = hpwlowless50/incless50

meanmanygrt50 = hpwmanygrt50/incgrtr50
meanmanyless50 = hpwmanyless50/incless50



#sos =dataTrain.iloc[0]['age'] 
#print(sos)

for y in range(len(dataTest)):
     z=[]
     for x in range(len(dataTest)):
        a1=0
        b1=0
        a2=0
        b2=0
        c1=0
        c2=0
        d1=0
        d2=0
        e1=0
        e2=0
        f1=0
        f2=0
        g1=0
        g2=0
        
#        age
        if dataTest.iloc[x]['age'] == "adult" :
            a1=meanageadltgrt50
            a2=meanageadltless50
            
        if dataTest.iloc[x]['age'] == "old" :
            a1=meanagaoldtgrt50 
            a2=meanageoldless50 
            
        if dataTest.iloc[x]['age'] == "young" :
            a1=meanageynggrt50
            a2=meanageyngless50 
        
#        workclass
        
            
        if dataTest.iloc[x]['workclass'] == "Private" :
          b1=meanprvgrt50 
          b2=meanprvless50  
            
        if dataTest.iloc[x]['workclass'] == "Local-gov" :
          b1=meanlclgrt50  
          b2=meanlclless50 
          
        if dataTest.iloc[x]['workclass'] == "Self-emp-not-inc" :
          b1=meansengrt50   
          b2=meansenless50 
          
#        education
        
        if dataTest.iloc[x]['education'] == "Some-college" :
          c1=meansmcgrt50  
          c2=meansmcless50   
            
        if dataTest.iloc[x]['education'] == "Hs-grad" :
          c1=meanhsggrt50   
          c2=meanhsgless50  
          
        if dataTest.iloc[x]['education'] == "Bachelors" :
          c1=meanbclgrt50    
          c2=meanbclless50 
          
#        marital status
    
        if dataTest.iloc[x]['marital-status'] == "Married-civ-spouse" :
          d1=meanmcsgrt50   
          d2=meanmcsless50    
            
        if dataTest.iloc[x]['marital-status'] == "Never-married" :
          d1=meannmgrt50    
          d2=meannmless50   
          
        if dataTest.iloc[x]['marital-status'] == "Divorced" :
          d1=meandivgrt50     
          d2=meandivless50  
        
#        occupation
        
        if dataTest.iloc[x]['occupation'] == "Prof-specialty" :
          e1=meanprofgrt50    
          e2=meanprofless50     
            
        if dataTest.iloc[x]['occupation'] == "Craft-repair" :
          e1=meancrftgrt50     
          e2=meancrftless50    
          
        if dataTest.iloc[x]['occupation'] == "Exec-managerial" :
          e1=meanexecgrt50      
          e2=meanexecless50 
          
#          relationship
        
        if dataTest.iloc[x]['relationship'] == "Husband" :
          f1=meanhsbgrt50     
          f2=meanhsbless50      
            
        if dataTest.iloc[x]['relationship'] == "Not-in-family" :
          f1=meannifgrt50      
          f2=meannifless50     
          
        if dataTest.iloc[x]['relationship'] == "Own-child" :
          f1=meanowcgrt50       
          f2=meanowcless50 
          
          
#          hours per week
        
        if dataTest.iloc[x]['hours-per-week'] == "normal" :
          g1=meannorgrt50      
          g2=meannorless50       
            
        if dataTest.iloc[x]['hours-per-week'] == "low" :
          g1=meanlowgrt50       
          g2=meanlowless50      
          
        if dataTest.iloc[x]['hours-per-week'] == "many" :
          g1=meanmanygrt50       
          g2=meanmanyless50 

        hasA=a1*b1*c1*d1*e1*f1*g1
        hasB=a2*b2*c2*d2*e2*f2*g2
    
        fixA=hasA*incgrtr50
        fixB=hasB*incless50
     
        if fixA>fixB:
            hunda=">50K"
        else:
            hunda="<=50K"
            
        z.append(hunda)

fix= pd.DataFrame(z)
fix.to_csv('TebakanTugas1.csv',index=False,header=False)
print(fix)


