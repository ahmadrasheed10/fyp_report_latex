"""Independently check the recorded HTTP responses. Run after reproduce_checks.py."""
from pathlib import Path
import json, hashlib
root=Path(__file__).resolve().parent
raw=(root/'api_checks.json').read_bytes()
data=json.loads(raw)
records={r['id']:r for r in data['records']}
assert len(records)==16
assert all('transport_error' not in r for r in records.values())
models=records['registry']['response']['models']
names={m['model'] for m in models}
approved=set(records['privacy-config']['response']['deployment']['approved_for_sensitive'])
routes=['legacy','balanced','private','sensitive-balanced']
invalid=['empty','threshold-high','invalid-mode','threshold-low','quality-low','quality-high','zero-latency','too-long','missing-query']
validation=[]
for ident in invalid:
    r=records[ident]
    details=r['response'].get('detail',[])
    ok=r['status']==422 and bool(details) and all('loc' in e and 'type' in e for e in details)
    validation.append({'id':ident,'status':r['status'],'structured_error':ok,'errors':[{'location':e.get('loc'),'type':e.get('type')} for e in details]})
route_rows=[]
for ident in routes:
    r=records[ident]; body=r['response']; chosen=body.get('selected_model',body.get('chosen_model'))
    route_rows.append({'id':ident,'status':r['status'],'selected_model':chosen,'in_registry':chosen in names,'is_fallback':body.get('is_fallback'),'approved_for_sensitive':chosen in approved})
summary={'recorded_at_utc':data['recorded_at_utc'],'request_count':len(records),'http_status_matches':sum(r['status']==r['expected_status'] for r in records.values()),'registry_count':len(names),'approved_model_count':len(approved),'approved_models':sorted(approved),'valid_routing_responses':sum(r['status']==200 and r['in_registry'] for r in route_rows),'routing_requests':len(routes),'validation_rejections_with_details':sum(r['structured_error'] for r in validation),'invalid_requests':len(invalid),'privacy_eligible_selections':sum(r['approved_for_sensitive'] for r in route_rows if r['id'] in ['private','sensitive-balanced']),'privacy_requests':2,'keyword_result':records['keyword-positive']['response'],'routes':route_rows,'validation':validation,'evidence_sha256':hashlib.sha256(raw).hexdigest()}
(root/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
