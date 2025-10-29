# تبدیل‌کننده HTML به Django Template | HTML to Django Template Converter

---

<div dir="rtl">

## معرفی | Introduction

یک ابزار گرافیکی برای تبدیل خودکار فایل‌های HTML به تمپلیت استاندارد Django با رابط کاربری زیبا و کاربرپسند.

A graphical tool for automatically converting HTML files to standard Django templates with a beautiful and user-friendly interface.

</div>

---

## ویژگی‌ها | Features

<div dir="rtl">

- **رابط کاربری گرافیکی** - استفاده آسان با رابط کاربری tkinter
- **ورودی و خروجی انعطاف‌پذیر** - انتخاب بین کد مستقیم یا فایل برای ورودی و خروجی
- **دو ستون کنار هم** - فیلد بزرگ برای کد ورودی (سمت چپ) و کد خروجی (سمت راست)
- **تبدیل خودکار** - تبدیل تمام لینک‌های استاتیک به `{% static %}`
- **پشتیبانی از انواع فایل** - تبدیل CSS، JavaScript، تصاویر و سایر فایل‌های استاتیک
- **سریع و کارآمد** - تبدیل فایل‌های بزرگ در کسری از ثانیه
- **نمایش همزمان** - می‌توانید کد را ببینید و فایل را نیز ذخیره کنید

</div>

**English:**
- **Graphical User Interface** - Easy to use with tkinter GUI
- **Flexible Input and Output** - Choose between direct code or file for input and output
- **Two Columns Side by Side** - Large field for input code (left) and output code (right)
- **Automatic Conversion** - Converts all static links to `{% static %}`
- **Multi-file Support** - Converts CSS, JavaScript, images and other static files
- **Fast and Efficient** - Convert large files in seconds
- **Simultaneous Display** - You can view the code and save the file at the same time

---

## نیازمندی‌ها | Requirements

<div dir="rtl">

- Python 3.6 یا بالاتر
- BeautifulSoup4
- tkinter (معمولاً به صورت پیش‌فرض در Python نصب است)

</div>

**English:**
- Python 3.6 or higher
- BeautifulSoup4
- tkinter (usually pre-installed with Python)

---

## نصب | Installation

### 1. کلون یا دانلود پروژه | Clone or Download the Project

<div dir="rtl">

```bash
git clone <repository-url>
cd convert_to_django_template.py
```

</div>

**English:**
```bash
git clone <repository-url>
cd convert_to_django_template.py
```

### 2. نصب وابستگی‌ها | Install Dependencies

<div dir="rtl">

```bash
pip install -r requirements.txt
```

یا به صورت دستی:

```bash
pip install beautifulsoup4 lxml
```

</div>

**English:**
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install beautifulsoup4 lxml
```

### 3. نصب پکیج (اختیاری) | Install Package (Optional)

<div dir="rtl">

برای استفاده از پکیج به عنوان ماژول Python:

```bash
pip install -e .
```

این دستور پکیج را در حالت "editable" نصب می‌کند، به این معنی که می‌توانید تغییرات را بدون نصب مجدد اعمال کنید.

</div>

**English:**

To use the package as a Python module:

```bash
pip install -e .
```

This command installs the package in "editable" mode, meaning you can apply changes without reinstalling.

---

## نحوه استفاده | Usage

### روش اول: اجرای مستقیم با main.py | Method 1: Direct Execution with main.py

<div dir="rtl">

```bash
python main.py
```

یا:

```bash
python3 main.py
```

</div>

**English:**
```bash
python main.py
```

Or:
```bash
python3 main.py
```

### روش دوم: نصب به عنوان پکیج | Method 2: Install as Package

<div dir="rtl">

```bash
# نصب در حالت توسعه (editable mode)
pip install -e .

# سپس اجرا
django-template-converter
```

</div>

**English:**
```bash
# Install in editable mode
pip install -e .

