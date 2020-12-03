#Sources used to get stories for templates: 
# https://www.madlibs.com/wp-content/uploads/2016/04/VacationFun_ML_2009_pg15.pdf
# https://irp-cdn.multiscreensite.com/ec2b0ab8/files/uploaded/Mad%20Libs.pdf
                                            
import re

class Template:
    '''Generates the template
    
    '''
    def genre(self, genre):
    
        """ Choose the genre of the story to be generated
       
        Args:
        genre(str) User chooses between different genres such as vacation, park, zoo, or arcade.
        Side effects:
        Generates a story of the genre choosen
        
        """
        genre = input("Choose a genre: vacation/park/zoo/arcade ")
        open_file = open("madlibstemplate.txt", "r")
        content = open_file.read()
        output = []
        keywords=['[adjective]', '[noun]', '[plural noun]','[verb ending in "ing"]','[part of body]','[a place]','[number]','[adverb]','[past tense verb]','[verb]']
        for word in content.strip():
            if word in keywords:
                newWord=input('replace the word %s:' % word)
                output.append(newWord)
            else:
                output.append(word)
            
            
        #create a method that reads the madlibstemplate.txt and grabs the story that matches the inputed genre
    
    
    def format(filename):
        """ Determines which types of words will be needed to fill in the blank of the specific story.
        
        Args: 
            template(str): path to a txt file, in this case we are using the madlibstemplate.txt

        Returns:
            The values of the txt file that are in []   
        """
        temp = open(filename, "r", encoding="utf-8")
        blank_temp = re.sub()
        #takes story that was choosen in the genre and returns a tuple of every phrase in [] in the story
        #using regex use finditer, sub
        #method takes out square brackets
        
    def generator(self, story):
        #prompts user for words in square brackets
        """Compiles story into a Mad Libs template text file
        Arg:
        story(dict): total words in mad libs template
        Side effects:
        file(str): text file 
        """