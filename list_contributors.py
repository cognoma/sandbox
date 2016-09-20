# This script is will list sandbox contributors and generate a markdown file.
# It is also an example that will be used in a continuous analysis workflow.
# See http://biorxiv.org/content/early/2016/08/11/056473 for more details.

import os

people = os.listdir('people')
handles = [x.strip('.md') for x in people if x != 'example.md']
handles = sorted(handles, key=str.lower)

markdown_text = "Here are all of the people playing in the sandbox:\n\n"
for handle in handles:
    markdown_text = markdown_text + '* ' + handle + '\n'

with open('sandbox_contributors.md', 'w') as markdown_fh:
    markdown_fh.write(markdown_text)
