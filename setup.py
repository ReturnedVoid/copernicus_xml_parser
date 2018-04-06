from cx_Freeze import setup, Executable

setup(
    name="copernicus_parser",
    version="1.0",
    description="parser for DNURT",
    executables=[Executable("parse.py")], requires=['cx_Freeze', 'colorama']
)
