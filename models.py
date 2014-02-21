from faker import Factory
import json
import uuid


class Person:
    def __init__(self, **kwargs):
        fake = Factory.create()
        self.id = str(uuid.uuid4())
        self.name = kwargs.get('name', fake.name())
        self.address = kwargs.get('address', fake.address())
        self.text = kwargs.get('text', fake.text())
        self.date_joined = kwargs.get('date_joined', fake.iso8601())


    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' %self.name

    def __repr__(self):
        return self.name

if __name__ == '__main__':
    p = [Person().__dict__ for i in range(1)]
    print json.dumps(p)

