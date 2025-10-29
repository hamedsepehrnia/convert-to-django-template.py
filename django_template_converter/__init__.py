"""
Django Template Converter

A tool for converting HTML files to standard Django templates.
"""

__version__ = "2.0.0"
__author__ = "Developer"

from .core.converter import DjangoTemplateConverter as Converter

__all__ = ['Converter']

