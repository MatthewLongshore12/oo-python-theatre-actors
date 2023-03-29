from .audition import Audition

class Role:
    
    all = []

    def __init__( self, character_name ):
        self.character_name = character_name
        Role.all.append( self )

    @property
    def auditions( self ):
        return [ r for r in Audition.all if r.role == self ]

    @property
    def actors( self ):
        return [ r.actor.name for r in self.auditions ]

    @property
    def locations( self ):
        return [ r.location for r in self.auditions ]

    @classmethod
    def silver_screen( cls ):
        return f"Hired characters are { [ a.role.character_name for a in Audition.all if a.hired == True ] }"