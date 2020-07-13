import argparse
from collections import deque


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''


bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


# initialise args
def init_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('directory', help='directory for web pages',
                    type=str)
    return ap.parse_args()


# check for directory and create if not existing
def create_dir(dir_path):
    import os
    try:
        os.mkdir(dir_path)
        print(f'Directory {dir_path} created')
    except FileExistsError:
        print(f'Directory {dir_path} already exists')


# write to file
def get_data(directory, url):
    match_url = url.replace('.', '_')
    if match_url in globals():
        print(globals().get(match_url))
        filename = url[:url.rindex('.')]
        with open(f'{directory}/{filename}.txt', 'w') as f:
            f.write(globals().get(match_url))
            f.close()
    elif [s for s in globals() if url in s]:
        with open(f'{directory}/{url}.txt', 'r') as f:
            print(f.read())
            f.close()
    else:
        print('404 error')


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
            history.pop() # current page
            get_data(args.directory, history.pop()) # previous page
        except IndexError:
            'No more URLs in history'
    else:
        get_data(args.directory, txt)
        history.append(txt)
