"""
Core converter logic for converting HTML to Django templates

This module contains the main conversion logic that is independent of GUI.
"""

from pathlib import Path
from typing import Optional
from bs4 import BeautifulSoup


class DjangoTemplateConverter:
    """
    Main class for converting HTML files to Django templates.
    
    This class manages all conversion logic without GUI dependencies.
    """
    
    def __init__(self):
        """Initialize the converter"""
        self._excluded_prefixes = [
            "http://", "https://", "//", "data:", "{%"
        ]
    
    def convert_file(
        self, 
        input_path: str, 
        output_path: Optional[str] = None
    ) -> str:
        """
        Convert HTML file to Django template.
        
        Args:
            input_path: Path to input HTML file
            output_path: Path to output file (optional)
            
        Returns:
            Output file path
            
        Raises:
            FileNotFoundError: If input file doesn't exist
            IOError: If error occurs while reading/writing file
        """
        input_file = Path(input_path)
        if not input_file.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
        
        # Read HTML file
        with open(input_path, "r", encoding="utf-8") as file:
            html_content = file.read()
        
        # Convert content
        converted_html = self.convert_string(html_content)
        
        # Determine output path
        if not output_path:
            output_path = str(
                input_file.parent / f"{input_file.stem}_django{input_file.suffix}"
            )
        
        # Save file
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(converted_html)
        
        return output_path
    
    def convert_string(self, html_content: str) -> str:
        """
        Convert HTML content string to Django template.
        
        Args:
            html_content: HTML content as string
            
        Returns:
            Converted Django template content
        """
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Add {% load static %} tag
        self._add_load_static_tag(soup)
        
        # Convert different types of links
        self._convert_links(soup)
        self._convert_scripts(soup)
        self._convert_images(soup)
        self._convert_sources(soup)
        self._convert_srcsets(soup)
        
        return str(soup)
    
    def _add_load_static_tag(self, soup: BeautifulSoup) -> None:
        """Add {% load static %} tag at the beginning of the file"""
        if soup.html:
            html_string = str(soup)
            if '{% load static %}' not in html_string:
                load_static_tag = soup.new_string('{% load static %}\n')
                soup.html.insert(0, load_static_tag)
    
    def _convert_links(self, soup: BeautifulSoup) -> None:
        """Convert <link> tags"""
        for link in soup.find_all("link", href=True):
            href = link['href']
            if self._should_convert(href):
                link['href'] = f'{{% static "{href}" %}}'
    
    def _convert_scripts(self, soup: BeautifulSoup) -> None:
        """Convert <script> tags"""
        for script in soup.find_all("script", src=True):
            src = script['src']
            if self._should_convert(src):
                script['src'] = f'{{% static "{src}" %}}'
    
    def _convert_images(self, soup: BeautifulSoup) -> None:
        """Convert <img> tags"""
        for img in soup.find_all("img", src=True):
            src = img['src']
            if self._should_convert(src, include_data_uri=False):
                img['src'] = f'{{% static "{src}" %}}'
    
    def _convert_sources(self, soup: BeautifulSoup) -> None:
        """Convert <source> tags"""
        for source in soup.find_all("source", src=True):
            src = source['src']
            if self._should_convert(src, include_data_uri=False):
                source['src'] = f'{{% static "{src}" %}}'
    
    def _convert_srcsets(self, soup: BeautifulSoup) -> None:
        """Convert srcset in <img> and <source> tags"""
        # Convert srcset in <source>
        for source in soup.find_all("source", srcset=True):
            srcset = source['srcset']
            if srcset and not srcset.startswith("{%"):
                new_srcset = self._convert_srcset_string(srcset)
                source['srcset'] = new_srcset
        
        # Convert srcset in <img>
        for img in soup.find_all("img", srcset=True):
            srcset = img['srcset']
            if srcset and not srcset.startswith("{%"):
                new_srcset = self._convert_srcset_string(srcset)
                img['srcset'] = new_srcset
    
    def _convert_srcset_string(self, srcset: str) -> str:
        """
        Convert srcset string to Django template format.
        
        Args:
            srcset: Original srcset string
            
        Returns:
            Converted srcset string
        """
        parts = srcset.split(',')
        new_parts = []
        
        for part in parts:
            part = part.strip()
            url = part.split()[0] if ' ' in part else part
            
            if self._should_convert(url, include_data_uri=False):
                if ' ' in part:
                    size = part.split()[1]
                    new_parts.append(f'{{% static "{url}" %}} {size}')
                else:
                    new_parts.append(f'{{% static "{url}" %}}')
            else:
                new_parts.append(part)
        
        return ', '.join(new_parts)
    
    def _should_convert(
        self, 
        url: str, 
        include_data_uri: bool = True
    ) -> bool:
        """
        Check if URL should be converted.
        
        Args:
            url: URL to check
            include_data_uri: Whether to include data URI
            
        Returns:
            True if should be converted, False otherwise
        """
        if not url:
            return False
        
        excluded = self._excluded_prefixes.copy()
        if not include_data_uri:
            # data: is already in the list, so no need to handle it
            pass
        
        return not any(url.startswith(prefix) for prefix in excluded)

