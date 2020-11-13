from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='TOPSIS_SUKRITI_401803026',
    version='0.0.1',
    description='TOPSIS evaluator for given data',
    author='Sukriti Sharma',
    author_email='ssharma_bemba18@thapar.edu',
    license='MIT',
    classifiers=classifiers,
    keywords='calculator',
    packages=find_packages(),
    install_requires=['pandas']
)