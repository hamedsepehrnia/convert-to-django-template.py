"""
GUI Window for Django Template Converter

This module contains the graphical user interface for the converter.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
from pathlib import Path

from ..core.converter import DjangoTemplateConverter
from ..utils.helpers import validate_html_file, generate_output_path


class DjangoTemplateConverterGUI:
    """Main GUI class for the converter"""
    
    def __init__(self, root: tk.Tk):
        """
        Initialize the GUI.
        
        Args:
            root: Main tkinter window
        """
        self.root = root
        self.converter = DjangoTemplateConverter()
        
        self._setup_window()
        self._setup_ui()
    
    def _setup_window(self):
        """Setup main window"""
        self.root.title("HTML to Django Template Converter")
        self.root.geometry("1200x800")
        self.root.resizable(True, True)
    
    def _setup_ui(self):
        """Setup user interface"""
        # General style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Application header
        self._create_header()
        
        # Main container for two columns
        main_container = tk.Frame(self.root, bg="#ecf0f1", padx=10, pady=10)
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Left column (Input)
        self._create_input_column(main_container)
        
        # Middle column (Convert button)
        self._create_convert_button_column(main_container)
        
        # Right column (Output)
        self._create_output_column(main_container)
    
    def _create_header(self):
        """Create application header"""
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=70)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="HTML to Django Template Converter",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#2c3e50"
        )
        title_label.pack(pady=15)
    
    def _create_input_column(self, parent: tk.Frame):
        """Create input column on the left"""
        input_column = tk.Frame(parent, bg="#ecf0f1", padx=10)
        input_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Input label
        tk.Label(
            input_column,
            text="Input",
            font=("Arial", 14, "bold"),
            bg="#ecf0f1"
        ).pack(anchor=tk.W, pady=(0, 10))
        
        # Input type selection
        input_type_frame = tk.Frame(input_column, bg="#ecf0f1")
        input_type_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.input_type_var = tk.StringVar(value="code")
        tk.Radiobutton(
            input_type_frame,
            text="Code",
            variable=self.input_type_var,
            value="code",
            command=self._on_input_type_change,
            bg="#ecf0f1",
            font=("Arial", 10)
        ).pack(side=tk.LEFT, padx=(0, 20))
        
        tk.Radiobutton(
            input_type_frame,
            text="File",
            variable=self.input_type_var,
            value="file",
            command=self._on_input_type_change,
            bg="#ecf0f1",
            font=("Arial", 10)
        ).pack(side=tk.LEFT)
        
        # Input content frame
        self.input_content_frame = tk.Frame(input_column, bg="#ecf0f1")
        self.input_content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Code input (default)
        self.input_code_text = scrolledtext.ScrolledText(
            self.input_content_frame,
            wrap=tk.WORD,
            font=("Consolas", 10),
            bg="#ffffff",
            fg="#2c3e50",
            insertbackground="#2c3e50",
            padx=10,
            pady=10
        )
        self.input_code_text.pack(fill=tk.BOTH, expand=True)
        
        # File input (hidden initially)
        self.input_file_frame = tk.Frame(self.input_content_frame)
        
        self.input_path_var = tk.StringVar()
        self.input_entry = tk.Entry(
            self.input_file_frame,
            textvariable=self.input_path_var,
            font=("Arial", 10),
            state="readonly"
        )
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        browse_input_btn = tk.Button(
            self.input_file_frame,
            text="Browse...",
            command=self._browse_input_file,
            bg="#3498db",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=5,
            cursor="hand2"
        )
        browse_input_btn.pack(side=tk.RIGHT)
    
    def _create_output_column(self, parent: tk.Frame):
        """Create output column on the right"""
        output_column = tk.Frame(parent, bg="#ecf0f1", padx=10)
        output_column.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Output label
        tk.Label(
            output_column,
            text="Output",
            font=("Arial", 14, "bold"),
            bg="#ecf0f1"
        ).pack(anchor=tk.W, pady=(0, 10))
        
        # Output type selection
        output_type_frame = tk.Frame(output_column, bg="#ecf0f1")
        output_type_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.output_type_var = tk.StringVar(value="code")
        tk.Radiobutton(
            output_type_frame,
            text="Code",
            variable=self.output_type_var,
            value="code",
            command=self._on_output_type_change,
            bg="#ecf0f1",
            font=("Arial", 10)
        ).pack(side=tk.LEFT, padx=(0, 20))
        
        tk.Radiobutton(
            output_type_frame,
            text="File",
            variable=self.output_type_var,
            value="file",
            command=self._on_output_type_change,
            bg="#ecf0f1",
            font=("Arial", 10)
        ).pack(side=tk.LEFT)
        
        # Output content frame
        self.output_content_frame = tk.Frame(output_column, bg="#ecf0f1")
        self.output_content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Code output (default)
        self.output_code_text = scrolledtext.ScrolledText(
            self.output_content_frame,
            wrap=tk.WORD,
            font=("Consolas", 10),
            bg="#f8f9fa",
            fg="#2c3e50",
            insertbackground="#2c3e50",
            padx=10,
            pady=10,
            state=tk.DISABLED
        )
        self.output_code_text.pack(fill=tk.BOTH, expand=True)
        
        # File output (hidden initially)
        self.output_file_frame = tk.Frame(self.output_content_frame)
        
        self.output_path_var = tk.StringVar()
        self.output_entry = tk.Entry(
            self.output_file_frame,
            textvariable=self.output_path_var,
            font=("Arial", 10)
        )
        self.output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        browse_output_btn = tk.Button(
            self.output_file_frame,
            text="Browse...",
            command=self._browse_output_file,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=5,
            cursor="hand2"
        )
        browse_output_btn.pack(side=tk.RIGHT)
    
    def _create_convert_button_column(self, parent: tk.Frame):
        """Create convert button in the middle"""
        button_column = tk.Frame(parent, bg="#ecf0f1", padx=10)
        button_column.pack(side=tk.LEFT, fill=tk.Y)
        
        convert_btn = tk.Button(
            button_column,
            text="Convert\n→",
            command=self._convert_to_django_template,
            bg="#27ae60",
            fg="white",
            font=("Arial", 14, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=30,
            cursor="hand2",
            width=10
        )
        convert_btn.pack(pady=20)
        
        clear_btn = tk.Button(
            button_column,
            text="Clear",
            command=self._clear_all,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 12, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=10,
            cursor="hand2",
            width=10
        )
        clear_btn.pack()
    
    def _on_input_type_change(self):
        """Handle input type change"""
        input_type = self.input_type_var.get()
        
        if input_type == "code":
            self.input_file_frame.pack_forget()
            self.input_code_text.pack(fill=tk.BOTH, expand=True)
        else:
            self.input_code_text.pack_forget()
            self.input_file_frame.pack(fill=tk.X)
    
    def _on_output_type_change(self):
        """Handle output type change"""
        output_type = self.output_type_var.get()
        
        if output_type == "code":
            self.output_file_frame.pack_forget()
            self.output_code_text.pack(fill=tk.BOTH, expand=True)
            # Enable output text for viewing
            self.output_code_text.config(state=tk.NORMAL)
        else:
            self.output_code_text.pack_forget()
            self.output_file_frame.pack(fill=tk.X)
    
    def _browse_input_file(self):
        """Browse and select input HTML file"""
        file_path = filedialog.askopenfilename(
            title="Select HTML File",
            filetypes=[
                ("HTML Files", "*.html *.htm"),
                ("All Files", "*.*")
            ]
        )
        if file_path:
            self.input_path_var.set(file_path)
            # Load file content into code text if visible
            if self.input_type_var.get() == "code":
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.read()
                    self.input_code_text.delete(1.0, tk.END)
                    self.input_code_text.insert(1.0, content)
                except Exception as e:
                    messagebox.showerror("Error", f"Error reading file: {str(e)}")
    
    def _browse_output_file(self):
        """Browse and select output file path"""
        file_path = filedialog.asksaveasfilename(
            title="Save Output File",
            defaultextension=".html",
            filetypes=[
                ("HTML Files", "*.html"),
                ("All Files", "*.*")
            ]
        )
        if file_path:
            self.output_path_var.set(file_path)
    
    def _convert_to_django_template(self):
        """Convert HTML to Django Template"""
        input_type = self.input_type_var.get()
        output_type = self.output_type_var.get()
        
        # Get input content
        if input_type == "code":
            html_content = self.input_code_text.get(1.0, tk.END).strip()
            if not html_content:
                messagebox.showerror("Error", "Please enter HTML code in the input field.")
                return
        else:
            input_path = self.input_path_var.get()
            if not input_path or not validate_html_file(input_path):
                messagebox.showerror("Error", "Please select a valid HTML file.")
                return
            try:
                with open(input_path, "r", encoding="utf-8") as file:
                    html_content = file.read()
            except Exception as e:
                messagebox.showerror("Error", f"Error reading file: {str(e)}")
                return
        
        # Convert content
        try:
            converted_html = self.converter.convert_string(html_content)
            
            # Handle output
            if output_type == "code":
                self.output_code_text.config(state=tk.NORMAL)
                self.output_code_text.delete(1.0, tk.END)
                self.output_code_text.insert(1.0, converted_html)
                self.output_code_text.config(state=tk.DISABLED)
                messagebox.showinfo("Success", "Conversion completed successfully!")
            else:
                output_path = self.output_path_var.get().strip()
                if not output_path:
                    # Generate default output path
                    if input_type == "file":
                        output_path = generate_output_path(input_path, None)
                    else:
                        messagebox.showerror("Error", "Please specify output file path.")
                        return
                
                with open(output_path, "w", encoding="utf-8") as file:
                    file.write(converted_html)
                
                messagebox.showinfo(
                    "Success",
                    f"Conversion completed successfully!\n\nOutput file:\n{output_path}"
                )
                
                # Also show in code output if visible
                if self.output_code_text.winfo_viewable():
                    self.output_code_text.config(state=tk.NORMAL)
                    self.output_code_text.delete(1.0, tk.END)
                    self.output_code_text.insert(1.0, converted_html)
                    self.output_code_text.config(state=tk.DISABLED)
        
        except Exception as e:
            messagebox.showerror("Error", f"Error converting: {str(e)}")
    
    def _clear_all(self):
        """Clear all fields"""
        # Clear input
        self.input_code_text.delete(1.0, tk.END)
        self.input_path_var.set("")
        
        # Clear output
        self.output_code_text.config(state=tk.NORMAL)
        self.output_code_text.delete(1.0, tk.END)
        self.output_code_text.config(state=tk.DISABLED)
        self.output_path_var.set("")
