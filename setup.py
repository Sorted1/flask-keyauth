from setuptools import setup, find_packages

setup(
    name='flask_keyauth',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'requests',
    ],
    author='sorted1',
    author_email='',
    description='A quick and simple way to integrate keyauth.win and keyauth.cc into your flask applications.',
    long_description="A quick and simple way to integrate keyauth.win and keyauth.cc into your flask applications.",  # Add the long description here
    long_description_content_type='text/markdown',  # Specify the content type
    url='https://github.com/sorted1/flask-keyauth',
    project_urls={
        'Website': 'https://sorted.live',
        'Source': 'https://github.com/sorted1/flask-keyauth',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)