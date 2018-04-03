class Root:
    def __init__(self, root_obj):
        self._root = root_obj
        self._issues = self._root.findall('issue')

    def get_issues(self):
        return [Issue(obj) for obj in self._issues]


class Issue:
    def __init__(self, issue_obj):
        self._issue = issue_obj
        self._volume = self._issue.find('volume').text
        self._number = self._issue.find('number').text
        self._year = self._issue.find('year').text
        self._date_published = self._issue.find('date_published').text
        self._open_access = self._issue.find('open_access').text
        self._sections = self._issue.findall('section')

    def get_sections(self):
        return [Section(obj) for obj in self._sections]

    def get_volume(self):
        return self._volume

    def get_number(self):
        return self._number

    def get_year(self):
        return self._year

    def get_date_published(self):
        return self._date_published

    def get_open_access(self):
        return self._open_access


class Section:
    def __init__(self, section_obj):
        self._section = section_obj
        self._titles = self._section.findall('title')
        self._abbrevs = self._section.findall('abbrev')
        self._articles = self._section.findall('article')

    def get_eng_title(self):
        return self._titles[0].text

    def get_rus_title(self):
        return self._titles[1].text

    def get_ukr_title(self):
        return self._titles[2].text

    def get_eng_abbrev(self):
        return self._abbrevs[0].text

    def get_rus_abbrev(self):
        return self._abbrevs[1].text

    def get_ukr_abbrev(self):
        return self._abbrevs[2].text

    def get_articles(self):
        return [Article(obj) for obj in self._articles]


class Article:
    def __init__(self, article_obj):
        self._article = article_obj
        self._id = self._article.find('id').text
        self._titles = self._article.findall('title')
        self._abstracts = self._article.findall('abstract')
        self._indexing = self._article.find('indexing').text
        self._authors = self._article.findall('author')
        self._pages = self._article.find('pages').text
        self._date_published = self._article.find('date_published').text
        self._galley = self._article.find('galley').text

    def get_id(self):
        return self._id

    def get_titles(self):
        return self._titles

    def get_abstracts(self):
        return self._abstracts

    def get_indexing(self):
        return self._indexing

    def get_authors(self):
        return [Author(obj) for obj in self._authors]

    def get_pages(self):
        return self._pages

    def get_date_published(self):
        return self._date_published

    def get_galley(self):
        return self._galley

    def get_rus_title(self):
        return self._titles[2].text

    def get_eng_title(self):
        return self._titles[0].text

    def get_ukr_title(self):
        return self._titles[1].text


class Author:
    def __init__(self, author_obj):
        self._author = author_obj
        self._first_name = self._author.find('firstname').text
        self._middle_name = self._author.find('middlename').text
        self._last_name = self._author.find('lastname').text
        self._country = self._author.find('country').text
        self._email = self._author.find('email').text

        self._affiliations = self._author.findall('affiliation')
        self._biography = self._author.findall('biography')

    def get_first_name(self):
        return self._first_name

    def get_middle_name(self):
        return self._middle_name

    def get_last_name(self):
        return self._last_name

    def get_country(self):
        return self._country

    def get_email(self):
        return self._email

    def get_affiliations(self):
        return self._affiliations

    def get_biography(self):
        return self._biography

    def get_eng_affiliation(self):
        return self._affiliations[0].text

    def get_rus_affiliation(self):
        return self._affiliations[1].text

    def get_ukr_affiliation(self):
        return self._affiliations[2].text