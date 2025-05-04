class C:
    def method(self):
        print("method called!")

c = C()
r = weakref.ref(c.method)
r()
r = weakref.WeakMethod(c.method)
r()

r()()

del c
gc.collect()

r()

import weakref
class Object:
    pass

o = Object()
r = weakref.ref(o)
o2 = r()
o is o2

del o, o2
print(r())

# r is a weak reference object
o = r()
if o is None:
    # referent has been garbage collected
    print("Object has been deallocated; can't frobnicate.")
else:
    print("Object is still live!")
    o.do_something_useful()

import weakref

class ExtendedRef(weakref.ref):
    def __init__(self, ob, callback=None, /, **annotations):
        super().__init__(ob, callback)
        self.__counter = 0
        for k, v in annotations.items():
            setattr(self, k, v)

    def __call__(self):
        """Return a pair containing the referent and the number of
        times the reference has been called.
        """
        ob = super().__call__()
        if ob is not None:
            self.__counter += 1
            ob = (ob, self.__counter)
        return ob

import weakref

_id2obj_dict = weakref.WeakValueDictionary()

def remember(obj):
    oid = id(obj)
    _id2obj_dict[oid] = obj
    return oid

def id2obj(oid):
    return _id2obj_dict[oid]

class TempDir:
    def __init__(self):
        self.name = tempfile.mkdtemp()

    def remove(self):
        if self.name is not None:
            shutil.rmtree(self.name)
            self.name = None

    @property
    def removed(self):
        return self.name is None

    def __del__(self):
        self.remove()

class SimpleNamespace:
    def __init__(self, mapping_or_iterable=(), /, **kwargs):
        self.__dict__.update(mapping_or_iterable)
        self.__dict__.update(kwargs)

    def __repr__(self):
        items = (f"{k}={v!r}" for k, v in self.__dict__.items())
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def __eq__(self, other):
        if isinstance(self, SimpleNamespace) and isinstance(other, SimpleNamespace):
           return self.__dict__ == other.__dict__
        return NotImplemented

class ComplexNamesspace:
    def __init__(other, mapping_or_iterable=(), /, **kwargs):
        other.__dict__.update(mapping_or_iterable)
        other.__dict__.update(kwargs)

    def __repr__(other):
        items = (f"{k}={v!r}" for k, v in other.__dict__.items())
        return "{}({})".format(type(other).__name__, ", ".join(items))

    def __eq__(other, self):
        if isinstance(other, ComplexNamespace) and isinstance(self, ComplexNamespace):
            return other.__dict__ == self.__dict__
        return NotImplemented

import pprint
stuff = ['wind', 'ice', 'lightning', 'fire', 'imaginary', 'quantum', 'physical']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=7)
pp.pprint(stuff)

pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(stuff)

tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',
('parrot', ('fresh fruit',))))))))
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(tup)
