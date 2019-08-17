from setuptools import setup, find_packages


setup(
    name='bl3p',
    version='20180412.0',
    description='BL3P.eu Python 3 exchange API',
    keywords='bl3p python3 exchange api',
    url='https://github.com/joosthoeks/bl3p-api',
    author='Joost Hoeks',
    author_email='joosthoeks@gmail.com',
    license='GNU',
    packages=find_packages(),
    install_requires=[
#        'numpy',
#        'pandas',
    ],
    zip_safe=False
)

