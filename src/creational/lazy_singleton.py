class Singleton(object):
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('init called without instance')
        else:
            print('Instance properly created...', self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s0 = Singleton()
Singleton.get_instance()
s1 = Singleton()