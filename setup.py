from setuptools import setup

setup(
    name='gamelog',
    version='0.1',
    py_modules=[
        'application.main',
        'application.game',
        'application.gamelist'],
    packages=["application"],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gamelog=application.main:log
    ''',
)
