from setuptools import setup


setup(
    name='bl3p',
    version='20180112.0',
    description='BL3P.eu Python 3 exchange API',
    keywords='bl3p python3 exchange api',
    url='https://github.com/joosthoeks/bl3p-api',
    author='Joost Hoeks',
    author_email='joosthoeks@gmail.com',
    license='GNU',
    packages=[
        'bl3p',
        'bl3p.api',
    ],
    install_requires=[
#        'numpy',
#        'pandas',
    ],
    zip_safe=False
)

