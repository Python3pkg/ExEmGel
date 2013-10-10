import doc
import unittest

class DocTestCases(unittest.TestCase):
    def testsimple(self):
        d = doc.Doc('gui.xml')
        self.assertEquals(d.guidata.skin.scoreFontName, "Tahoma Bold")


    def testlist(self):
        d = doc.Doc('gui.xml')
        self.assertEquals(type(d.guidata.skin.nextBlockX.line),  tuple)
        self.assertEquals(d.guidata.skin.nextBlockX.line[1], "206" )

    def testlistofnodes(self):
        d = doc.Doc('simple.xml')
        self.assertEquals(type(d.breakfast_menu.food),  tuple)
        self.assertEquals(d.breakfast_menu.food[1].name, "Strawberry Belgian Waffles" )
