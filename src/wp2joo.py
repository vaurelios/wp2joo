import getopt
from sqlobject.sqlbuilder import *
import xml.etree.ElementTree as ET


class Wp2Joo(object):
    """ Principal class
    """
    _valuelist = []
    def __init__(self, prefix):
        """ Initialize Wp2Joo class
        Attributes:
            prefix:    Prefix for use in content table, for example 'jo_'
        """
        self.posts = []
        self.users = []
        self.cats  = []
        self.tags  = []
    def _authors(self):
        """ Find authors in XML and create SQL users
        """
        root = self._et.getroot()
        ns = {"wp": "http://wordpress.org/export/1.2/"}
        
        for c in root.findall("/channel/wp:authors", ns):
            for tag in c:
                if tag.tag[33:] == "author_id":
                    self.users.append((''))
    def loadXML(self, filename):
        """ Load XML (Exported by Wordpress) and parse
        Attributes:
            filename:    XML file to load
        """
        self._et = ET.parse(filename)
    def dump(self, filename):
        """ Convert XML to SQL Dump format
        Attributes:
            filename:    File Name to save
        """
        pass