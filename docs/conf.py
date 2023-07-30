import sys
import os

sys.path.insert(0, os.path.abspath(os.sep.join((os.curdir, ".."))))

project = 'Moonshot'
author = u'Team Einstein'
extensions = ['sphinx.ext.todo', 
              'sphinx.ext.viewcode', 
              'sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinx.ext.mathjax']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']
autoclass_content = "both"
