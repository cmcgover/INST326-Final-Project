#Test script for madlibs_temp
from madlibs_temp import *
import re
import pytest
x = Template("check.txt")

def test_genre():
    x.genre("check.txt")
    assert x.content
    assert list(x.d.keys()) == ['story1','story2','story3','story4'] 
    assert len(x.d.keys()) ==  4
    
    
    
def test_read():
    t = ("A vacation is when you take a trip to some [adjective] place with your [adjective] family."
         "Usually you go to some place that is near a/an [noun] or up on a/an [noun]. A good vacation place isone where you can ride [plural-noun] or play [game] or go hunting for [plural-noun] ."
         " I like to spend my time [verb-ending-in-ing] or [verb-ending-in-ing]."
         "When parents go on a vacation, they spend their  time eating three [plural-noun] a day, and fathers play golf," 
         "and mothers sit around [verb-ending-in-ing]. Last summer, my little brother fell in a/an [noun] "
         "and got poison [plant] all over his [part-of-body]. My family is going to go to (the) [place], "
         "and I will practice [verb-ending-in-ing]."
         " Parents need vacation more than kids because parents are always very [adjective] and "
         "because they have to work [number] hours every day all year making enough [plural-noun] to pay"
         "for the vacation.")
    output= x.read(t)
    assert output == ['adjective', 'adjective','noun','noun', 'plural-noun','game','plural-noun','verb-ending-in-ing', 'verb-ending-in-ing', 'plural-noun','verb-ending-in-ing','noun','plant', 'part-of-body','place','verb-ending-in-ing','adjective','number','plural-noun']
   
    
    
    
    
def test_generator():
    word = "[noun]"
    regex = re.compile(r"(\[[^\]]+\])")
    assert regex.match(word)
  
    
#def test_format():
    
