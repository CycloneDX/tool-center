#!/usr/bin/env python3

from datetime import datetime, timezone
from json import dump as json_dump, load as json_load
from pathlib import Path
from re import compile as re_compile

REPO_ROOT = Path(__file__).parent.parent
TOOLS_JSON = REPO_ROOT / 'tools.json'
TOOLS_FOLDER = REPO_ROOT / 'tools'

_tool_fname_replace = re_compile('[^a-zA-Z0-9]+')


def make_tool_fname(t):
    from_file = t.get('_fromFile')
    name = t['name']
    return f'{Path(from_file).name}' if from_file \
        else f'{_tool_fname_replace.sub("_", name).lower()}.json'


with open(TOOLS_JSON) as ts:
    all_tools = json_load(ts)

spec_version = all_tools['specVersion']

now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')

for tool in all_tools['tools']:
    tfn = make_tool_fname(tool)
    print('tool', tool['name'], '->', tfn)
    with open(TOOLS_FOLDER / tfn, 'w') as tf:
        if '_fromFile' in tool:
            del tool['_fromFile']
        if 'repository_url' in tool and tool['repository_url'] is None:
            del tool['repository_url']
        if 'website_url' in tool and tool['website_url'] is None:
            del tool['website_url']
        json_dump({
            '$schema': 'https://cyclonedx.org/schema/tool-center-v2.tool.schema.json',
            'specVersion': spec_version,
            'tool': tool
        }, tf, indent=2)
