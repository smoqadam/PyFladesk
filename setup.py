from setuptools import setup

setup(name='PyFladesk',
      version='1.1',
      setup_requires=['setuptools-markdown'],
      long_description_markdown_filename='README.md',
      description='Create desktop application by using Flask and QtWebEngine',
      url="https://github.com/smoqadam/PyFladesk",
      author='​Saeed Moqadam, Ezequiel Castaño​',
      author_email='saeed.moqadam@gmail.com, castanoezequielleonardo@gmail.com',
      license='MIT',
      install_requires=[
          'flask',
          'pyqt5',
          'pyqtwebengine',
      ],
      packages=['pyfladesk'],
      zip_safe=False,
      keywords = ['​GUI​', '​Flask​', 'Qt'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3',
      ],
      python_requires='>=3',
      )