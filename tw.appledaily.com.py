#!/usr/bin/env python3

import hashlib
import lxml.etree
import lxml.html
import requests

user_agent = 'Mozilla/5.0'

def main():
    url = 'https://tw.appledaily.com/new/realtime'

    r = requests.get(url, headers={'User-agent': user_agent}, timeout=5)
    body = lxml.html.fromstring(r.text)

    for a in body.cssselect('.rtddt a'):
        item_url = a.get('href')

        r = requests.get(item_url, headers={'User-agent': user_agent}, timeout=5)
        body = lxml.html.fromstring(r.text)

        hgroup_content_byte = lxml.etree.tostring(body.cssselect('hgroup')[0], encoding='utf-8')
        item_content_byte = lxml.etree.tostring(body.cssselect('.ndArticle_margin p')[0], encoding='utf-8')

        h = hashlib.sha256()
        h.update(hgroup_content_byte)
        h.update(item_content_byte)

        fingerprint = h.digest()
        hgroup_content = hgroup_content_byte.decode('utf-8')
        item_content = item_content_byte.decode('utf-8')

if __name__ == '__main__':
    main()
