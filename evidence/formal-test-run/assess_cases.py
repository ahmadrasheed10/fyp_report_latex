import json,hashlib
from pathlib import Path
root=Path(__file__).resolve().parent
raw=(root/'api_checks.json').read_bytes(); run=json.loads(raw)
r={x['id']:x for x in run['records']}
def body(k): return r[k].get('response',{})
def ok(k): return r[k].get('status')==200
def chosen(k): return body(k).get('selected_model',body(k).get('chosen_model'))
models=body('registry').get('models',[])
names=[m.get('model') for m in models]
policy=body('privacy-config').get('deployment',{})
approved=set(policy.get('approved_for_sensitive',[]))
invalid=['empty','missing-query','too-long','threshold-low','threshold-high','quality-low','quality-high','zero-latency','invalid-mode']
checks={
'TC-01':{'HTTP 200':ok('registry'),'Nonempty registry':bool(names),'Distinct present identifiers':all(isinstance(n,str) and n for n in names) and len(set(names))==len(names)},
'TC-02':{'Legacy HTTP 200':ok('legacy'),'Legacy registered model':chosen('legacy') in names,'Boolean fallback flag':isinstance(body('legacy').get('is_fallback'),bool),'Decision reasons present':bool(body('legacy').get('reasons')),'Balanced HTTP 200':ok('balanced'),'Balanced registered model':chosen('balanced') in names,'Balanced mode returned':body('balanced').get('mode')=='balanced'},
'TC-03':{k:r[k].get('status')==422 and bool(body(k).get('detail')) and all(e.get('loc') and e.get('type') for e in body(k).get('detail',[])) for k in invalid},
'TC-04':{'Privacy config HTTP 200':ok('privacy-config'),'Approved set nonempty':bool(approved),'Private HTTP 200':ok('private'),'Selected model approved':chosen('private') in approved},
'TC-05':{'Sensitive requests enabled':policy.get('allow_sensitive_queries') is True,'Sensitive routing HTTP 200':ok('sensitive-balanced'),'Sensitivity preserved':body('sensitive-balanced').get('sensitive') is True,'Selected model approved':chosen('sensitive-balanced') in approved},
'TC-06':{'Keyword configured':'confidential' in body('privacy-config').get('sensitivity_rules',{}).get('keywords',[]),'Sensitivity HTTP 200':ok('keyword-positive'),'Sensitive label':body('keyword-positive').get('sensitivity')=='sensitive','Keyword explanation':'confidential' in body('keyword-positive').get('reason','').lower()}
}
results={k:{'status':'Passed' if all(v.values()) else 'Failed','criteria':v} for k,v in checks.items()}
out={'recorded_at_utc':run['recorded_at_utc'],'server_build_identifier':'Not exposed; cannot establish build reproducibility','scope':'Documented API and selection checks only; not generated-answer quality or end-to-end privacy','raw_evidence_sha256':hashlib.sha256(raw).hexdigest(),'executed':6,'passed':sum(v['status']=='Passed' for v in results.values()),'failed':sum(v['status']=='Failed' for v in results.values()),'not_executed':0,'cases':results}
(root/'case_results.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
