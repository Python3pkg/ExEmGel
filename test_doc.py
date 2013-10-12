import doc
import unittest
import StringIO

class DocTestCases(unittest.TestCase):
    def testsimple(self):
        s = StringIO.StringIO("""\
<?xml version="1.0"?>
<guidata>
    <skin>
        <scoreFontName>Tahoma Bold</scoreFontName>
        <scoreFontHeight>20</scoreFontHeight>
        <blockSize>16</blockSize>
        <nextBlockX>
            <line>205</line>
            <line>206</line>
            <line>207</line>
            <line>105</line>
        </nextBlockX>
        <backgroundFile>"back.bmp"</backgroundFile>
    </skin>
</guidata>
""")
        d = doc.Doc(s)
        self.assertEquals(d.guidata.skin.scoreFontName, "Tahoma Bold")



