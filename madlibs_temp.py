#Sources used to get stories for templates: 
# https://www.madlibs.com/wp-content/uploads/2016/04/VacationFun_ML_2009_pg15.pdf
# https://irp-cdn.multiscreensite.com/ec2b0ab8/files/uploaded/Mad%20Libs.pdf
                                            
from argparse import ArgumentParser                                          
import re
import sys

class Template:
    """Generates the template
    """
    
    def __init__(self,file): #Chelsea
        """Initializes content and output words
        args: 
        file(str): name of the template file
        """
        self.story = " "
        self.output = []
        self.genre(file)
        
        
    def genre(self, file): #Amanu
        """ Choose the genre of the story to be generated
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
        open_file = open(file, "r")
        content = open_file.read()
        self.d = {}
        x = content.split("\n\n")
        for template in x: 
            y = template.strip().split(":")
            self.d[y[0].lower()] = y[1]
         
    def user_choice(self): #Amanu
        user_input  = input("Choose a genre: vacation/park/zoo/arcade ")
        return self.d[user_input]

            
     # add, code to validate user input, and give them a chance to do it again. use while loop 
            
    def read(self,template): #Chelsea
        self.output = []
        l = []
        keywords=['[adjective]', '[noun]', '[plural-noun]', '[game]', '[plant]',
                  '[verb-ending-in-ing]','[place]','[part-of-body]',
                  '[number]','[adverb]','[past-tense-verb]','[verb]']
        t = template.split(" ")
        for word in t:
            for item in keywords:
                if item in word:
                    self.output.append(item)
        
        return self.output
            
    
    def generator(self, template, user_answers): #Alhaji
        """Uses re.sub function to substitute all words inside brackets with "{}"
            then uses .format funtion to replace the "{}" with words in self.output in order
        
        Side effects:
            self.story gets updated
        """
   
        brackets_sub = re.sub(r"\[([^\]]+)\]", "{}", template)
        self.story = brackets_sub.format(*user_answers)
        return self.story
    
    def user_answers(self): #Casey
        """ Iterates through the story of the genre picked by the user, locates the words in brackets and returns a list of the words without the brackets
        
        Side Effects: 
        locates the words that must be replaced by the user

        Returns:
        word_types(list): a list of the word types that need to be replaced by the user's input   
        """
        remove_brackets = r"\[([^\]]+)\]"
        regex = re.compile(remove_brackets)
        user_words = []
        for word in self.output:
            new_word = regex.finditer(word)
            user_response = input(f"Please enter a(n) {new_word.group(1)}")
            user_words.append(user_response)
        return user_words
        
    
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


def main():
    args = parse_args(sys.argv[1:])
    
    x = True
    while x == True:
        template = Template("madlibstemplate.txt")
        user_input = template.user_choice()
        story_brackets = user_input.template.genre("madlibstemplate.txt")
        template.read(story_brackets)
        story = template.generator(story_brackets, template.user_answers())
        
        print(story)
        answer = input("Play Again? y/n: ")
        
        while answer != "y" or answer != "n":
            answer = input("Please Enter 'y' or 'n': ")
        
        if answer == "y":
            x = True
        elif answer == "n":
            x = False
    
    print("Thanks for playing!\nCreators:\nAmanu Huq\nAlhaji Bah\nChelsea McGovern\nCasey Tabatabai")