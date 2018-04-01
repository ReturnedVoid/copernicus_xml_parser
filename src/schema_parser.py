import re
import xml.etree.ElementTree as eT


class Documentation:
    def __init__(self, doc_obj):
        self._doc = doc_obj
        self._text = self._doc.text

    def get_text(self):
        return self._text


class Annotation:
    def __init__(self, ann_obj):
        self._annotation = ann_obj
        self._documentations = self._annotation.findall('documentation')

    def get_documentations(self):
        return [Documentation(obj) for obj in self._documentations]


class Enumeration:
    def __init__(self, enum_obj):
        self._enumeration = enum_obj
        self._annotations = self._enumeration.findall('annotation')

    def get_annotations(self):
        return [Annotation(obj) for obj in self._annotations]


class Restriction:
    def __init__(self, restr_obj):
        self._restriction = restr_obj
        self._enumerations = self._restriction.findall('enumeration')

    def get_enumerations(self):
        return [Enumeration(obj) for obj in self._enumerations]


class SimpleType:
    def __init__(self, simple_type_obj):
        self._simple_type = simple_type_obj
        self._restrictions = self._simple_type.findall('restriction')

    def get_restrictions(self):
        return [Restriction(obj) for obj in self._restrictions]


class Root:
    def __init__(self, root_obj):
        self._root = root_obj
        self._schemas = self._root.findall('schema')

    def get_schemas(self):
        return [Schema(obj) for obj in self._schemas]


class Schema:
    def __init__(self, schema_obj):
        self._schema = schema_obj
        self._objects = self._schema.findall('simpleType')

    def get_simple_types(self):
        return [SimpleType(obj) for obj in self._objects]


def parse_xml(xml_file):
    with open(xml_file, encoding='utf-8') as fobj:
        xml_file = fobj.read()

    xml_file = re.sub('xmlns:xs="http://www.w3.org/2001/XMLSchema" ', '', xml_file)
    xml_file = re.sub('xs:', '', xml_file)

    file = open('test.xsd', 'w', encoding='utf-8')
    file.write(xml_file)
    file.close()

    tree = eT.parse('test.xsd')

    root = Schema(tree.getroot())

    print(root.get_simple_types()[0]
          .get_restrictions()[0]
          .get_enumerations()[0]
          .get_annotations()[0]
          .get_documentations()[0]
          .get_text())


if __name__ == "__main__":
    parse_xml("ic-import.xsd")