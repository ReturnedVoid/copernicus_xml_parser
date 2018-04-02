import re
import xml.etree.ElementTree as eT
from enum import Enum


class ESimpleType(Enum):
    roleType = 'roleType'
    articleType = 'articleType'
    areaScienceType = 'areaScienceType'
    fieldScienceType = 'fieldScienceType'
    disciplineScienceType = 'disciplineScienceType'

    def __str__(self):
        return self.value


class EEnumeration(Enum):
    LEAD_AUTHOR = 'LEAD_AUTHOR'
    AUTHOR = 'AUTHOR'
    RESEARCH_PROJECT = 'RESEARCH_PROJECT'
    RESEARCH_EXECUTION = 'RESEARCH_EXECUTION'
    STATISTICAL_ANALYSIS = 'STATISTICAL_ANALYSIS'
    DATA_INTERPRETATION = 'DATA_INTERPRETATION'
    MANUSCRIPT_PREPARATION = 'MANUSCRIPT_PREPARATION'
    LITERATURE_OVERVIEW = 'LITERATURE_OVERVIEW'
    RESEARCH_FUNDING = 'RESEARCH_FUNDING'
    ORIGINAL_ARTICLE = 'ORIGINAL_ARTICLE'
    REVIEW_ARTICLE = 'REVIEW_ARTICLE'
    SHORT_COMMUNICATION = 'SHORT_COMMUNICATION'
    COMMENTARY_ON_THE_LAW = 'COMMENTARY_ON_THE_LAW'
    SCIENTIFIC_REVIEW = 'SCIENTIFIC_REVIEW'
    GUIDELINES = 'GUIDELINES'
    POPULAR_SCIENCE_ARTICLE = 'POPULAR_SCIENCE_ARTICLE'
    OTHERS_NONCITABLE = 'OTHERS_NONCITABLE'
    OTHERS_CITABLE = 'OTHERS_CITABLE'
    CASE_STUDY = 'CASE_STUDY'
    NUMBER1 = '1'
    NUMBER2 = '2'
    NUMBER3 = '3'
    NUMBER4 = '4'
    NUMBER5 = '5'
    NUMBER6 = '6'
    NUMBER7 = '7'
    NUMBER8 = '8'
    NUMBER9 = '9'
    NUMBER10 = '10'
    NUMBER11 = '11'
    NUMBER12 = '12'
    NUMBER13 = '13'
    NUMBER14 = '14'
    NUMBER15 = '15'
    NUMBER16 = '16'
    NUMBER17 = '17'
    NUMBER18 = '18'
    NUMBER19 = '19'
    NUMBER20 = '20'
    NUMBER21 = '21'
    NUMBER22 = '22'
    NUMBER23 = '23'
    NUMBER24 = '24'
    NUMBER25 = '25'
    NUMBER26 = '26'
    NUMBER27 = '27'
    NUMBER28 = '28'
    NUMBER29 = '29'
    NUMBER30 = '30'
    NUMBER31 = '31'
    NUMBER32 = '32'
    NUMBER33 = '33'
    NUMBER34 = '34'
    NUMBER35 = '35'
    NUMBER36 = '36'
    NUMBER37 = '37'
    NUMBER38 = '38'
    NUMBER39 = '39'
    NUMBER40 = '40'
    NUMBER41 = '41'
    NUMBER42 = '42'
    NUMBER43 = '43'
    NUMBER44 = '44'
    NUMBER45 = '45'
    NUMBER46 = '46'
    NUMBER47 = '47'
    NUMBER48 = '48'
    NUMBER49 = '49'
    NUMBER50 = '50'
    NUMBER51 = '51'
    NUMBER52 = '52'
    NUMBER53 = '53'
    NUMBER54 = '54'
    NUMBER55 = '55'
    NUMBER56 = '56'
    NUMBER57 = '57'
    NUMBER58 = '58'
    NUMBER59 = '59'
    NUMBER60 = '60'
    NUMBER61 = '61'
    NUMBER62 = '62'
    NUMBER63 = '63'
    NUMBER64 = '64'
    NUMBER65 = '65'
    NUMBER66 = '66'
    NUMBER67 = '67'
    NUMBER68 = '68'
    NUMBER69 = '69'
    NUMBER70 = '70'
    NUMBER71 = '71'
    NUMBER72 = '72'
    NUMBER73 = '73'
    NUMBER74 = '74'
    NUMBER75 = '75'
    NUMBER76 = '76'
    NUMBER77 = '77'
    NUMBER78 = '78'
    NUMBER79 = '79'
    NUMBER80 = '80'
    NUMBER81 = '81'
    NUMBER82 = '82'
    NUMBER83 = '83'
    NUMBER84 = '84'
    NUMBER85 = '85'
    NUMBER86 = '86'
    NUMBER87 = '87'
    NUMBER88 = '88'
    NUMBER89 = '89'
    NUMBER90 = '90'
    NUMBER91 = '91'
    NUMBER92 = '92'
    NUMBER93 = '93'
    NUMBER94 = '94'
    NUMBER95 = '95'

    def __str__(self):
        return self.value