# Then run
django-template-converter
```

### روش سوم: استفاده به عنوان ماژول | Method 3: Use as Module

<div dir="rtl">

```python
from django_template_converter import Converter

converter = Converter()
output_path = converter.convert_file("input.html", "output.html")
```

</div>

**English:**
```python
from django_template_converter import Converter

converter = Converter()
output_path = converter.convert_file("input.html", "output.html")
```

---

## راهنمای استفاده | User Guide

### گام 1: اجرای برنامه | Step 1: Run the Application

<div dir="rtl">

پس از نصب وابستگی‌ها، فایل `main.py` را اجرا کنید:

```bash
python main.py
```

</div>

**English:**

After installing dependencies, run `main.py`:

```bash
python main.py
```

### گام 2: انتخاب نوع ورودی | Step 2: Select Input Type

<div dir="rtl">

رابط کاربری دارای دو ستون است:
- **ستون چپ (Input)**: برای ورودی
- **ستون راست (Output)**: برای خروجی

برای ورودی، می‌توانید یکی از دو گزینه را انتخاب کنید:
- **Code**: مستقیماً کد HTML را در فیلد بزرگ متنی وارد کنید
- **File**: فایل HTML را از سیستم انتخاب کنید

</div>

**English:**

The user interface has two columns:
- **Left column (Input)**: For input
- **Right column (Output)**: For output

For input, you can choose one of two options:
- **Code**: Enter HTML code directly in the large text field
- **File**: Select an HTML file from your system

### گام 3: انتخاب نوع خروجی | Step 3: Select Output Type

<div dir="rtl">

برای خروجی نیز می‌توانید یکی از دو گزینه را انتخاب کنید:
- **Code**: کد تبدیل شده در فیلد بزرگ متنی نمایش داده می‌شود (می‌توانید آن را کپی کنید)
- **File**: فایل تبدیل شده در مسیر مشخص شده ذخیره می‌شود

**نکته**: می‌توانید همزمان از هر دو گزینه استفاده کنید. برای مثال، کد را در فیلد متنی ببینید و همچنین فایل را نیز ذخیره کنید.

</div>

**English:**

For output, you can also choose one of two options:
- **Code**: The converted code is displayed in the large text field (you can copy it)
- **File**: The converted file is saved at the specified path

**Note**: You can use both options simultaneously. For example, view the code in the text field and also save the file.

### گام 4: وارد کردن یا انتخاب ورودی | Step 4: Enter or Select Input

<div dir="rtl">

**اگر Code را انتخاب کرده‌اید:**
1. کد HTML خود را در فیلد بزرگ متنی سمت چپ وارد کنید

**اگر File را انتخاب کرده‌اید:**
1. روی دکمه **"Browse..."** کلیک کنید
2. فایل HTML مورد نظر خود را انتخاب کنید
3. می‌توانید محتوای فایل را در فیلد Code نیز مشاهده کنید (اگر به حالت Code تغییر دهید)

</div>

**English:**

**If you selected Code:**
1. Enter your HTML code in the large text field on the left

**If you selected File:**
1. Click the **"Browse..."** button
2. Select your desired HTML file
3. You can view the file content in the Code field as well (if you switch to Code mode)

### گام 5: تنظیم خروجی | Step 5: Configure Output

<div dir="rtl">

**اگر Code را برای خروجی انتخاب کرده‌اید:**
- کد تبدیل شده به صورت خودکار در فیلد سمت راست نمایش داده می‌شود

**اگر File را برای خروجی انتخاب کرده‌اید:**
1. (اختیاری) روی دکمه **"Browse..."** کلیک کنید و مسیر ذخیره فایل را انتخاب کنید
2. اگر مسیر را مشخص نکنید و ورودی فایل باشد، فایل خروجی به صورت خودکار با نام `[نام_فایل_ورودی]_django.html` در همان پوشه ذخیره می‌شود

</div>

**English:**

**If you selected Code for output:**
- The converted code will be automatically displayed in the field on the right

**If you selected File for output:**
1. (Optional) Click the **"Browse..."** button and select the save path for the file
2. If you don't specify a path and input is a file, the output file will be automatically saved with the name `[input_filename]_django.html` in the same folder

### گام 6: تبدیل | Step 6: Convert

<div dir="rtl">

1. روی دکمه **"Convert"** (در ستون وسط) کلیک کنید
2. پس از اتمام تبدیل:
   - اگر خروجی **Code** باشد، کد تبدیل شده در فیلد سمت راست نمایش داده می‌شود
   - اگر خروجی **File** باشد، فایل در مسیر مشخص شده ذخیره می‌شود
3. پیام موفقیت نمایش داده می‌شود

</div>

**English:**
1. Click the **"Convert"** button (in the middle column)
2. After conversion is complete:
   - If output is **Code**, the converted code is displayed in the field on the right
   - If output is **File**, the file is saved at the specified path
3. A success message will be displayed

### گام 7: پاک‌سازی | Step 7: Clear

<div dir="rtl">

برای شروع مجدد، روی دکمه **"Clear"** کلیک کنید تا تمام فیلدها پاک شوند.

</div>

**English:**

To start over, click the **"Clear"** button to clear all fields.

---

## تبدیل‌های انجام شده | Conversions Performed

<div dir="rtl">

برنامه به صورت خودکار موارد زیر را تبدیل می‌کند:

</div>

**English:**

The program automatically converts the following:

### 1. اضافه شدن `{% load static %}` | Adding `{% load static %}`

<div dir="rtl">

در ابتدای فایل HTML، تگ `{% load static %}` اضافه می‌شود (در صورت نبودن):

</div>

**English:**

The `{% load static %}` tag is added at the beginning of the HTML file (if not present):

```html
{% load static %}
<html>
  ...
