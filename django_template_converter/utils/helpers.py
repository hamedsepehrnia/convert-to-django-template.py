"""
Helper utility functions

This module contains utility functions for file validation and path generation.
"""

from pathlib import Path
from typing import Optional


def validate_html_file(file_path: str) -> bool:
    """
    Validate HTML file.
    
    Args:
        file_path: Path to file
        
    Returns:
        True if file is valid
    """
    path = Path(file_path)
    return path.exists() and path.is_file() and path.suffix.lower() in ['.html', '.htm']


def generate_output_path(
    input_path: str, 
    output_path: Optional[str] = None
) -> str:
    """
    Generate automatic output path if not specified.
    
    Args:
        input_path: Path to input file
        output_path: Path to output file (optional)
        
    Returns:
        Output file path
    """
    if output_path and output_path.strip():
        return output_path.strip()
    
    input_file = Path(input_path)
    return str(input_file.parent / f"{input_file.stem}_django{input_file.suffix}")

