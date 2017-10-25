from setuptools import setup


setup(
    name='bl3p',
    version='20171025.0',
    description='BL3P.eu exchange API',
    keywords='bl3p exchange api',
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

