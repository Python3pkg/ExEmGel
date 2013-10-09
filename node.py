

class Node(object):
    def __init__(self, element):
        self._element = element

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__dict__[attr]
        l = list(self._element.iter(attr))
        print "len(l) = %d" % len(l) 
        if len(l) > 0:
            new_element = l[0]
            print type(new_element)
            if(len(list(new_element.iter())) == 1):
                return new_element.text
            return Node(new_element)
                
        
        raise AttributeError("%r object has no attribute %r" %
                                         (self.__class__, attr))

    
