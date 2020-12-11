#Sources used to get stories for templates: 
# https://www.madlibs.com/wp-content/uploads/2016/04/VacationFun_ML_2009_pg15.pdf
# https://irp-cdn.multiscreensite.com/ec2b0ab8/files/uploaded/Mad%20Libs.pdf
                                            
from argparse import ArgumentParser                                          
import re
import sys

class Template:
    """Generates the template
    """
    
    def __init__(self): #Chelsea
        """Initializes content and output words
        """
        self.story = {}
        self.output = []
        
    def genre(self, genre): #Amanu
        """ Choose the genre of the story to be generated
        **work in progress. Was not able to output all the genres, only the vacation genre. currently being worked on. 
        Args:
        filename(txt) User chooses between different genres such as vacation, park, zoo, or arcade to be used
        as a template. Currently just the vacation genre, but will update to have all the genres output. 
    
        Side effects:
        d(dict) = stores the different genres and stories in a dictionary.
        Genre is the key, stories in the template are values. 
        genre(key value in dict): stores genre title in dictionary as key value
        story(value in dict): stores story as value
        
        Return: 
        story(dict): return the vacation genre  story. 
        
        """    
        open_file = open(genre, "r")
        content = open_file.read()
        self.d = {}
        x = content.split("\n\n")
        for template in x: 
            y = template.strip().split(":")
            self.d[y[0].lower()] = y[1]
         
    def user_choice (self): #Amanu
        user_input  = input("Choose a genre: vacation/park/zoo/arcade ")
        return self.d[user_input]

            
     # add, code to validate user input, and give them a chance to do it again. use while loop 
            
    def read(self, genre): #Chelsea
        self.output = []
        keywords=['[adjective]', '[noun]', '[plural noun]','[verb ending in "ing"]','[part of body]','[a place]','[number]','[adverb]','[past tense verb]','[verb]']
        for word in self.story.strip():
            if word in keywords:
                newWord=input('replace the word %s:' % word)
                self.output.append(newWord)
            else:
                self.output.append(word)
        
        return self.output
            
    
    def generator(self, filename): #Alhaji
        #prompts user for words in square brackets
        #uses output to ask user to fill in words
        """Takes the list output from read() and replaces all the words with brackets from the story
            pulled from genre()
        Arg:
        filename: path leading to file
        
        Side effects:
        returns generated_story
        """
        generated_story = re.sub(r"\[([^\]]+)\]", read(), genre())
        return generated_story

    
    def format(filename): #Casey
        """ Determines which types of words will be needed to fill in the content.
        
        Args: 
        template(str): path to a txt file, in this case we are using the madlibstemplate.txt

        Returns:
        The values of the txt file that are in []   
        """
        with open(filename, "r", encoding="utf-8") as f:
            madlibs = f.read()
            word_types = re.sub(r"\[([^\]]+)\]", self.output)
            return word_types
        
        
    #takes story that was choosen in the genre (content) and replaces the square brackets w the user inputs
    #using regex use finditer, sub
    #method takes out square brackets
if __name__ == "__main__": 
    x = Template()
    print(x.genre("madlibstemplate.txt"))
    
    
