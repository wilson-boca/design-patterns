class Singleton(object):
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('init called without instance')
        else:
            print('Instance properly created...')

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s0 = Singleton()
print(s0.get_instance())
s1 = Singleton()
print(s1.get_instance())
Singleton.get_instance()
print(s0.get_instance())
print(s1.get_instance())