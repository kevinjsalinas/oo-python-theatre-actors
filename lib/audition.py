
class Audition:

    all_auditions = []

    def __init__(self, location, hired, role_instance, actor_instance):
        self.location = location
        self.hired = hired
        self.role = role_instance
        self.actor = actor_instance
        Audition.all_auditions.append(self)

    # do i really need getter and setters? It breaks when I do this
    # @property
    # def role(self):
    #     return self.role

    # @property
    # def actor(self):
    #     return self.actor

    @property
    def call_back(self):
        self.hired = True
    
        

    
