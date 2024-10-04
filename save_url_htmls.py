import os
import re
import requests

# NOTE ON BELOW CODE THAT WAS REFACTORED AS IT DID NOT REPLACE SOME SPECIAL 
# CHARACTERS (-, .) WITH UNDERSCORE:
# 
# Breakdown of the call re.sub(r'[^\w\-_\.]', '_', url): 
#
# re.sub(): This function from the re module is used for substituting a regex 
# match with a replacement string. Here, it replaces matches with the 
# underscore (_).
#
# r'[^\w\-_\.]': This is the regular expression pattern. Let's decompose it:
#
# \w: This matches any "word" character, which includes letters, digits, and 
#     underscores ([A-Za-z0-9_]).
# \-: This specifically matches a literal hyphen (-). We escape the hyphen (\), 
#     so it’s treated as a character and not part of a range.
# \.: This matches a literal dot (.), escaped (\) because the dot in regular 
#     expressions is normally a wildcard character that matches any character.
# [^\w\-_\.]: The square brackets [] define a character class (a group of 
#             characters you're looking for). The ^ inside the brackets negates 
#             the class, meaning "match anything that is not in this set." 
#
# Therefore, this pattern matches any character that is not a word character 
# (\w), a hyphen (-), or a dot (.).
#
# def sanitize_filename(url):
#     """
#     Sanitize the URL to create a valid filename.
#     - Remove 'www.' from the URL.
#     - Replace non-alphanumeric characters with underscores.
#     """
#     url = url.replace("www.", "")  # Remove 'www.'
#     filename = re.sub(r'[^\w\-_\.]', '_', url)  # Replace special characters
#     return filename + ".html"

def sanitize_filename(url):
    """
    Sanitize the URL to create a valid filename.
    - Remove 'www.' from the URL.
    - Replace non-alphanumeric characters (including dots) with underscores.
    - Replace multiple underscores with a single underscore.
    """
    url = url.replace("www.", "")  # Remove 'www.'
    
    # Replace non-alphanumeric characters and dots with underscores
    filename = re.sub(r'[^\w]', '_', url)
    
    # Replace multiple underscores with a single underscore
    filename = re.sub(r'_+', '_', filename)
    
    return filename + ".html"

def save_html_from_urls(url_list, output_dir="./url_htmls"):
    """
    Fetch HTML content from the URLs and save to separate files.
    :param url_list: List of URLs to fetch.
    :param output_dir: Directory to save the HTML files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for url in url_list:
        try:
            # the header template used below copies from https://httpbin.org/headers with host 
            # and X-Amzn-Trace-Id keys removed
            HTTP_HEADERS = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9",
                "Priority": "u=0, i",
                "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "\"Windows\"",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "cross-site",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            }
            response = requests.get(url, headers=HTTP_HEADERS)
            response.raise_for_status()  # Raise an exception for HTTP errors
            filename = sanitize_filename(url)
            filepath = os.path.join(output_dir, filename)

            # Save the content to an HTML file
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(response.text)

            print(f"Saved {url} to {filepath}")
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")

if __name__ == '__main__':
    url_list = [
        "https://www.dataroma.com/m/home.php"
    ]
    save_html_from_urls(url_list)
