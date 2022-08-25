#!/usr/bin/env python3

import json
import sys
from urllib import request    
from urllib.error import HTTPError
from pkg_resources import parse_version    


def main():
    return print(*versions(sys.argv[1]), sep='\n')


def versions(pkg_name):
    flags = sys.argv[1:5]
    url = f'https://pypi.python.org/pypi/{pkg_name}/json'
    try:
        response = request.urlopen(url).read()
    except HTTPError as e:
        return [e.msg]
    releases = json.loads(response)['releases']
    if '--latest' in flags:
        return [sorted(releases, key=parse_version, reverse=True)[0]]
    return sorted(releases, key=parse_version, reverse=False)


if __name__ == '__main__':
    print(*versions(sys.argv[1]), sep='\n')
