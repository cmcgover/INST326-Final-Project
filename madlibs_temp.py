                                            
from argparse import ArgumentParser                                          
import re
import sys

class Template:
    """
    This class will formulate a madlib game story. The user will choose a genre from a template, and from their be given blanks to fill. 
    
    Attributes: 
        self.story(string): stores the completed story with user input for the blanks
        self.output(list): a list of all the words in brackets for the particular chosed genre from the user
        self.genre(txt): takes the template as "file"
        self.user_words(list): is the words that are selected from the user to rpelace the blanks that are stored in a list
        self.user_input(str): The genre that is chosen by the user for the template 
    
    """
    
    def __init__(self,file): #Chelsea
        """Initializes content and output words
        Args: 
            file(str): name of the template file
        
        Side effects: 
            Intialized variables that are described in class doc string
        """
        self.story = " "
        self.output = []
        self.genre(file)
        self.user_words = []
        self.user_input= ""
        
        
    def genre(self, file): #Amanu
        """ Choose the genre of the story to be generated
        Args:
            filename(txt): User chooses between different genres such as vacation, park, zoo, or arcade to be used
            as a template.
        
        Side Effects: 
            self.content = opens file to read
            self.d (dict): Stores story from template that user chose. genre title is key and the story is the value
    
        """    
        open_file = open(file, "r")
        self.content = open_file.read()
        self.d = {}
        x = self.content.split("\n\n")
        for template in x: 
            y = template.strip().split(":")
            self.d[y[0].lower()] = y[1]
         
    def user_choice(self): #Amanu
        """ 
        Side effects: 
            self.user_input (str): asks for user input for genre based given the options of vacation, park, zoo, or aracde. 
        
        Returns: 
            self.d[user_input](dict): the story based upon the genre chosen
        """
        self.user_input  = input("Choose a genre: vacation/park/zoo/arcade ")
        self.user_input.strip("\n")
        while self.user_input not in  ['vacation' ,'park' ,'zoo' ,'arcade']:
            self.user_input = input("Choose a genre: vacation/park/zoo/arcade ")
        else:    
            return self.d[self.user_input]

                
    def read(self,template): #Chelsea
        """ Finds "missing words" in the chosen story and returns a list of what needs to be filled in by the user.
        Args:
            template(str): the story generated based on what genre the user has chosen 
        
        Returns:
            self.output(list): the words that need to be replaced into the story
        """
        self.output = []
        keywords=['[adjective]', '[noun]', '[plural-noun]', '[game]', '[plant]',
                  '[verb-ending-in-ing]','[place]','[part-of-body]',
                  '[number]','[adverb]','[past-tense-verb]','[verb]']
        t = template.split(" ")
        for word in t:
            for item in keywords:
                if item in word:
                    item = item[1:len(item) - 1]
                    self.output.append(item)
        
        return self.output
    
    def user_answers(self,template): #Casey
        """ Iterates through the words types within the genre that need to be replaced,
        and asks the user for new words
        
        Args:
            template(str): the story generated based on what genre the user has chosen
        
        Side Effects: 
            Creates an empty string named user_words that will be filled with the users answers

        Returns:
            user_words(list): Returns a list of the user's answers in the correct order 
        """
        self.user_words = []
        for word in self.output:
            user_response = input(f"Please enter a(n) {word}: ")
            self.user_words.append(user_response)
        return self.user_words
        
    def generator(self, template): #Alhaji
        """Uses re.sub function to substitute all words inside brackets with "{}"
            then uses .format funtion to replace the "{}" with words in self.user_words in order
        
        Args:
            template(str): the story generated based on what genre the user has chosen 
            
        Side Effects:
            brackets_sub: becomes a string with words inside brackets replaced with "{}"
            self.story (str):gets updated to a string with "{}" replaced with words the user inputed in proper order
        
        Returns:
            self.story(str): the completed story with the blanks filled 
        """
        brackets_sub = re.sub(r"(\[[^\]]+\])", "{}", self.d[self.user_input])
        self.story = brackets_sub.format(*self.user_words)
        return self.story
    
def parse_args(argList):
    """Parses command-line arguments.

    The following required command-line arguments are defined:

    genre: a txt file

    Args:
        arglist (list of str): a list of command-line arguments.

    Returns:
        namespace: a namespace with the story replaced with the user's inputted words.
    """
    parser = ArgumentParser()
    parser.add_argument("filename", help ="path to txt file called madlibstemplate.txt")
    return parser.parse_args(argList)


def main(file):
    """Generates the story based on what genre the user selects. Then prompts user to fill in word so a
    story is generated.
    
    Args: 
        file(txt): Template of the file
    
    Side effects: 
        temp = instance of the Template class with file as an arguement. The prompted with a print statement to pick genre. 
        x = by temp.user_choice , user is suppoed to input the words for the blanks to complete the sotry 
        blanks = stores the words in brackets  in a list
        new_words = temp.user_answers(blanks) asks for users choice for words to be replaced in blanks
        story = genereated story with the user_words inputted 
        answer(str) = through input statement asks if user wants to play again. Then story is printed.

    Returns:
        story(str): The final template with the words the user has inputted
    """
    temp = Template(file)
    print("Welcome to the MadLibs game! Pick a genre to begin.\n")
    x = temp.user_choice()
    print("\nFill in the following words to complete the story!")
    blanks = temp.read(x)
    new_words = temp.user_answers(blanks)
    story = temp.generator(new_words)      
    print("\n", story)
    
    answer = input("\nPlay Again? y/n: ")
    while answer != "y" and answer != "n":
        answer = input("Please enter 'y' or 'n': ")
            
    if answer == "y":
        main(file)
    elif answer == "n":
        print("\nThanks for playing!\nCreated by: Amanu Huq, Alhaji Bah, Chelsea McGovern, Casey Tabatabai")
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)