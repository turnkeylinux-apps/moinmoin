Dependencies = []
generates_headings = False

def macro_HttpHostLink(macro, proto, port, desc):
    """generates href link in form of proto://HTTP_HOST:port"""
    return "<a href='%s://%s:%s'>%s</a>" % (proto,
                                            macro.request.environ['HTTP_HOST'],
                                            port, desc)

