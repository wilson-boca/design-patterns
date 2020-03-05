class Singleton(object):
    # overwriting __new__ method, this is how we ensure that it returns always the same object
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s0 = Singleton()
s1 = Singleton()
print(s0)
print(s1)
print(s0 == s1)
