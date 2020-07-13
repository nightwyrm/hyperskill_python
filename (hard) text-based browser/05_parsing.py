import argparse, requests, os
from collections import deque
from bs4 import BeautifulSoup as bs


# initialise args
def init_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('directory', help='directory for web pages',
                    type=str)
    return ap.parse_args()


# check for directory and create if not existing
def create_dir(dir_path):
    try:
        os.mkdir(dir_path)
        print(f'Directory {dir_path} created')
    except FileExistsError:
        print(f'Directory {dir_path} already exists')


# process url to get data
def get_data(directory, url):
    try:
        r = requests.get('https://' + url if 'https' not in url else url)
        if r:
            output = parse_html(r.content)
            write_file(directory, url, output)
        else:
            print('error - failed request')
    except ConnectionError:
        print('Connection error')


# parse web page data
def parse_html(page):
    soup = bs(page, 'html.parser')
    output = ''
    for tg in soup.find_all(['[document]', 'head', 'script', 'style',
             'body', 'html', 'h1', 'h2', 'h3', 'h4', 'h5',
             'h6', 'title',
             'table', 'div', 'li', 'form',
             'img', 'tr', '\n']):
        output += tg.text.strip()
    print(output)
    return output


# write cache data to file
def write_file(directory, url, text):
    if 'https' in url:
        url = url.lstrip('https://')
    if 'www' in url:
        url = url.lstrip('www.')
    filename = url[:url.rindex('.')]
    with open(f'{directory}/{filename}.txt', 'w') as f:
        f.write(text)
        f.close()


# main code
args = init_args()
create_dir(args.directory)
history = deque()
while True:
    txt = input()
    if txt == 'exit':
        exit()
    elif txt == 'back':
        try:
            history.pop()  # current page
            get_data(args.directory, history.pop())  # previous page
        except IndexError:
            'No more URLs in history'
    elif f'{txt}.txt' in os.listdir(args.directory):
        with open(f'{args.directory}/{txt}.txt', 'r') as f:
            print(f.read())
            f.close()
    elif '.' not in txt:
        print('error - invalid URL')
    else:
        get_data(args.directory, txt)
        history.append(txt)
