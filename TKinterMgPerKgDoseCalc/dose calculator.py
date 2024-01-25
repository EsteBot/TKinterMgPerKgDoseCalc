#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class color:
    BLUE  = '\033[1;34;48m'
    GREEN = '\033[1;32;48m' 
    END   = '\033[1;37;0m'

Mg_Per_Kg  = float(input("What dose of Mg per Kg would you like to use? "))
Rat_weight = int(input("What is the weight in grams, of your rat(s)? "))

Vol = Rat_weight / 1000
Mg  = Mg_Per_Kg * Rat_weight / 1000000

print('')
print('You will need') 
print(color.BLUE + str(Vol),'mL' + color.END)
print('of solution to dilute the drug into.')
print('')
print('The weight of drug you need for this rat weight is:')
print(color.GREEN + str(Mg),'grams' + color.END)




