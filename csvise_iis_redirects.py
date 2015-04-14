#!/usr/bin/python

import re
from xml.etree import ElementTree

doc = ElementTree.parse("/home/hillsy/Desktop/rewriterules.config")

f = open('output.csv', 'w')
f.write("Match,Redirect\n")

rules = doc.getroot()

def urlise(str):

    pattern = "^https?://"

    if re.match(pattern, str):
        out = str
    else:
        out = "http://www.hscic.gov.uk/" + str

    return out

for rule in rules:
    for node in rule.getchildren():
        line = ""
        if node.tag == "match":
            line += "%s," % node.attrib["url"]
        if node.tag == "action":
            try: # some actions aren't rewrites/redirects
                line += "%s\n" % (urlise(node.attrib["url"]))
            except:
                line += "No redirect URL specified\n"

        f.write(line)

f.close()
