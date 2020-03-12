from datetime import datetime
from pony import orm

db = orm.Database()

class Student(db.Entity):
    '''
        school_id:int, name:str, school_class:str, gets_a_meal:bool
    '''
    school_id = orm.PrimaryKey(int, auto=False)
    name = orm.Required(str)
    school_class = orm.Required(str)
    gets_a_meal = orm.Required(bool)
    card_id = orm.Optional(int)
    uses = orm.Set("Log")

    def __repr__(self):
        s = "<User(id={id}, name={name}, school_class={school_class}, Meal={meal})>"
        return s.format(
                id=self.id,
                name=self.name,
                school_class=self.school_class,
                meal=str(self.gets_a_meal)
                )


class Log(db.Entity):
    student = orm.Required("Student")
    date = orm.Required(datetime)
    # or date + count ....
