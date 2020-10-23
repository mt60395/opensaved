#!/usr/bin/env python3

def openLinks(name):
    import json
    inputFile = open("config.json")
    config = json.load(inputFile)

    links = None
    for i in config:
        if i == name:
            links = config[i]
    if links:
        import webbrowser
        for i in links:
            webbrowser.open(i)
    else:
        print("Link set not found.")

if __name__ == "__main__":
    linkSet = input("Set Name: ")
    openLinks(linkSet)
