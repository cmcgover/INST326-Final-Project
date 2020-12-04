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
        
    def genre(self, genre):
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
        open_file = open(filename, "r")
        content = open_file.read()
        d = {}
        x = content.split(":")
        genre = x[0]
        self.story = x[1]
        d[genre] = self.story 
        print(story) #instead of printing I think returning it would be better bc we need to use this variable in the next method
        
        
    def read(filename): #Chelsea
        """Using the story choosen in the genre method, this method finds 
        the square brackets in the story and creates and input for the user to fill in.
        
            Args:
                filename(str): madlibs template text file
            Returns: 
                An input for user based on the words found in square brackets
                
            Side effects:
                output(list): Puts the user's input into a list that will be replaced back into the template.
        """
        output = []
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

    
    def format(self): #Casey
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
        
    
