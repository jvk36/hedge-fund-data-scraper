from bs4 import BeautifulSoup
import csv

def read_html_for_soup(file_path):
    """
    Reads the HTML file content and returns it for use with BeautifulSoup.
    :param file_path: The path to the saved HTML file.
    :return: The HTML content as a string.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()
        return html_content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    
def save_superinvestor_list(soup):
  superinvestors_ul = soup.select_one("#port_body > ul")
  superinvestors_a_tags = superinvestors_ul.select("a")
  superinvestors = [s.contents[0] for s in superinvestors_a_tags] 
  # print(superinvestors)

  file_name = "./csvs/superinvestors.csv"
  with open(file_name, 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(superinvestors)
    

def save_top_10_most_owned_list(soup):
  top_10_most_owned_td = soup.select_one('#t10 > tbody > tr:nth-child(1) > td:nth-child(1)')
  top_10_most_owned_a_tags = top_10_most_owned_td.select("a")
  top_10_most_owned = [[t.contents[0], t.contents[1].text.replace(" - ", "")] 
                       for t in top_10_most_owned_a_tags if t.contents[0] != '▾']  
  # print(top_10_most_owned)

  file_name = "./csvs/top_10_most_owned.csv"
  with open(file_name, 'w', newline='') as file:
      writer = csv.writer(file)
      for row in top_10_most_owned:
        writer.writerow(row)
    
def save_most_insider_buys(soup):
  most_insider_buys_tbody = soup.select_one('#ins_sum > table > tbody')
  most_insider_buys_td_st_tags = most_insider_buys_tbody.select("tr > td.st")  
  most_insider_buys_td_cnt_tags = most_insider_buys_tbody.select("tr > td.cnt")  
  most_insider_buys_td_amt_tags = most_insider_buys_tbody.select("tr > td.amt")  

  data_st = [d.text for d in most_insider_buys_td_st_tags]
  data_cnt = [d.text for d in most_insider_buys_td_cnt_tags]
  data_amt = [d.text for d in most_insider_buys_td_amt_tags]
  data = list(zip(data_st, data_cnt, data_amt))

  # print(data)
  file_name = "./csvs/most_insider_buys.csv"
  with open(file_name, 'w', newline='') as file:
      writer = csv.writer(file)
      for row in data:
        writer.writerow(row)


if __name__ == '__main__':
  file_path = "./url_htmls/https_dataroma_com_m_home_php.html"  # Adjust with your file path
  html_content = read_html_for_soup(file_path)

  if html_content:
    soup = BeautifulSoup(html_content, "html.parser")
    # print(soup.prettify())  # Example: print prettified HTML content
    
    save_superinvestor_list(soup)
    save_top_10_most_owned_list(soup)
    save_most_insider_buys(soup)

  