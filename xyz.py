python -c "import json; d=json.load(open('knowledge/incidents.json',encoding='utf-8')); print('INCIDENTS IN incidents.json:', len(d)); print([x['incident_id'] for x in d])"
