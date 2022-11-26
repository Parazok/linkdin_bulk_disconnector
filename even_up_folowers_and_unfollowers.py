import os
from pathlib import Path
from time import sleep
import requests
from pprint import pprint
import pandas as pd
from openpyxl import load_workbook
import concurrent.futures
import curlparser

total_connections = 2000
total_pages = int(total_connections/40)
CURL_FILE_PATH = "./curl.txt"
EXCEL_FILE_PATH = "./result.xlsx"

def extract_connections(first_page = 0, last_page = 20):  
    def process(i):
        raw = get_page_raw_data(i)
        return extract_page_data(raw)
        
    all_data = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
            for result in executor.map(process, range(first_page, last_page + 1)):
                all_data.extend(result)

    
    write_to_excel(all_data)

        

def extract_page_data(raw_json):
    page_data = {}
    print("extracting data from each item ...")
    print("items_done", end=": ")
    raw_data = raw_json.get("included", None)
    
    for j, item_raw in enumerate(raw_data):
        urn = item_raw.get("entityUrn", None).replace("urn:li:fsd_profile:","").replace("urn:li:fsd_connection:","")
        try:
            item = page_data[urn]
        except:
            item = dict()
        fname = item_raw.get("firstName", None)
        lname = item_raw.get("lastName", None)
        headline = item_raw.get("headline", None)
        created_at = item_raw.get("createdAt", None)
        public_id = item_raw.get("publicIdentifier", None)
        
        if urn:
            item["urn"] = urn
        
        if fname:
            item["firstName"] = fname
        
        if lname:
            item["lastName"] = lname
        
        if headline:
            item["headline"] = headline
            
        if created_at:
            item["createdAt"] = created_at
        
        if public_id:
            item["publicIdentifier"] = public_id
            
        page_data[urn] = item
        
    print("all done!\n\n")

    return page_data.values()


def get_page_raw_data(page):
    print(f"{page} ...", end=" ")

    start = page * 40
    params = {
        'decorationId': 'com.linkedin.voyager.dash.deco.web.mynetwork.ConnectionListWithProfile-15',
        'count': '40',
        'q': 'search',
        'sortType': 'RECENTLY_ADDED',
        'start': start,
    }

    response = requests.get('https://www.linkedin.com/voyager/api/relationships/dash/connections', params=params, cookies=cookies, headers=headers)
        
    
    print("done","--"*10,"\n")

    return response.json()


# def sort_connections_file_by_oldest_to_new(path=EXCEL_FILE_PATH):
#     print("sorting out")


    
    
def remove_connections(count, path=EXCEL_FILE_PATH):
    def process(row):
        print("removing ", row.firstName)


        params = {
            'action': 'removeFromMyConnections',
        }

        json_data = {
            'connectedMember': f'urn:li:fsd_profile:{row.urn}',
        }

        response = requests.post('https://www.linkedin.com/voyager/api/relationships/dash/connections', params=params, cookies=cookies, headers=headers, json=json_data)
        print("removing ", row.firstName, " done!")

        
    df = pd.read_excel(path)[:count]
    print("\n\nwill remove following people:\n")
    for row in df.itertuples(index=True, name='connections'):
        print(row.firstName, row.lastName)
        
    inp = input("proceed???:(y/N)")
    if inp != "y":
        return
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
            for result in executor.map(process, df.itertuples(index=True, name='connections')):
                # all_data.extend(result)
                pass
            

def pars_curl():
    global headers, cookies
    with open(CURL_FILE_PATH, "r") as f:
            curl = f.read().replace("--compressed","")
            result = curlparser.parse(curl)
            headers_raw = dict(result.header)
            headers = dict()
            for k, v in headers_raw.items():
                headers[k.strip()] = v.strip()
            raw_cookies = headers['cookie'].strip().split(';')
            del headers['cookie']
            cookies = {}
            for c in raw_cookies:
                c = c.strip().split('=')
                k = c[0].strip()
                v = '='.join(c[1:])
                cookies[k] = v.strip()

            
            

    
    

txt = """enter 1 for extracting connections and making excel file
enter 2 for unconnecting some of your connections
enter 3 for deleting connections excel file (!! Danger !!)
enter 0 to quite..
"""

def main():
    curl_file = Path(CURL_FILE_PATH)
    if not curl_file.is_file():
        print("please make a file named \"curl.txt\" in current directory and put one of your linkdin requests as curl in it; then try again.")
        return
    
    pars_curl()
    
    
    while True:
        try:    
            print(txt)
            inp = int(input("what to do?:"))
            if inp == 1:
                
                print(f"starting up... total pages: {total_pages}")
                make_excel_file()
                extract_connections(0,total_pages)
                # sort_connections_file_by_oldest_to_new()
                print("\n\nfinish..")
            
            elif inp == 2:
                excel_file = Path(EXCEL_FILE_PATH)
                if not excel_file.is_file():
                    make_excel_file()
                    extract_connections(0,total_pages)
                
                count = int(input("How much?:"))
                remove_connections(count)
                sleep(10)
                make_excel_file()
                extract_connections(0,total_pages)
                
                
            elif inp == 3:
                make_excel_file()
            
            elif inp == 0:
                break
        except TypeError as e:
            print("\n\n\n\nbad input... try again..\n\n", e)
            
    print("Bye Bye!")
    
if __name__ =='__main__':
    main()