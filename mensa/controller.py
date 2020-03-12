from models import (
        Student,
        Log
        )

# planning ...

def add_student(school_id, name, school_class, gets_a_meal=False):
    return False

def register_card(student, card_id):
    return False

def unregister_card(student=None, card_id=None):
    '''
    remove card_id from Student, either by Student or Card_id)
    '''
    return False

def remove_student(school_id=None, name=None, school_class=None):
    return False

def update_student(school_id=None, name=None, school_class=None, gets_a_meal=None, card_id=None):
    return False

def gets_a_meal(card_id):
    return False
