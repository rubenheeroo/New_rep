
language : python



sudo : required
dist : xenial

python:
-3.6


install:

script:
- python New_rep.py

#c'est géniale!!!!!!!!!!!!

import unittest



def test_calculerScore(name,age):
    if name == 'Joseph' and age =='15':
        return '66%'
    if name =='Marie' and age== '33':
        return '50%'
    if name =='Marc' and age== '60':
        return '43%'
    if name =='Ely' and age== '28':
        return '75%'

