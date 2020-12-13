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
        self.story = " "
        self.output = []
        self.d = []
        
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
        for word in self.d:
            if word in keywords:
                newWord=input('replace the word %s:' % word)
                self.output.append(newWord)
            else:
                self.output.append(word)
        
        return self.output
            
    
    def generator(self): #Alhaji
        """Uses re.sub function to substitute all words inside brackets with "{}"
            then uses .format funtion to replace the "{}" with words in self.output in order
        
        Side effects:
            self.story gets updated
        """
        string = " " #output of user_choice(self)
    
   
        brackets_sub = re.sub(r"\[([^\]]+)\]", "{}", string)
        self.story = brackets_sub.format(*self.output)
        
    
    def format(self, filename): #Casey
        """ Iterates through the story of the genre picked by the user, locates the words in brackets and returns a list of the words without the brackets
        
        Side Effects: 
        locates the words that must be replaced by the user

        Returns:
        word_types(list): a list of the word types that need to be replaced by the user's input   
        """
        remove_brackets = r"\[([^\]]+)\]"
        regex = re.compile(remove_brackets)
        words = regex.finditer(self.story)
        word_types = []
        for word in words:
            word_types.append(word.group(1))
        return word_types 
        
    
def parse_args(argList):
    """Parses command-line arguments.

    The following required command-line arguments are defined:

    genre: a txt file

    Args:
        arglist (list of str): a list of command-line arguments.

    Returns:
        namespace: a namespace with the story replaced with the user's inputted words.
    """
    parser= ArgumentParser()
    parser.add_argument("genre", help ="path to txt file called madlibstemplate.txt")
    return parser.parse_args(argList)

if __name__ == "__main__": 
    x = Template()
    print(x.genre("madlibstemplate.txt"))
    
    
