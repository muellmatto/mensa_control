import unittest
from random import (
        sample,
        randint,
        random,
        choice
        )
from string import (
        ascii_letters,
        digits
        )
import names
#gen random names:
#names.get_full_name()

from mensa.models import db, Student, orm

db.bind(provider='sqlite', filename=':memory:')
db.generate_mapping(create_tables=True)

class TestStudent(unittest.TestCase):
    def test_add_class(self):
        number_of_students = randint(20,30)
        school_class = "{c}{n:02d}".format(
                    c=choice(ascii_letters),
                    n=int(choice(digits))
                )
        ids = sample(range(1,8000), number_of_students)
        for i in ids:
            with orm.db_session:
                p = Student(
                        school_id = i,
                        name = names.get_full_name(),
                        school_class = school_class,
                        gets_a_meal = random() < 0.5
                        )
