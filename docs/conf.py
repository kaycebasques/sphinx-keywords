project = 'sphinx-extension'
copyright = '<YEAR>, <NAME>'
author = '<NAME>'
release = '0.0.1'

extensions = ['sphinx-extension']

templates_path = ['_templates']
exclude_patterns = [
    '_build',
    'build.sh',
    'venv', 
]

html_theme = 'alabaster'
