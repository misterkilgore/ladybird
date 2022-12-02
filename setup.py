import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ladybird',
    version='0.0.1',
    author='Michele Cantoni',
    author_email='mcantoni81@gmail.com',
    description='Various tools for social media analysis',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/misterkilgore/ladybird',
    project_urls = {
        "Bug Tracker": "https://github.com/misterkilgore/ladybird/issues"
    },
    license='MIT',
    packages=['ladybird'],
    install_requires=['re'],
)