class Parser:
    def __init__(self):
        self._output_file_name = 'test.xsd'
        self._source_file_name = 'ic-import.xsd'
        self._tree = None
        self._root = None
        self._parse_xml(self._source_file_name)

    def _parse_xml(self, xml_file):
        with open(xml_file, encoding='utf-8') as f:
            xml = f.read()

        xml_file = re.sub('xmlns:xs="http://www.w3.org/2001/XMLSchema" ', '', xml)
        xml_file = re.sub('xs:', '', xml)

        file = open(self._output_file_name, 'w', encoding='utf-8')
        file.write(xml_file)
        file.close()

        self._tree = eT.parse(self._output_file_name)
        self._root = self._tree.getroot()

    def get_doc_text(self, simple_type_name, enumeration_value):
        simple_type = self._root.find('.//simpleType[@name="{}"]'.format(simple_type_name))
        enumeration = simple_type.find('.//enumeration[@value="{}"]'.format(enumeration_value))
        annotation = enumeration.getchildren()[0]
        doc = annotation.getchildren()[0]
        return doc.text

    def set_doc_text(self, simple_type_name, enumeration_value, text):
        simple_type = self._root.find('.//simpleType[@name="{}"]'.format(simple_type_name))
        enumeration = simple_type.find('.//enumeration[@value="{}"]'.format(enumeration_value))
        annotation = enumeration.getchildren()[0]
        doc = annotation.getchildren()[0]
        doc.text = text

    def write_xml_to_file(self):
        self._tree.write(self._output_file_name)


class Documentation:
    def __init__(self, doc_obj):
        self._doc = doc_obj
        self._text = self._doc.text

    def get_text(self):
        return self._text

    def set_text(self, text):
        self._doc.text = text


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
        self._els = self._schema.findall('element')

    def get_simple_types(self):
        return [SimpleType(obj) for obj in self._objects]

    def get_elements(self):
        return [Element(obj) for obj in self._els]


class Element:
    def __init__(self, el_obj):
        self._element = el_obj
        self._annotations = self._element.findall('annotation')
        self._complex_types = self._element.findall('complexType')

    def get_annotations(self):
        return [Annotation(obj) for obj in self._annotations]

    def get_complex_types(self):
        return [ComplexType(obj) for obj in self._complex_types]


class ComplexType:
    def __init__(self, ct_obj):
        self._complex_type = ct_obj
        self._sequences = self._complex_type.findall('sequence')

    def get_sequences(self):
        return [Sequence(obj) for obj in self._sequences]


class Sequence:
    def __init__(self, seq_obj):
        self._sequence = seq_obj
        self._elements = self._sequence.findall('element')

    def get_elements(self):
        return [Element(obj) for obj in self._elements]


if __name__ == "__main__":
    parser = Parser()
    text = parser.get_doc_text(ESimpleType.disciplineScienceType, EEnumeration.NUMBER7)
    print(text)

