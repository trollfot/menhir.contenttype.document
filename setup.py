from setuptools import setup, find_packages
from os.path import join

name = 'menhir.contenttype.document'
version = '0.1'
history = open(join("docs", "HISTORY.txt")).read()
readme = open(
    join("src", "menhir", "contenttype", "document", "README.txt")).read()

tests_require = [
    'zope.app.publisher',
    'zope.component',
    'zope.publisher',
    ]

setup(name = name,
      version = version,
      description = 'Dolmen contenttype extension : document',
      long_description = readme + '\n' + history,
      keywords = 'Grok Zope3 CMS Dolmen',
      author = 'Souheil Chelfouh',
      author_email = 'trollfot@gmail.com',
      url = 'http://gitweb.dolmen-project.org/',
      download_url = 'http://pypi.python.org/pypi/menhir.contenttype.document',
      license = 'GPL',
      packages = find_packages('src', exclude=['ez_setup']),
      package_dir = {'': 'src'},
      namespace_packages = ['menhir', 'menhir.contenttype'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      tests_require = tests_require,
      extras_require = {'test': tests_require},
      install_requires=[
          'dolmen.app.layout',
          'dolmen.content >= 0.5.1',
          'dolmen.forms.crud >= 1.0b1',
          'dolmen.widget.tinymce',
          'grok',
          'html2text',
          'setuptools',
          'zope.i18nmessageid',
          'zope.index',
          'zope.interface',
          'zope.schema',
          'dolmen.app.security',
      ],
      classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
      ],
)
