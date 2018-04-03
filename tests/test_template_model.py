from sample import template_model


def test_get_doc_with_valid_args():
    parser = template_model.Parser()
    assert parser.get_doc_text(template_model.ESimpleType.roleType, template_model.EEnumeration.AUTHOR) \
           == 'Author (including co-author) / Autor (w tym Współautor)'


test_get_doc_with_valid_args()