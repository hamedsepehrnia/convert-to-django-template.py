#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main entry point for the Django Template Converter application
"""

import tkinter as tk
from django_template_converter.gui import DjangoTemplateConverterGUI


def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = DjangoTemplateConverterGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

