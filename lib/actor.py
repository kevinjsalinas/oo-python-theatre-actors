from .audition import Audition

class Actor:
    
    def __init__(self, actor_name):
        self.name = actor_name


    #list of auditions 
    # that the actor has attended so we need the actor attribute
    # from the list
    # and it's returning a list of auditions 

    @property
    def auditions(self):
        return [a for a in Audition.all_auditions if a.actor == self ]

    # returns a list of ROLES the actor auditioned for... 
    # so we need another list, and specifically get out the role of that 
    # actor and right now we already have a list of auditions the 
    # actor already has attended so we can filter from that using
    # [ list of auditions of the actor , filter out roles.]
    @property
    def roles(self):
        return [a.role for a in self.auditions]

    # role.name we need .. and the best way to get it is from 
    # through auditions is how we can get it... and we must filter it
    # from Audition.role instance ...
    # components... we have
        # self.roles
        # self.roles[0].name gives us a name string
        # len(self.roles) = 2 of things inside 

    def len(self):
        length = len(self.roles)
        return length

    def characters(self):
        new_list = []
        if len(self.roles) > 0:
            name = self.roles[0].name.pop()
            new_list.append(self.roles[0].name)
        
#notes

    # list of all the character names this actor has auditions for
    # porentially we can filter from the self. audtions because the actor
    # is already here and now we can grab a.role from auditions 
    # character names is inside Role but we can grab it from Auditions
    # auditions.role because it's there 
    # so in theory we can do 
    # list [ a.role ]
    # [roles if ] -- okay so now we know that 
    # self.roles[0].name does give you the character name yo hoo!!!
    # so if i = len(self.roles)

    # new_list = []
    # we could do if len(self.roles) = 0:
                #new_list.append(self.roles[0])
            # elif if len(self.roles) = 1 
                #new_listappend(self.roles[1]) blah blah
