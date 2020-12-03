#Sources used to get stories for templates: 
# https://www.madlibs.com/wp-content/uploads/2016/04/VacationFun_ML_2009_pg15.pdf
# https://irp-cdn.multiscreensite.com/ec2b0ab8/files/uploaded/Mad%20Libs.pdf
                                            
import re

class Template:
    """Generates the template
    
    """
    def genre(self, genre):
        """ Choose the genre of the story to be generated
        Args:
        genre(str) User chooses between different genres such as comedy, horror etc.
        Side effects:
        Generates a story of the genre choosen
        
        """
        genre = input("Choose a genre: vacation/park/zoo/arcade ")
        #create a method that reads the madlibstemplate.txt and grabs the story that matches the inputed genre
        
    def format(self, template): #Casey
        """ Determines which types of words will be needed to fill in the blank of the specific story.
        
        Args: 
            template(str): path to a txt file, in this case we are using the madlibstemplate.txt

        Returns:
            The values of the txt file that are in []
            
        """
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
        #takes story that was choosen in the genre and returns a tuple of every phrase in [] in the story
        
    def generator(self, story):
        """Compiles story into a Mad Libs template text file
        Arg:
        story(dict): total words in mad libs template
        Side effects:
        file(str): text file 
        """
