class Parser:
    'Notion Page Parser'
    block_map = {
        "image": [],
        "divider": [],
        "link_to_page": [],
        "column_list": []
    }
    blocks = []

    def __init__(self, token, page_url):
        self.token = token
        self.page_url = page_url

    def push_to_dict(self, block):
        "Handle other blocks that have no title"
        try:
            block
        except NameError:
            return
        Parser.block_map[block.type].append(block)

    def append_text(self, block):
        "Append to text list"
        try:
            block
        except Exception:
            raise NameError
        Parser.blocks.append(block.title)

    def get_text(self):
        "Text getter"
        return Parser.blocks

    def get_block_map(self):
        "Block getter"
        return Parser.block_map
