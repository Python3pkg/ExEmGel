

class Node(object):
    def __init__(self, element):
        self._element = element

    def _make_new_node_or_leaf(self, new_element):
        if(len(list(new_element.iter())) == 1):
            return new_element.text
        else:
            return Node(new_element)
    

    def __getattr__(self, attr):
        if attr in self.__dict__:
            print "we has " , attr
            return self.__dict__[attr]
        l = list(self._element.iter(attr))
        print "len(l) = %d" % len(l) 
        if len(l) == 1:
            return self._make_new_node_or_leaf(l[0])
        elif len(l) > 1:
            return tuple([self._make_new_node_or_leaf(e) for e in l])
                
        
        raise AttributeError("%r object has no attribute %r" %
                                         (self.__class__, attr))

    
