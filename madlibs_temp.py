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
        user_input.strip("\n")
        while  user_input not in  ['vacation' ,'park' ,'zoo' ,'arcade']:
            user_input = input("Choose a genre: vacation/park/zoo/arcade ")
        else:    
            return self.d[user_input]

                
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
        """ Iterates through the story of the genre picked by the user, locates the words in brackets and returns a list of the words without the brackets
        
        Side Effects: 
        locates the words that must be replaced by the user

        Returns:
        word_types(list): a list of the word types that need to be replaced by the user's input   
        """
        user_words = []
        for word in self.output:
            user_response = input(f"Please enter a(n) {word}: ")
            user_words.append(user_response)
        return user_words
        
    def generator(self, template, user_answers): #Alhaji
        """Uses re.sub function to substitute all words inside brackets with "{}"
            then uses .format funtion to replace the "{}" with words in self.output in order
        
        Side effects:
            self.story gets updated
        """
   
        brackets_sub = re.sub(r"\[([^\]]+)\]", "{}", template)
        self.story = brackets_sub.format(*user_answers)
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
    temp = Template(file)
    x = temp.user_choice()
    blanks = temp.read(x)
    new_words = temp.user_answers(blanks)
          
    print(new_words)
    answer = input("Play Again? y/n: ")  
    if answer == "y":
        main(file)
    elif answer == "n":
        print("Thanks for playing!\nCreated by: Amanu Huq, Alhaji Bah, Chelsea McGovern, Casey Tabatabai")
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)