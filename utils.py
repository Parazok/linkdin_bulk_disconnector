from os import system, name
import pandas as pd
import curlparser
from pathlib import Path


def make_excel_file(path):
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    df = pd.DataFrame({
        "urn": [],
        "firstName": [],
        "lastName": [],
        "headline": [],
        "createdAt": [],
        "publicIdentifier": [],
    })

    df.to_excel(writer, sheet_name='data', index=False)
    writer.save()


def make_excel_file(path):
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    df = pd.DataFrame({
        "urn": [],
        "firstName": [],
        "lastName": [],
        "headline": [],
        "createdAt": [],
        "publicIdentifier": [],
    })

    df.to_excel(writer, sheet_name='data', index=False)
    writer.save()


def write_to_excel(data, path):
    global total_connections, total_pages
    total_connections = len(data)
    total_pages = int(total_connections/40)
    print(f"writing {total_connections} items to excel", end=" ")
    # new dataframe with same columns
    df = pd.DataFrame(data)
    df_excel = pd.read_excel(path)
    result = pd.concat([df_excel, df], ignore_index=True)
    result.sort_values(by=['createdAt'], ascending=True, inplace=True)
    result.to_excel(path, index=False)
    print("done\n")


def pars_curl(path):
    curl_file = Path(path)
    if not curl_file.is_file():
        return False
    try:
        with open(path, "r", encoding="utf-8") as f:
            curl = f.read().replace("--compressed", "")
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

            return cookies, headers
    except Exception:
        return False


def write_session_files(cookies, headers):
    with open("./.session.cookies.dnttch", "w", encoding="utf-8") as f:
        f.write("\n".join([f"{k}wtf!$this$h!t{v}" for k, v in cookies.items()]))

    with open("./.session.headers.dnttch", "w", encoding="utf-8") as f:
        f.write("\n".join([f"{k}wtf!$this$h!t{v}" for k, v in headers.items()]))
        
    return True


def read_session_files():
    cookies = None
    headers = None
    try:
        with open("./.session.cookies.dnttch", "r", encoding="utf-8") as f:
            cookies = {}
            for l in f.readlines():
                k, v = l.strip().split("wtf!$this$h!t")
                cookies[k] = v

        with open("./.session.headers.dnttch", "r", encoding="utf-8") as f:
            headers = {}
            for l in f.readlines():
                k, v = l.strip().split("wtf!$this$h!t")
                headers[k] = v
    finally:          
        return cookies, headers


# clears terminal from all outputs


def clrscr():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
