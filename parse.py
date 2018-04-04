from src.copernicus_parser import fill_template_xml
from src.issue_model import XML_FILE_NAME as ISSUE_FILE_NAME


if __name__ == '__main__':
    fill_template_xml(ISSUE_FILE_NAME)