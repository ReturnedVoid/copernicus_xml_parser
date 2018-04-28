import sys
from src.copernicus_parser import fill_template_xml
from src.template_model import XML_FILE_NAME as TEMPLATE_FILE_NAME
from src.issue_model import XML_FILE_NAME as ISSUE_FILE_NAME
from colorama import init
from colorama import Fore, Back, Style

# for colorama
init()


def verify_files_existence():
    file_not_exists_error = False
    try:
        open(TEMPLATE_FILE_NAME)
    except IOError:
        print(Fore.RED + 'Critical error: file {} does not exist'.format(TEMPLATE_FILE_NAME))
        file_not_exists_error = True

    try:
        open(ISSUE_FILE_NAME)
    except IOError:
        print(Fore.RED + 'Critical error: file {} does not exist'.format(ISSUE_FILE_NAME))
        file_not_exists_error = True

    if file_not_exists_error:
        input()
        sys.exit(0)


if __name__ == '__main__':
    verify_files_existence()
    fill_template_xml(ISSUE_FILE_NAME)
    input('Completed.')