</html>
```

### 2. تبدیل لینک‌های CSS | Converting CSS Links

<div dir="rtl">

```html
<!-- قبل -->
<link rel="stylesheet" href="css/style.css">

<!-- بعد -->
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

</div>

**English:**
```html
<!-- Before -->
<link rel="stylesheet" href="css/style.css">

<!-- After -->
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

### 3. تبدیل اسکریپت‌های JavaScript | Converting JavaScript Scripts

<div dir="rtl">

```html
<!-- قبل -->
<script src="js/main.js"></script>

<!-- بعد -->
<script src="{% static 'js/main.js' %}"></script>
```

</div>

**English:**
```html
<!-- Before -->
<script src="js/main.js"></script>

<!-- After -->
<script src="{% static 'js/main.js' %}"></script>
```

### 4. تبدیل تصاویر | Converting Images

<div dir="rtl">

```html
<!-- قبل -->
<img src="images/logo.png" alt="Logo">

<!-- بعد -->
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

</div>

**English:**
```html
<!-- Before -->
<img src="images/logo.png" alt="Logo">

<!-- After -->
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

### 5. تبدیل فایل‌های صوتی و ویدیویی | Converting Audio and Video Files

<div dir="rtl">

```html
<!-- قبل -->
<source src="media/video.mp4" type="video/mp4">

<!-- بعد -->
<source src="{% static 'media/video.mp4' %}" type="video/mp4">
```

</div>

**English:**
```html
<!-- Before -->
<source src="media/video.mp4" type="video/mp4">

<!-- After -->
<source src="{% static 'media/video.mp4' %}" type="video/mp4">
```

### 6. تبدیل srcset در تصاویر | Converting srcset in Images

<div dir="rtl">

```html
<!-- قبل -->
<img srcset="img-1x.jpg 1x, img-2x.jpg 2x">

<!-- بعد -->
<img srcset="{% static 'img-1x.jpg' %} 1x, {% static 'img-2x.jpg' %} 2x">
```

</div>

**English:**
```html
<!-- Before -->
<img srcset="img-1x.jpg 1x, img-2x.jpg 2x">

