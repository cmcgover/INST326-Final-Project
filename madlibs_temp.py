class Template:
    '''Generates the template
    
    '''
    def genre(self, genre):
        
        """ Choose the genre of the story to be generated
       
        Args:
        genre(str) User chooses between different genres such as comedy, horror etc.
        Side effects:
        Generates a story of the genre choosen
        
        """
        genre = input("What type of story would you like? comedy/horror/romance/celebrity ")
        
    def format(self): #Casey
        """ Creating the format of the Mad Libs template regarding word count, # of type of words, etc.
        
        Args:
        num_nouns(int): Total # of nouns in story
        num_verbs(int): Total # of verbs in story
        num_adverbs(int): Total # of adverbs in story
        num_adjectives(int): Total # of adjectives in story
        
        Side effects:
        # of words for each word type in a dictionary
        """
        
    def generator(self, story):
        """Compiles story into a Mad Libs template text file
        Arg:
        story(dict): total words in mad libs template
        Side effects:
        file(str): text file 
        """