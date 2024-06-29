import logging


log_id = 'sphinx-keywords'
logger = logging.getLogger(log_id)
handler = logging.FileHandler(f'{log_id}.log')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def on_doctree_resolved(app, doctree, docname):  # TODO: type hints
    """TODO: Description"""
    logger.info(docname)
    

def setup(app):  # TODO: type hints
    """TODO: Description"""
    # https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx-core-events
    app.connect('doctree-resolved', on_doctree_resolved)
    return {
        'version': '0.0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
