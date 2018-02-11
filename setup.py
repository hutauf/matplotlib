#!/usr/bin/env python

# ...

from distutils.core import setup

setup(name='matplotlib-aipy',
      version='2.1.0',
      description='Python plotting package, this is the prebuilt version for QPython (AiPy branch)',
      author='John D. Hunter, Michael Droettboom',
      author_email='info@numfocus.org',
      url='http://matplotlib.org',
      packages=["matplotlib","mpl_toolkits"],
      package_data={
            "mpl_toolkits":[
"*.py",
"axes_grid/*.py",
"axes_grid1/*.py",
"axisartist/*.py",
"mplot3d/*.py",
],

            "matplotlib": [
"*.so",
"axes/*",
"backends/*.py",
"backends/*.so",
"backends/qt_editor/*.py",
"backends/web_backend/*.html",
"backends/web_backend/*.js",
"backends/web_backend/css/*",
"backends/web_backend/js/*",
"backends/web_backend/jquery/css/themes/base/*.css",
"backends/web_backend/jquery/css/themes/base/images/*",
"backends/web_backend/jquery/js/*",
"cbook/*.py",
"compat/*.py",
"mpl-data/fonts/afm/*",
"mpl-data/fonts/pdfcorefonts/*",
"mpl-data/fonts/ttf/*",
"mpl-data/images/*",
"mpl-data/sample_data/*.png",
"mpl-data/sample_data/*.jpg",
"mpl-data/sample_data/*.gz",
"mpl-data/sample_data/*.xrc",
"mpl-data/sample_data/*.npz",
"mpl-data/sample_data/*.dat",
"mpl-data/sample_data/*.csv",
"mpl-data/sample_data/axes_grid/*",
"mpl-data/stylelib/*",
"projections/*.py",
"sphinxext/*.py",
"style/*.py",
"testing/*.py",
"testing/_nose/*.py",
"testing/_nose/plugins/*.py",
"testing/jpl_units/*.py",
"tri/*.py",

            ]
      },
      long_description="""

Matplotlib strives to produce publication quality 2D graphics
for interactive graphing, scientific publishing, user interface development and web application servers targeting multiple user interfaces and hardcopy output formats. There is a 'pylab' mode which emulates matlab graphics.

""",
      license="BSD",
      install_requires=["pyparsing","backports.functools_lru_cache-qpython","cycler","python-dateutil-qpython","scipy-aipy"],
     )
