
class Audition:
    
    all = []

    def __init__( self, location, hired, role, actor ):
        self.location = location
        self.hired = hired
        self.role = role
        self.actor = actor
        Audition.all.append( self )

    def call_back( self, hired ):
        self.hired = hired
