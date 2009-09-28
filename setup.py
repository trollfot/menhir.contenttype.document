from setuptools import setup, find_packages
from os.path import join

name = 'menhir.contenttype.document'
version = '0.1'
history = open(os.path.join("docs", "HISTORY.txt")).read()
readme = open(os.path.join("src", "menhir", "contenttype", "document", "README.txt")).read()

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
      install_requires=[
          'setuptools',
          'grok',
          'html2text',
          'dolmen.content',
          'dolmen.widget.tinymce',
      ],
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Grok',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
      ],
)
