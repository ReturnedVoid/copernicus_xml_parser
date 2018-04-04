from sample.template_model import *
from sample.parser import *
from sample.issue_model import *


def test_get_doc_with_valid_args():
    parser = Parser()
    assert parser.get_doc_text(ESimpleType.roleType, EEnumeration.AUTHOR) \
           == 'Author (including co-author) / Autor (w tym Współautor)'


def test_get_doc_after_set():
    test_text = 'Test'
    parser = Parser()
    parser.set_doc_text(ESimpleType.roleType, EEnumeration.AUTHOR, test_text)
    text = parser.get_doc_text(ESimpleType.roleType, EEnumeration.AUTHOR)
    assert text == test_text


def test_get_element_annotation():
    parser = Parser()
    expected = 'Schemat importu danych'
    assert parser.get_element_annotation() == expected


def test_insertion():
    expected = 'Kherson National Technical University'
    fill_template_xml(ISSUE_FILE)

    parser = Parser('outputs/output_num0.xsd')
    text = parser.get_doc_text(EElement.TYPE)
    assert text == expected
