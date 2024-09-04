#!/usr/bin/env python3

import json
import sys

if len(sys.argv) != 2:
    print("Usage: ./extract_markdown.py <path_to_notebook.ipynb>")
    sys.exit(1)

notebook_path = sys.argv[1]

with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook_data = json.load(f)

for cell in notebook_data['cells']:
    if cell['cell_type'] == 'markdown':
        print(''.join(cell['source']))
