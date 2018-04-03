from template_model import Parser, EEnumeration, ESimpleType, EElement
from lxml import etree
from issue_model import Root, Issue
import xml.etree.ElementTree as eT
import os
import sys


def make_output_dir():
    """Create dir for outputs"""

    try:
        os.mkdir('outputs')
    except FileExistsError:
        print('dir already exists')


def parse_xml(xml_file):
    make_output_dir()

    parser = Parser()
    root = Root(parser.get_tree(xml_file))

    for i in range(0, len(root.get_issues())):
        # TODO
        # Set issue info in output file here
        issue = root.get_issues()[i]
        # write_to_file.append('\nIssue {}\n'.format(i + 1))
        # write_to_file.append('Volume: {0}\nNumber: {1}\nData published: {2}\nYear:{3}\nOpen access: {4}\n\n'
        #                      .format(issue.get_volume(), issue.get_number(), issue.get_date_published(),
        #                              issue.get_year(), issue.get_open_access()))

        for j in range(0, len(issue.get_sections())):
            # TODO
            # Set section info in output file here
            section = issue.get_sections()[j]

            # write_to_file.append('\nSection {}\n'.format(j + 1))
            # write_to_file.append('Eng. title: {0}\nRus. title: {1}\nUrk. title: {2}\n'
            #                      .format(section.get_eng_title(), section.get_rus_title(), section.get_ukr_title()) +
            #                      'Eng. abbrev : {0}\nRus. abbrev: {1}\nUkr. abbrev: {2}\n\n'
            #                      .format(section.get_eng_abbrev(), section.get_rus_abbrev(), section.get_ukr_abbrev())
            #                      )
            for k in range(0, len(section.get_articles())):
                # TODO
                # Set article info in output file here

                article = section.get_articles()[k]
                parser.set_doc_text(EElement.TYPE, text=article.get_eng_title())
                # write_to_file.append('\nArticle {}\n'.format(k + 1))
                # write_to_file.append('Eng. title: {0}\nRus. title: {1}\nUrk. title: {2}\n'
                #                      .format(article.get_eng_title(), article.get_rus_title(),
                #                              article.get_ukr_title()) +
                #                      'Pages: {0}\nDate published: {1}\nId: {2}\nAbstract:{3}\nIndexing:{4}\nGalley: {5}\n\n'
                #                      .format(article.get_pages(), article.get_date_published(), article.get_id(),
                #                              article.get_abstracts()[0].text, article.get_indexing(),
                #                              article.get_galley())
                #                      )
                for z in range(0, len(article.get_authors())):
                    # TODO
                    # Set author info in output file here

                    author = article.get_authors()[z]
                    affiliation = author.get_eng_affiliation()
                    parser.set_doc_text(EElement.TYPE, text=affiliation)
                    # write_to_file.append('\nAuthor {}\n'.format(z + 1))
                    # write_to_file.append('Name: {0}{1} {2}\n'
                    #                      .format(author.get_first_name(), author.get_middle_name(),
                    #                              author.get_last_name()) +
                    #                      'Email: {0}\nCountry: {1}\nBiography: {2}\n'
                    #                      .format(author.get_email(), author.get_country(),
                    #                              author.get_biography()[1].text))

            file_name = 'outputs/output_num{}.xsd'.format(j)
            parser.write_xml_to_file(file_name)


if __name__ == "__main__":
    parse_xml("issues.xml")
