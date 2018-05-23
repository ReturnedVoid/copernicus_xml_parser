from setuptools import setup, find_packages

setup(name='copernicus_xml_parser',
      version='1.0.0',
      description='DNURT app for parsing issues.',
      long_description='',
      install_requires=['colorama'],
      url='https://github.com/ReturnedVoid/copernicus_xml_parser',
      author='Andrey Nechaev',
      author_email='andrewnech@gmail.com',
      license='DNURT',
      packages=find_packages(),
      keywords='DNURT author scopus web_of_science',

      entry_points={
          'console_scripts':
              ['parse_issues = src.parse:main']
      },
      package_data={
          '': ['*.json', 'geckodriver']
      }
      )
