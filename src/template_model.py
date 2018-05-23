import re
import os
import xml.etree.ElementTree as eT
from enum import Enum


XML_FILE_NAME = os.path.join(os.path.dirname(__file__), '..', 'ic-import.xsd')
TEMP_FILE_NAME = os.path.join(os.path.dirname(__file__), '..', 'temp.xsd')


class ESimpleType(Enum):
    """Enum for simpleType`s"""

    roleType = 'roleType'
    articleType = 'articleType'
    areaScienceType = 'areaScienceType'
    fieldScienceType = 'fieldScienceType'
    disciplineScienceType = 'disciplineScienceType'

    def __str__(self):
        return self.value


class EEnumeration(Enum):
    """Enum for enumeration`s"""

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


class EElement(Enum):
    """Enum for elements`s"""

    JOURNAL = 'journal'
    ISSUE = 'issue'
    ARTICLE = 'article'
    TYPE = 'type'
    LANGUAGE_VERSION = 'languageVersion'
    TITLE = 'title'
    ABSTRACT = 'abstract'
    PDF_FILE_URL = 'pdfFileUrl'
    PUBLICATION_DATE = 'publicationDate'
    REGISTRATION_DATE = 'registrationDate'
    PAGE_FROM = 'pageFrom'
    PAGE_TO = 'pageTo'
    DOI = 'doi'
    KEYWORDS = 'keywords'
    KEYWORD = 'keyword'
    AUTHORS = 'authors'
    AUTHOR = 'author'
    NAME = 'name'
    NAME2 = 'name2'
    SURNAME = 'surname'
    EMAIL = 'email'
    POLISH_AFFILIATION = 'polishAffiliation'
    ORDER = 'order'
    INSTITUTE_AFFILIATION = 'instituteAffiliation'
    DEPARTMENT_AFFILIATION = 'departmentAffiliation'
    SUBJECT_AFFILIATION = 'subjectAffiliation'
    ROLE = 'role'
    REFERENCES = 'references'
    REFERENCE = 'reference'
    UNPARSED_CONTENT = 'unparsedContent'
    DISCIPLINE_SCIENCES = 'disciplineSciences'
    AREA_SCIENCE = 'areaScience'
    FIELD_SCIENCE = 'fieldScience'
    DISCIPLINE_SCIENCE = 'disciplineScience'

    def __str__(self):
        return self.value


class Parser:
    def __init__(self, file=TEMP_FILE_NAME):
        self.__delete_xs(XML_FILE_NAME)
        self._tree = eT.parse(file)
        self._root = self._tree.getroot()

    @staticmethod
    def get_root_obj(file_name):
        tree = eT.parse(file_name)
        root = tree.getroot()
        return root

    @staticmethod
    def get_tree(file_name):
        tree = eT.parse(file_name)
        return tree

    @staticmethod
    def __delete_xs(xml_file):
        with open(xml_file, encoding='utf-8') as f:
            xml = f.read()

        # delete unnecessary xs schema
        xml_file = re.sub('xs:', '', xml)

        with open(TEMP_FILE_NAME, 'w', encoding='utf-8') as temp_file:
            temp_file.write(xml_file)

    def get_doc_text(self, tag, enumeration_value=None):
        """Returns documentation of given fragment

        Args:
            tag (ESimpleType|EElement): simpleType or element tag in which doc must be found.
            enumeration_value (EEnumeration): enumeration tag in which doc must be found.

        Returns:
            str: documentation text

        Raises:
            AttributeError: if doc in given fragment was not found."""
        try:
            if type(tag) is ESimpleType:
                simple_type = self._root.find(
                    './/simpleType[@name="{}"]'.format(tag))
                enumeration = simple_type.find(
                    './/enumeration[@value="{}"]'.format(enumeration_value))
                annotation = enumeration.find('.//annotation')
                doc = annotation.find('.//documentation')
                return doc.text
            else:  # if its EElement
                element = self._root.find('./element')
                req_element = element.find(
                    './/element[@name="{}"]'.format(tag))
                doc = req_element.find('.//documentation')
                return doc.text
        except AttributeError:
            print('Check file`s fragment, doc was not found')

    def set_doc_text(self, tag, enumeration_value=None, text=''):
        """Sets text to given fragment`s documentation

        Args:
            tag (ESimpleType|EElement): simpleType or element tag in which text must be set.
            enumeration_value (EEnumeration): enumeration tag in which text must be set.
            text (str): text for setting to documentation fragment.

        Raises:
            AttributeError: if doc in given fragment was not found."""
        try:
            if type(tag) is ESimpleType:
                simple_type = self._root.find(
                    './/simpleType[@name="{}"]'.format(tag))
                enumeration = simple_type.find(
                    './/enumeration[@value="{}"]'.format(enumeration_value))
                annotation = enumeration.getchildren()[0]
                doc = annotation.getchildren()[0]
                doc.text = text
            else:
                element = self._root.find('./element')
                req_element = element.find(
                    './/element[@name="{}"]'.format(tag))
                doc = req_element.find('.//documentation')
                doc.text = text
        except AttributeError:
            print('Check file`s fragment, doc was not found')

    def get_element_annotation(self):
        element = self._root.find('./element[@name="ici-import"]')
        annotation = element.find('.//annotation')
        doc = annotation.find('.//documentation')
        return doc.text

    def write_xml_to_file(self, file_name):
        self._tree.write(file_name)
