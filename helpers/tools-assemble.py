#!/usr/bin/env python3

from datetime import datetime, timezone
from json import dump as json_dump, load as json_load
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
TOOLS_JSON = REPO_ROOT / 'tools.json'
TOOLS_FOLDER = REPO_ROOT / 'tools'

tools = []

license_ = {
    'id': 'CC-BY-SA-4.0',
    'name': 'Creative Commons Attribution-ShareAlike 4.0 International',
    'url': 'https://creativecommons.org/licenses/by-sa/4.0/'
}

now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')

for tfn in sorted(TOOLS_FOLDER.glob('*.json')):
    print('loading', tfn, '...')
    with open(tfn) as t:
        tool = json_load(t)
        tool['tool']['_fromFile'] = tfn.name
        tools.append(tool['tool'])

print('writing', TOOLS_JSON, '...')
with open(TOOLS_JSON, 'w') as ts:
    json_dump({
        '$schema': 'https://cyclonedx.org/schema/tool-center-v2.schema.json',
        'specVersion': '2.0',
        'last_updated': now,
        'license': license_,
        'tools': tools
    }, ts, indent=2)
