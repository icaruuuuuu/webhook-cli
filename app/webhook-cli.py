#!/usr/bin/env python3
import argparse
import os

def readMd(file):
    with open(file) as f:
        msg = ''
        for line in f.readlines(): msg += line + '\\n'

        return msg

def makeJson(args, usefile):
    if usefile:
        msg = readMd(args.file)
    else:
        msg = args.message

    with open('/tmp/tmp.json', 'w') as t:
        t.write('{\n\t"content":' + f'"{msg}"' + '\n}\n')
        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", help="Message to be sent to the webhook.")
    parser.add_argument("-f", "--file", help="Markdown file to be sent to the webhook. Alternative to -m if your message is too complex")
    parser.add_argument("url", help="Discord webhook URL")

    args = parser.parse_args()
    usefile = True if args.file else False
    url = args.url

    makeJson(args, usefile)

    exit_status = os.system(f'curl -i -H "Accept: application/json" -H "Content-Type:application/json" -X POST --data @/tmp/tmp.json {url}')
    print(exit_status)


if __name__ == "__main__":
    main()