<!-- After -->
<img srcset="{% static 'img-1x.jpg' %} 1x, {% static 'img-2x.jpg' %} 2x">
```

---

## نکات مهم | Important Notes

### مواردی که تبدیل نمی‌شوند | Items That Are Not Converted

<div dir="rtl">

1. **لینک‌های HTTP/HTTPS** - لینک‌های خارجی تغییری نمی‌کنند
   ```html
   <link href="https://cdn.example.com/style.css"> <!-- بدون تغییر -->
   ```

2. **لینک‌های Data URI** - تصاویر base64 تبدیل نمی‌شوند
   ```html
   <img src="data:image/png;base64,..."> <!-- بدون تغییر -->
   ```

3. **لینک‌های از قبل تبدیل شده** - لینک‌هایی که قبلاً `{% static %}` دارند
   ```html
   <link href="{% static 'css/style.css' %}"> <!-- بدون تغییر -->
   ```

4. **لینک‌های پروتکل** - لینک‌هایی که با `//` شروع می‌شوند
   ```html
   <script src="//cdn.example.com/script.js"> <!-- بدون تغییر -->
   ```

</div>

**English:**
1. **HTTP/HTTPS Links** - External links remain unchanged
   ```html
   <link href="https://cdn.example.com/style.css"> <!-- unchanged -->
   ```

2. **Data URI Links** - Base64 images are not converted
   ```html
   <img src="data:image/png;base64,..."> <!-- unchanged -->
   ```

3. **Already Converted Links** - Links that already have `{% static %}`
   ```html
   <link href="{% static 'css/style.css' %}"> <!-- unchanged -->
   ```

4. **Protocol Links** - Links starting with `//`
   ```html
   <script src="//cdn.example.com/script.js"> <!-- unchanged -->
   ```

---

## ساختار پروژه | Project Structure

```
convert_to_django_template.py/
├── django_template_converter/     # Main package
│   ├── __init__.py               # Package settings
│   ├── core/                     # Main conversion module
│   │   ├── __init__.py
│   │   └── converter.py          # DjangoTemplateConverter class
│   ├── gui/                      # GUI module
│   │   ├── __init__.py
│   │   └── window.py             # DjangoTemplateConverterGUI class
│   └── utils/                    # Utility functions
│       ├── __init__.py
│       └── helpers.py            # Helper functions
├── tests/                        # Unit tests
│   ├── __init__.py
│   └── test_converter.py         # Converter tests
├── main.py                       # Main entry point
├── setup.py                      # Package setup file
├── requirements.txt              # Project dependencies
├── .gitignore                   # Git ignore file
└── README.md                    # This file
```

### توضیحات ساختار | Structure Description

<div dir="rtl">

- **`django_template_converter/`**: پکیج اصلی که شامل تمام منطق برنامه است
  - **`core/`**: منطق اصلی تبدیل HTML به Django Template (بدون وابستگی به GUI)
  - **`gui/`**: رابط کاربری گرافیکی با tkinter
  - **`utils/`**: توابع کمکی و کاربردی
  
- **`tests/`**: تست‌های واحد برای اطمینان از صحت عملکرد

- **`main.py`**: نقطه ورود اصلی برنامه که GUI را راه‌اندازی می‌کند

- **`setup.py`**: امکان نصب پروژه به عنوان یک پکیج Python

</div>

**English:**
- **`django_template_converter/`**: Main package containing all program logic
  - **`core/`**: Core logic for converting HTML to Django Template (independent of GUI)
  - **`gui/`**: Graphical user interface with tkinter
  - **`utils/`**: Helper utility functions
  
- **`tests/`**: Unit tests to ensure correct functionality

- **`main.py`**: Main entry point that launches the GUI

- **`setup.py`**: Allows installation of the project as a Python package

---

