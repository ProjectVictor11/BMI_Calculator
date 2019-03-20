# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 23:04:17 2019

@author: Amit
"""

## Programme-- To Calculate the body mass index(BMI) of a person....
# [BMI calculator is used to check whether a person is overweight, healthy(normal) or underweight...]

print('select the unit of weight(kg, g)')

w_unit=h_unit='unit'
count1=count2=0

while w_unit not in('g', 'kg'):              # For unacceptable units..
    if count1!=0:
        print('undefined unit entered, enter again!')
    count1+=1
    w_unit=str(input('enter the unit here   :'))
weight=float(input('Your Weight   :'))

if w_unit=='g':
    weight/=1000

print('select the unit of height(m, cm, inch, feet)')

while h_unit not in('m', 'cm', 'inch', 'feet'):
    if count2!=0:
        print('undefined unit entered, enter again!')
    count2+=1
    h_unit=str(input('enter the unit here   :'))
height=float(input('Your height    :'))

if h_unit=='cm':
    height/=100
elif h_unit=='inch':
    height=(height*2.54)                # converted to cm.
    height/=100
elif h_unit=='feet':
    height*=12                          # converted into inches
    height*=2.54                        # converted into centimeters
    height/=100                         # converted into meters

BMI=weight/(height**2)
if BMI>=25.0:
    print(BMI, '             you are overwight  :(')
elif BMI<25.0 and BMI>=18.5:
    print(BMI, '             You are a healthy person  :)')
else:
    print(BMI, '            you are underweight  :(')
