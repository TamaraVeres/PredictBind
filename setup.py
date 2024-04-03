import setuptools

with open("README.md", "r") as fh: 
    long_description = fh.read() 

setuptools.setup(
    name='PredictBind',
    version='1.0.1',
    packages=setuptools.find_packages(),
    package_data={'PredictBind': ['p2rank.jar']},
    install_requires=['requests'],
    author='Tamara Veres',
    author_email='tamaraveres19@gmail.com',
    description='PredictBind is a wrapped inspired and built around P2Rank as ligand binding site predictor for proteins',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/TamaraVeres/binder',
    classifiers=[ 
        "Programming Language :: Python :: 3", 
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent", 
    ], 
)