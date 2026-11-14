# **Downloading Files Automatically Using Python**

**Automatic File Downloading** means using Python to download files from websites or URLs without manually clicking the download button.

For example:

- Download PDFs automatically.
- Download images from URLs.
- Download Excel and CSV files.
- Download multiple files at once.
- Automatically save files into folders.

## **1. Required Library**

We will use the Python `requests` library.

Install it:

```
pip install requests
```

## **2. Download a Single File**

```
import requestsurl = "https://example.com/sample.pdf"response = requests.get(url)with open("sample.pdf", "wb") as file:    file.write(response.content)print("File downloaded successfully!")
```

**How it works:**

1. `requests.get()` sends a request to the URL.
2. `response.content` gets the downloaded file.
3. `"wb"` opens a file in binary write mode.
4. `write()` saves the file to your computer.

## **3. Download Multiple Files Automatically**

Suppose you have multiple PDF URLs.

```
import requestsurls = [    "https://example.com/file1.pdf",    "https://example.com/file2.pdf",    "https://example.com/file3.pdf"]for i, url in enumerate(urls):    response = requests.get(url)    with open(f"file_{i+1}.pdf", "wb") as file:        file.write(response.content)    print(f"Downloaded file {i+1}")
```

## **4. Download Images Automatically**

```
import requestsurl = "https://example.com/image.jpg"response = requests.get(url)with open("image.jpg", "wb") as file:    file.write(response.content)print("Image downloaded!")
```

## **5. Better Version with Error Handling**

This version checks whether the download was successful.

```
import requestsurl = "https://example.com/sample.pdf"try:    response = requests.get(url, timeout=30)    response.raise_for_status()    with open("sample.pdf", "wb") as file:        file.write(response.content)    print("Download completed!")except requests.RequestException as e:    print("Download failed:", e)
```

## **6. Automatically Download Excel Files**

```
import requestsurl = "https://example.com/students.xlsx"response = requests.get(url, timeout=30)response.raise_for_status()with open("students.xlsx", "wb") as file:    file.write(response.content)print("Excel file downloaded successfully!")
```

## **7. Mini Project: Automatic File Downloader**

Beginner Project

[Prime Download Manager (PDM) — Fast, modern download manager for Windows, macOS & Linux](https://images.openai.com/static-rsc-4/z9mbCoYHRG8AmflMEkxz4e3bosBo8Q2W47W6Zvh1SvQgxjofj2u0oszSLunZyoAnXSkBXQZPTC-XKooKWucaxNxkwbkSW6wOxqdZoGr7AKFR7U-bSmImBq1L8P52fV1LuivIQjTGg4XUo3nxOqwbqj2do1owuzhYUBrBueSCQJg?purpose=inline)

[emizo59.github.io](https://emizo59.github.io/Prime-Download-Manager/?utm_source=chatgpt.com)

**Project features:**

- Accept a file URL from the user.
- Download the file automatically.
- Allow the user to enter a filename.
- Save files in a Downloads folder.
- Display download success or failure.

```
import requestsimport os# Create Downloads folderfolder = "Downloads"os.makedirs(folder, exist_ok=True)# Take URL from userurl = input("Enter File URL: ")# Take filenamefilename = input("Enter File Name: ")# Download filetry:    response = requests.get(url, timeout=30)    response.raise_for_status()    filepath = os.path.join(folder, filename)    with open(filepath, "wb") as file:        file.write(response.content)    print("File Downloaded Successfully!")    print("Saved at:", filepath)except requests.RequestException as e:    print("Download Error:", e)
```

## **8. Important Python Libraries**

| Library    | Purpose                        |
| ---------- | ------------------------------ |
| `requests` | Download files from URLs       |
| `os`       | Manage folders and files       |
| `shutil`   | Copy and move downloaded files |
| `urllib`   | URL handling and downloading   |
| `aiohttp`  | Asynchronous downloads         |
| `tqdm`     | Display download progress      |

## **9. Practice Projects**

1. **PDF Downloader:** Download multiple PDFs from URLs.
2. **Image Downloader:** Download images automatically.
3. **Bulk File Downloader:** Download multiple files using a list of URLs.
4. **Website Resource Downloader:** Download permitted resources from a website.
5. **Automatic Report Downloader:** Download daily reports from a provided URL.

## **Practice MCQs**

**Test your knowledge**

**1. Which library is commonly used to download files from URLs?**

A. Pandas

B. Requests

C. NumPy

D. Tkinter



**2. What does the 'wb' mode mean?**

A. Write Binary

B. Web Browser

C. Write Backup

D. Web Binary



**3. Which method sends an HTTP GET request?**

A. requests.post()

B. requests.get()

C. requests.send()

D. requests.download()



**4. Which method checks for HTTP errors?**

A. check_error()

B. raise_error()

C. raise_for_status()

D. verify_file()



**5. Which module helps create folders?**

A. os

B. math

C. random

D. time



Submit Answers

**Next practical step:** Build the Bulk File Downloader, which accepts multiple URLs and downloads all files automatically into a single folder.