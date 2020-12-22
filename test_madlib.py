#Test script for madlibs_temp
from madlibs_temps import Template, genre, user_choice,read, generator, format
import re
 
def test_genre():
    assert self.content
    assert self.d.keys() in ['park'] 
    assert len(self.d.keys()) ==  1
        
def test_user_choice():
    
    
def test_read():
    
    
def test_generator():
    word = "[zoo]"
    regex = re.compile(r"(\[[^\]]+\])")
    assert regex.match(regex, word)
    
def test_format():
    
