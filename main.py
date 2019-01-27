from notion.client import NotionClient
from functools import reduce, partial
from operator import add, mul, neg
from toolz import curry, pipe

# client = NotionClient(
#     token_v2="ce3156b6ba04b9aab71a05479733bab47b5165ac04c1e83f405d2889cc05687e55e1aa55e3c140490c9e77421c525bcfa32a7ec026ff22e192210a8688c6937ee2ba24b87473bbcc63b2b4217d29", start_monitoring=False)
# page = client.get_block(
#     "https://www.notion.so/taebae/2018-by-4ceee3ab2dc74897b9b2c6850655cc3e")
sample = [{"title": "ㅗㅜㅑ"}, {"title": "ㅗㅜㅑ"}, {"title": "ㅗㅜㅑ"}]
text = filter(lambda block: "title" in block, sample)
# ext_srcs = filter(lambda block: block not in text, page)
sample_list = [
    [1, 2],
    3, 4, 5,
    [6, 7, 8],
    [9, 10]
]


def compose(*funcs):
    return reduce(lambda f, g: lambda x: f(g(x)),  funcs, lambda x: x)


add = curry(add)
mul = curry(mul)
add_and_mul = compose(neg, mul(2), add(2))


@curry
def calc(li):
    return reduce(lambda acc, i: acc + add_and_mul(i), li)


@curry
def odd(li):
    return filter(lambda i: i % 2 == 1, li)


def i_range(stop):
    i = 0
    while(i < stop):
        yield i
        i += 1


execute = compose(calc, odd, i_range)

print(calc(i_range(100)))
print(execute(100))
