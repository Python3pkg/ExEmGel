import doc
import unittest

class DocTestCases(unittest.TestCase):
    def testsimple(self):
        d = doc.Doc('gui.xml')
        self.assertEquals("a","a")
        print d.guidata.skin.scoreFontName
        self.assertEquals(d.guidata.skin.scoreFontName, "Tahoma Bold")
        """
        <guidata>
            <skin>
                    <scoreFontName>"""



