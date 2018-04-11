import xml.etree.ElementTree as ET
import sqlite3

# ask user if she wants to parse a different file
fname = input('Importing Library.xml. Press enter to proceed or enter file name to load a different file:')
# if not then proceed with default
if (len(fname) < 1): fname="Library.xml"
library = ET.parse("Library.xml")
