# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 23:04:17 2019

@author: Amit
"""

## Programme-- To Calculate the body mass index(BMI) of a person....
# [BMI calculator is used to check whether a person is overweight, healthy(normal) or underweight...]

print('select the unit of weight(kg, g)')
w_unit=str(input('enter the unit here   :'))
weight=float(input('Your Weight   :'))

if w_unit=='g' or w_unit=='G':                #case sensitive..
    weight/=1000
print()

print('select the unit of height(m, cm, inch, feet)')
h_unit=str(input('enter the unit here   :'))
height=float(input('Your height    :'))

if h_unit=='cm' or h_unit=='CM':
    height/=100
elif h_unit=='inch' or h_unit=='INCH':
    height=(height*2.54)                     # converted to cm.
    height/=100
elif h_unit=='feet' or h_unit=='FEET':
    height*=12                                # converted into inches
    height*=2.54                              # converted into centimeters
    height/=100                               # converted into meters

BMI=weight/(height**2)
if BMI>=25.0:
    print(BMI, '           Sorry! you are overwight  :(')
elif BMI<25.0 and BMI>=18.5:
    print(BMI, '           You are a healthy person  :)')
else:
    print(BMI, '           Sorry! you are underweight  :(')
