from .audition import Audition

class Role:
    

    def __init__(self, character_name):
        self.name = character_name



    # returns all of the auditions associated with this role 
    # so we need all the auditions list = and filter out with a.role == self
    # so [ a for a in Audition.all_auditions if a.role == self]
    @property
    def auditions(self):
        return [a for a in Audition.all_auditions if a.role == self]

    # returns a list of all names from the actors associated with this role
    # seems like we'll need a.actor[0].names from roles associated with auditions
    # since we already have auditions filitered associated with this role, we can 
    # use self.auditions
    @property
    def actors(self):
        return [a.actor for a in self.auditions]
    
    # returns a list of all of locations from the auditions associated with this role
    # so we'll stil need the self.auditions filtered list since we have association
    # we can get location from it ... 
    @property
    def locations(self):
        return [a.location for a in self.auditions]

    # returns a unique list of strings, for all of the character names
    # who have been hired... (a.k.a Black Panther)
    # okay, so have characters names inside this class .. so we'll need
    # the cls, we also may need an instance creation bucket of list
    # so like ... Role.all.append(self) and then under class all = []
    # so now we need people who have been hired... 
    # we may also need auditon filtered list... to grab the a.hired statements
    # for example, if we do....
    # def hired (self):
    # return [a.hired for a in self.auditions if self.hired == True]
    # we should get all of the hired people in this list only

    def hired(self):
        return [a.role for a in self.auditions if a.hired == True]

    @classmethod
    def silver_screen(cls):
        pass 
