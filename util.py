def compose(g, f):
    """
    python currying
        :param g: 
        :param f: 
    """
    def h(*args, **kwargs):
        """
        Parameter function gets passed down
            :param *args: 
            :param **kwargs: 
        """
        return g(f(*args, **kwargs))
    return h
