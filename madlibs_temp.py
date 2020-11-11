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
        