from model.person import Person
import random
import string


class PersonHelper:
    def __init__(self, app):
        self.app = app

    def random_person(self):
        return Person(name=self.random_name("n", 2, 10), lastname=self.random_name("l", 2, 10),
                      email=self.random_email("e", 3, 8), mobile=self.random_mobile())

    def random_name(self, prefix, minlen, maxlen):
        return prefix + "".join([random.choice(string.ascii_letters) for i in range(random.randint(minlen, maxlen))])

    def random_email(self, prefix, minlen, maxlen):
        login = prefix + "".join([random.choice(string.ascii_letters) for i in range(random.randint(minlen, maxlen))])
        host = "".join([random.choice(string.ascii_lowercase) for i in range(random.randint(minlen, maxlen))])
        domain_zone = "".join([random.choice(string.ascii_lowercase) for i in range(random.randint(2, 3))])
        return login + "@" + host + "." + domain_zone

    def random_mobile(self):
        return "9" + "".join([random.choice(string.digits) for i in range(9)])
