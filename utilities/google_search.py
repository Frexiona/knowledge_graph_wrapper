# -*- coding: utf-8 -*-
# @Time    : 05/02/2020
# @Author  : Haolin Zhang
# @File    : google_search.py
# @Software: VS Code

from googlesearch import search


def google_search(query, num=10):
    urls = list()
    # query : query string that we want to search for.
    # tld : tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain.
    # lang : lang stands for language.
    # num : Number of results we want.
    # start : First result to retrieve.
    # stop : Last result to retrieve. Use None to keep searching forever.
    # pause : Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
    # Return : Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
    for url in search(query, tld='com', lang='en', num=num, start=0, stop=None, pause=2.0):
        urls.append(url)

    return urls


if __name__ == '__main__':
    query = 'apple'
    print(google_search('ibm ireland'))
