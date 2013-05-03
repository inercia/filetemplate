from setuptools import setup, find_packages

version = '0.1'

setup(name='test_app',
      version=version,
      description="frozen test app",
      long_description="""A test app""",
      classifiers=[],
      keywords='test app',
      author='tester',
      author_email='tester@gmail.com',
      url='www.testing.com',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
)
