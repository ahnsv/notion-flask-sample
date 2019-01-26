from notion.client import NotionClient
import requests as req

client = NotionClient(
    token_v2="ce3156b6ba04b9aab71a05479733bab47b5165ac04c1e83f405d2889cc05687e55e1aa55e3c140490c9e77421c525bcfa32a7ec026ff22e192210a8688c6937ee2ba24b87473bbcc63b2b4217d29")
page = client.get_block(
    "https://www.notion.so/taebae/2018-by-4ceee3ab2dc74897b9b2c6850655cc3e")

text = filter(lambda block: "title" in block, page)
ext_srcs = filter(lambda block: block not in text, page)
for value in text:
    try:
        print(value)
    except ValueError:
        print("Value Error")
for value in ext_srcs:
    try:
        print(value)
    except ValueError:
        print("Value Error")
