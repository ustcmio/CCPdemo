import uuid


class Member(object):
    def __init__(self, name, ):
        self.uid = uuid.uuid1()
        self.name = name