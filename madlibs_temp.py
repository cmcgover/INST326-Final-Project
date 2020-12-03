#Sources used to get stories for templates: 
# https://www.madlibs.com/wp-content/uploads/2016/04/VacationFun_ML_2009_pg15.pdf
# https://irp-cdn.multiscreensite.com/ec2b0ab8/files/uploaded/Mad%20Libs.pdf
                                            
# Hello
import re

class Template:
    '''Generates the template
    
    '''
    def genre(self, filename): #Amanu
    
        """ Choose the genre of the story to be generated
       
        Args:
        genre(str) User chooses between different genres such as vacation, park, zoo, or arcade.
        Side effects:
        Generates a story of the genre choosen
        
        """
        genre = input("Choose a genre: vacation/park/zoo/arcade ")
        open_file = open(filename, "r")
        content = open_file.read()
        d = {}
        for i in content: 
            x = i.split(":")
            genre = x[0]
            story = x[1]
            d[genre] = story 
            
        print(d)
        
        
        
    def read(): #Chelsea
        output = []
        keywords=['[adjective]', '[noun]', '[plural noun]','[verb ending in "ing"]','[part of body]','[a place]','[number]','[adverb]','[past tense verb]','[verb]']
        for word in content.strip():
            if word in keywords:
                newWord=input('replace the word %s:' % word)
                output.append(newWord)
            else:
                output.append(word)
        
        return output
            
            
        #create a method that reads the madlibstemplate.txt and grabs the story that matches the inputed genre
    
    def generator(self, story): #Alhaji
        #prompts user for words in square brackets
        #uses output to ask user to fill in words
        """Compiles story into a Mad Libs template text file
        Arg:
        story(dict): total words in mad libs template
        Side effects:
        file(str): text file 
        """
        
    
    def format(filename):
        """ Determines which types of words will be needed to fill in the content.
        
        Args: 
            template(str): path to a txt file, in this case we are using the madlibstemplate.txt

        Returns:
            The values of the txt file that are in []   
        """
        temp = open(filename, "r", encoding="utf-8")
        blank_temp = re.sub()
        #takes story that was choosen in the genre (content) and replaces the square brackets w the user inputs
        #using regex use finditer, sub
        #method takes out square brackets
        
    