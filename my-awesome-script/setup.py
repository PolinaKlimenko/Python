from setuptools import setup
 
setup(
name='my-awesome-script',
version='0.1.0',
packages=['my_awesome_script'],
entry_points = {
      'console_scripts': ['my-awesome-script=my_awesome_script.hw_script:main'],
  }
) 