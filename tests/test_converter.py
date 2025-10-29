"""
Unit tests for Django Template Converter
تست‌های واحد برای تبدیل کننده
"""

import unittest
from django_template_converter.core.converter import DjangoTemplateConverter


class TestDjangoTemplateConverter(unittest.TestCase):
    """تست‌های کلاس DjangoTemplateConverter"""
    
    def setUp(self):
        """تنظیمات اولیه برای هر تست"""
        self.converter = DjangoTemplateConverter()
    
    def test_convert_links(self):
        """تست تبدیل تگ‌های <link>"""
        html = '<link rel="stylesheet" href="css/style.css">'
        result = self.converter.convert_string(html)
        
        self.assertIn('{% load static %}', result)
        self.assertIn('{% static "css/style.css" %}', result)
    
    def test_convert_scripts(self):
        """تست تبدیل تگ‌های <script>"""
        html = '<script src="js/main.js"></script>'
        result = self.converter.convert_string(html)
        
        self.assertIn('{% static "js/main.js" %}', result)
    
    def test_convert_images(self):
        """تست تبدیل تگ‌های <img>"""
        html = '<img src="images/logo.png" alt="Logo">'
        result = self.converter.convert_string(html)
        
        self.assertIn('{% static "images/logo.png" %}', result)
    
    def test_exclude_external_urls(self):
        """تست عدم تبدیل لینک‌های خارجی"""
        html = '<link href="https://cdn.example.com/style.css">'
        result = self.converter.convert_string(html)
        
        self.assertIn('https://cdn.example.com/style.css', result)
        self.assertNotIn('{% static "https://', result)
    
    def test_exclude_data_uri(self):
        """تست عدم تبدیل data URI"""
        html = '<img src="data:image/png;base64,iVBORw0KGgo...">'
        result = self.converter.convert_string(html)
        
        self.assertIn('data:image/png;base64', result)
        self.assertNotIn('{% static "data:', result)
    
    def test_already_converted(self):
        """تست عدم تغییر لینک‌های از قبل تبدیل شده"""
        html = '<link href="{% static \'css/style.css\' %}">'
        result = self.converter.convert_string(html)
        
        # نباید دو بار {% static %} اضافه شود
        count = result.count('{% static')
        self.assertEqual(count, 1)


if __name__ == "__main__":
    unittest.main()

