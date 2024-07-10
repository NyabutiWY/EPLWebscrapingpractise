# Practice Web Scraping and PDF Generation in Python

## Objective

The objective of this project is to practice web scraping and PDF generation in Python. Specifically, the project involves:

1. Scraping data from a website.
2. Processing and filtering the scraped data.
3. Generating a PDF report from the processed data using the ReportLab library.

## What I Learned

During this project, I gained valuable insights and skills in the following areas:

### Web Scraping

- **Libraries Used:** Learned to use libraries like `requests` and `BeautifulSoup` for web scraping.
- **Techniques:** Extracted data from HTML content by navigating the DOM, using tags, classes, and attributes.
- **Data Cleaning:** Processed raw HTML data to filter out unnecessary information and structure the data appropriately.

### PDF Generation

- **ReportLab Basics:** Understood the basics of creating PDF documents using the ReportLab library.
- **Table Creation:** Created tables in PDFs with various styles, including custom column widths, row heights, cell merging, and padding.
- **Table Styling:** Applied advanced styles to tables, such as alternating row colors and custom fonts.
- **Dynamic Data Handling:** Managed dynamic data input from web scraping to populate tables in the PDF.

### Challenges and Limitations

Despite the progress, there were some challenges and limitations:

- **Dynamic Content:** Handling dynamic content in web scraping, especially with JavaScript-rendered pages, posed challenges. Solutions like `selenium` might be required for such cases.
- **Table Overflow:** Managing table content overflow in PDFs, particularly with variable cell sizes, required careful handling to ensure the document layout remained consistent and readable.

## Code Example

### Web Scraping

```python
import requests
from bs4 import BeautifulSoup

url = "http://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

data = []
for item in soup.select(".desired-element"):
    data.append({
        "field1": item.select_one(".field1").text,
        "field2": item.select_one(".field2").text,
    })

print(data)
```
