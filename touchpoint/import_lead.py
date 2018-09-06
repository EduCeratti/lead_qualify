import os
from touchpoint.models import Touchpoint
from datetime import datetime



def do_import():    
    
    read_users = readFile()

    for item in read_users:

        # if user not already exists
        if Touchpoint.objects.filter(username=item[0]):
            pass 
        else:
            new_touchpoint = Touchpoint(username=item[0], modified_date=datetime.now())
            new_touchpoint.save()

    return "Imported from origin"
    
def readFile():

    rows = []
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'lead.txt')

    with open(file_path, 'r') as f:
        for line in f:
            columns = line.strip().split(',')
            rows.append(columns)
    
    return rows