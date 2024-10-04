# BEFORE RUNNING THE FILES EXECUTE THE FOLLOWING IN THE TERMINAL FROM THE WORKING FOLDER:
pip install -r requirements.txt

## PROJECT STRUCTURE:

The project consists of two components:

1. save_url_htmls.py: This script takes a list of URLs, fetches their content using the requests library, and saves them to .html files. Each html file is named based on a name derived from the URL.

2. generate_csvs.py: This script reads a previously saved HTML file and provides its content for further use with the BeautifulSoup library. An example of data scrapping from the dataroma home page is implemented.


### save_url_htmls.py - FUNCTION SPEC:

1. sanitize_filename: Converts a URL into a valid filename by removing 'www.' and replacing special characters with underscores.

NOTE on Regular Expression usage to construct file names: 

re.sub(r'[^\w]', '_', url): This replaces all characters that are not word characters ([^\w]), including dots (.), with underscores (_).

re.sub(r'_+', '_', filename): This ensures that multiple consecutive underscores are replaced with a single underscore.

Now, regardless of how many special characters or dots are present in the URL, the file name will have only single underscores between segments.

2. save_html_from_urls: Fetches content from each URL and saves it in an HTML file inside a directory (set to url_htmls sub-directory). If the directory doesn't exist, it creates it.

### generate_csvs.py - FUNCTION SPEC:

read_html_for_soup: Opens an HTML file, reads its content, and returns it as a string for further use.

save_superinvestor_list, save_top_10_most_owned_list, and save_most_insider_buys: These three functions retrieve data from different parts of the dataroma home page and saves it to csv files under the csvs sub-folder.


