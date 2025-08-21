"""Setup for pdf XBlock."""

import os
from setuptools import setup, find_packages


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


def load_requirements():
    """Load requirements from requirements.txt"""
    with open('requirements.txt', 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]


setup(
    name='xblock-pdf',
    version='2.0.0',
    description='Course component (Open edX XBlock) that provides an easy way to embed a PDF',
    long_description='A modernized XBlock for embedding PDF files in Open edX courses, compatible with Teak release and newer versions.',
    author='Updated for OpenEDX Teak compatibility',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'XBlock>=2.0.0',
        'web-fragments>=2.0.0',
        'xblock-utils>=3.0.0',
        'Django>=4.2,<5.0',
    ],
    entry_points={
        'xblock.v1': [
            'pdf = pdf.pdf:PdfBlock',
        ]
    },
    package_data=package_data('pdf', 'static'),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
