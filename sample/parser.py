from sample.template_model import Parser, EEnumeration, ESimpleType, EElement, TEMP_FILE_NAME
from sample.issue_model import Root
import os
import sys
from sample.issue_model import XML_FILE_NAME as ISSUE_FILE

OUTPUT_DIR_NAME = '../outputs'


def fill_template_xml(xml_file):
    # make dir for output files
    try:
        os.mkdir(OUTPUT_DIR_NAME)
    except FileExistsError:
        print('Output directory already exists.')

    parser = Parser()
    root = Root(Parser.get_tree(xml_file))

    for i in range(0, len(root.get_issues())):
        # TODO
        # Set issue info in output file here
        issue = root.get_issues()[i]

        for j in range(0, len(issue.get_sections())):
            # TODO
            # Set section info in output file here
            section = issue.get_sections()[j]

            for k in range(0, len(section.get_articles())):
                # TODO
                # Set article info in output file here

                article = section.get_articles()[k]

                for z in range(0, len(article.get_authors())):
                    # TODO
                    # Set author info in output file here

                    author = article.get_authors()[z]
                    affiliation = author.get_eng_affiliation()
                    parser.set_doc_text(EElement.TYPE, text=affiliation)

            file_name = '../outputs/output_num{}.xsd'.format(j)
            parser.write_xml_to_file(file_name)

    # Delete unnecessary temp file
    try:
        os.remove(TEMP_FILE_NAME)
    except FileNotFoundError:
        print('Temp file was not found.')


if __name__ == "__main__":
    fill_template_xml(ISSUE_FILE)
