import ipdb
from lib import *

# Test your code below...
vader = Role( 'Darth Vader' )
thanos = Role( 'Thanos' )



matthew = Actor( 'Matthew Longshore' )
lebron = Actor( 'Lebron James' )
roman = Actor( 'Roman Reigns' )




a1 = Audition( 'Atlanta', True, vader, matthew )
a2 = Audition( 'Akron', False, vader, lebron )
a3 = Audition( 'Pensacola', True, thanos, roman )
a4 = Audition( 'Charlotte', True, thanos, lebron)




# the below line allows us to stop & try stuff!
ipdb.set_trace()