#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import webbrowser
import re

# URLs taken from stdin (for service)
url_input = sys.stdin.read()

# URL Regex created John Gruber
# http://daringfireball.net/2010/07/improved_regex_for_matching_urls
# Pythonized: https://gist.github.com/705383
url_regex = re.compile(ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-'
ur'z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+'
ur'|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018'
ur'\u2019]))')

# Grab the urls
urls_match = url_regex.findall(url_input)
urls = [url_list[0] for url_list in urls_match]

# Open in default webbrowser
for url in urls:
    webbrowser.open_new_tab(url)
