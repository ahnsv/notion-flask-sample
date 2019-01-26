import requests as req
from notion.client import NotionClient

sample = [{"title": "ㅗㅜㅑ"}, {"title": "ㅗㅜㅑ"}, {"title": "ㅗㅜㅑ"}]
text = filter(lambda block: "title" in block, sample)
# ext_srcs = filter(lambda block: block not in text, page)


def curry(func):
    f_args = []
    f_kwargs = {}

    def f(*args, **kwargs):
        nonlocal f_args, f_kwargs
        if args or kwargs:
            f_args += args
            f_kwargs.update(kwargs)
            return f
        else:
            return func(*f_args, *f_kwargs)
    return f

# TODO: make curry decorator work
@curry
def iterate_thru():
    for i in text:
        yield i

@curry
def add(*args):
    sum = 0
    for item in args:
        sum += item
    return sum

@curry
def take(f, li):
    for i in li:
        if len(li):
            yield(i)

a1 = add(1)
a2 = a1(2)

# TODO: Implement Pipe decorator class for functional programming
for item in iterate_thru():
    try:
        print(item)
    except ValueError:
        print("Value Error")
