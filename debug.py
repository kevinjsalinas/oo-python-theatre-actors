import ipdb
from lib import *


# Roles -- < Auditions > -- Actors

# Test your code below...

peter = Actor("Peter")
jon = Actor("Jon")

john_wick = Role("John Wick")
spiderman = Role("Spiderman")
black_panther = Role("Black Panther")

audition1 = Audition("Miami", False, john_wick, peter)
audition2 = Audition("New York", False, spiderman, jon)
audition3 = Audition("Alabama", False, black_panther, jon)
audition4 = Audition("Mexico", True, black_panther, peter)




# the below line allows us to stop & try stuff!
ipdb.set_trace()