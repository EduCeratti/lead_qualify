import os
from touchpoint.models import Touchpoint
from datetime import datetime



def do_qualify():    

    # Steps
    #1 - Read all leads in imported status
    #2 - Aplly rules
    #3 - Update lead information

    list_to_qualify = Touchpoint.objects.filter(status='IM')

    # Read all imported leads and do anything
    for item in list_to_qualify:
        
        # Controls rules
        if 'a' in item.username:
            item.status='QL'
            item.rule_approved=1
    
        item.save()         

    return "Lead task qualify - DONE"