## عیب‌یابی | Troubleshooting

### مشکل: برنامه اجرا نمی‌شود | Problem: Application Won't Run

<div dir="rtl">

**راه حل:**
- مطمئن شوید Python 3.6+ نصب شده است:
  ```bash
  python --version
  ```
- وابستگی‌ها را دوباره نصب کنید:
  ```bash
  pip install --upgrade beautifulsoup4 lxml
  ```

</div>

**English - Solution:**
- Make sure Python 3.6+ is installed:
  ```bash
  python --version
  ```
- Reinstall dependencies:
  ```bash
  pip install --upgrade beautifulsoup4 lxml
  ```

### مشکل: خطای encoding | Problem: Encoding Error

<div dir="rtl">

**راه حل:**
- فایل HTML شما باید UTF-8 باشد
- اگر فایل شما encoding دیگری دارد، آن را به UTF-8 تبدیل کنید

</div>

**English - Solution:**
- Your HTML file must be UTF-8
- If your file has a different encoding, convert it to UTF-8

### مشکل: tkinter نصب نیست | Problem: tkinter Not Installed

<div dir="rtl">

**راه حل:**

**Linux:**
```bash
sudo apt-get install python3-tk
```

**macOS:**
```bash
brew install python-tk
```

**Windows:**
tkinter معمولاً به صورت پیش‌فرض با Python نصب است.

</div>

**English - Solution:**

**Linux:**
```bash
sudo apt-get install python3-tk
```

**macOS:**
```bash
brew install python-tk
```

**Windows:**
tkinter is usually pre-installed with Python.

---

## مشارکت | Contributing

<div dir="rtl">

برای مشارکت در پروژه:

1. Fork کنید
2. یک branch جدید ایجاد کنید (`git checkout -b feature/AmazingFeature`)
3. تغییرات خود را commit کنید (`git commit -m 'Add some AmazingFeature'`)
4. به branch خود push کنید (`git push origin feature/AmazingFeature`)
5. یک Pull Request باز کنید

</div>

**English:**

To contribute to the project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to your branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## مجوز | License

<div dir="rtl">

این پروژه تحت مجوز MIT منتشر شده است.

</div>

**English:**

This project is licensed under the MIT License.

---

## توسعه‌دهنده | Developer

<div dir="rtl">

برای سوالات و پیشنهادات، لطفاً یک Issue باز کنید.

</div>

**English:**

For questions and suggestions, please open an Issue.

---

## مثال کامل | Complete Example

<div dir="rtl">

فرض کنید یک فایل HTML به نام `blog.html` دارید:

</div>

**English:**

Suppose you have an HTML file named `blog.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <img src="images/logo.png" alt="Logo">
    <script src="js/jquery.min.js"></script>
    <script src="js/main.js"></script>
</body>
</html>
```

<div dir="rtl">

پس از تبدیل، فایل `blog_django.html` به این صورت خواهد بود:

</div>

**English:**

After conversion, the `blog_django.html` file will look like this:

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <img src="{% static 'images/logo.png' %}" alt="Logo">
    <script src="{% static 'js/jquery.min.js' %}"></script>
    <script src="{% static 'js/main.js' %}"></script>
</body>
</html>
```

---

## نسخه‌ها | Versions

<div dir="rtl">

- **v2.0** - رابط کاربری گرافیکی با tkinter
- **v1.0** - نسخه اولیه با رابط خط فرمان

</div>

**English:**
- **v2.0** - Graphical user interface with tkinter
- **v1.0** - Initial version with command line interface

---

<div dir="rtl">

**نکته:** این ابزار برای تبدیل خودکار لینک‌های استاتیک طراحی شده است. لطفاً فایل خروجی را بررسی کنید تا از صحت تبدیل اطمینان حاصل کنید.

</div>

**English - Note:** This tool is designed for automatic conversion of static links. Please review the output file to ensure conversion accuracy.
