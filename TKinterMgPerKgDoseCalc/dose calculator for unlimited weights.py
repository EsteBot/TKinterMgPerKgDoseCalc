#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class color:
    BLUE  = '\033[1;34;48m'
    GREEN = '\033[1;32;48m'
    CYAN  = '\033[1;36;36m' 
    END   = '\033[1;37;0m' 

Mg_Per_Kg = float(input("What dose of Mg per Kg would you\
 like to use? "))

print('')

RatTot = []

r = int(input('How many rat weights would you like to enter? ' ))

print('')

print('Enter each rat weight below.')
for i in range(0, r):
    ele = float(input())

    RatTot.append(ele)

Sum = sum(RatTot)

Vol   = Sum / 1000
Mg    = round((Mg_Per_Kg * Sum / 1000000), 6)
Vol10 = round(((Vol * .1) + Vol), 6)
Mg10  = round(((Mg * .1) + Mg), 6)
print(Mg)
print(Mg10)


print('')

print('The total weight of the rats you entered is:'\
, Sum,'grams')

print('You will need') 
print(color.BLUE + str(Vol),'mL' + color.END)
print('of solution to dilute the drug into.')

print('')

print('The weight of drug you need for these rat(s) weights\
 and solution volume is:')
print(color.GREEN + str(Mg),'grams' + color.END)
print('or')
print(color.GREEN + str(Mg * 1000),'milligrams' + color.END)

print('')

print('However, to make up for incidental solution loss\
 increasing your total end\nsolution volume\
 by 10% is advised.\
 This would then require:')

print(color.GREEN + str(Mg10),'grams' + color.END)
print('or') 
print(color.GREEN + str(Mg10 * 1000),'milligrams' + color.END)
print('of drug into')
print(color.BLUE + str(Vol10),'mL' + color.END)
print('of solution.')
print('')
