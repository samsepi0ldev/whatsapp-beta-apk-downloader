## Description

This is a Python script that automates the process of downloading the beta version of WhatsApp from the APKMirror website. It uses various Python libraries, including `requests`, `BeautifulSoup`, and `clint.textui`, to perform this task. Below, we explain how to use the script and detail its operation.

## Usage

1. Make sure you have the necessary libraries installed. You can install them by running the following command:
   ```shell
   $ pip install -r requirements.txt
   $ python wa_downloader.py
2. Run the Python script. It will initiate the process of downloading the beta version of WhatsApp from the APKMirror website.

## Operation
1. The script starts by defining the base URL (host) and user headers to simulate a web browser.

2. It then makes an HTTP request to the WhatsApp Beta homepage on APKMirror, parses the HTML content of the page with BeautifulSoup, and finds links to different versions of WhatsApp.

3. The script searches for the link to the beta version of WhatsApp, identifying it by the keyword "beta" in the link's text.

4. Once the link to the beta version is found, the script extracts the version of WhatsApp from the link's text.

5. The script proceeds to the download page for the beta version of WhatsApp and extracts the link to download the APK file.

6. After obtaining the download link, the script analyzes it to find the direct link to the APK file.

7. Next, it initiates the download process of the APK file, displaying progress with a progress bar.

8. The APK file is downloaded to the working directory with a name that includes the application's version.

Note: This script is specific to the APKMirror website and the structure of its pages. Any changes in the website's structure may break the script's functionality. Ensure that you use it in compliance with APKMirror's terms of service and for legal and ethical purposes.