#Sources used to get stories for templates: 
# https://www.madlibs.com/wp-content/uploads/2016/04/VacationFun_ML_2009_pg15.pdf
# https://irp-cdn.multiscreensite.com/ec2b0ab8/files/uploaded/Mad%20Libs.pdf
                                            
                                            
import re

class Template:
    '''Generates the template
    
    '''
    def genre(self, filename): #Amanu
    
        """ Choose the genre of the story to be generated
        **work in progress. Was not able to output all the genres, only the vacation genre. currently being worked on. 
        Args:
        filename(txt) User chooses between different genres such as vacation, park, zoo, or arcade to be used
        as a template. Currently just the vacation genre, but will update to have all the genres output. 
        
        Side effects:
        d(dict) = stores the sifferent genres and stories in a dictionary.
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
        story = x[1]
        d[genre] = story 
        print(story)
        
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
        
    
    def format(filename): #Casey
    """ Determines which types of words will be needed to fill in the content.
        
    Args: 
        template(str): path to a txt file, in this case we are using the madlibstemplate.txt

    Returns:
        The values of the txt file that are in []   
    """
    with open(filename, "r", encoding="utf-8") as f:
        madlibs = f.read()
        word_types = re.sub(r"\[([^\]]+)\]", madlibs)
        return word_types
        
        
    #takes story that was choosen in the genre (content) and replaces the square brackets w the user inputs
    #using regex use finditer, sub
    #method takes out square brackets
        
    