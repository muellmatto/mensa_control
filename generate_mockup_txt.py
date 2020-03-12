import csv
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

def create_mockup_txt(filename, size=14):
    school_ids = sample(range(1,8000), size)
    school_class = "{c}{n:02d}".format(
                c=choice(ascii_letters),
                n=int(choice(digits))
            )
    with open(filename, 'w') as f:
        f.write('"Interne ID-Nummer";"Nachname";"Vorname";"Klasse"\n')
        for i in school_ids:
            f.write('{};"{}";"{}";"{}"\n'.format(
                    i,
                    names.get_last_name(),
                    names.get_first_name(),
                    school_class
                    )
                )

create_mockup_txt('Test.TXT', size=10)
