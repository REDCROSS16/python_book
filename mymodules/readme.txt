файл заглушка

КАК УСТАНАВЛИВАТЬ СВОИ МОДУЛИ

1.папка mymodules
2.закинуть свой файл ... .py  в папку mymodules
3.создать файл setup.py и readme.txt
4.в файле setup.py
    from setuptools import setup

    setup(
        name = 'vsearch',
        version = '2.0',
        description = 'функции поиска',
        author = 'ALEX RED',
        author_email = 'belkill@mail.ru',
        url = 'https://github.com/REDCROSS16',
        py_modules = ['vsearch'],
    )
5.cmd или terminal с папки mymodules : py -3 setup.py sdist
6.dist/py -3 -m pip install vsearch-2.0.tar
7.import vsearch
