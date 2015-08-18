import xml.etree.ElementTree as etree
n = int(raw_input())
s = ""
count = 0
for i in range(n):
    s = s + raw_input()
tree = etree.ElementTree(etree.fromstring(s))
root = tree.getroot()
elements = root.findall(".//*")
for item in elements:
    count += len(item.attrib)
print count + len(root.attrib)
