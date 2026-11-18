"""Reproduce API-contract observations, not LLM answer-quality benchmarks.
Run: python reproduce_checks.py
Uses synthetic prompts only; saves complete responses and explicit checks.
"""
import json, urllib.request, urllib.error, hashlib
from pathlib import Path
from datetime import datetime, timezone

BASE = 'https://optiroute-ai-phi.vercel.app'
OUT = Path(__file__).resolve().parent
q = 'Explain binary search.'
cases = [
 ('registry','/api/models',None,200),
 ('privacy-config','/api/privacy',None,200),
 ('legacy','/api/route',{'query':q,'router':'legacy','threshold':0.95},200),
 ('balanced','/api/route',{'query':q,'router':'multi_objective','mode':'balanced'},200),
 ('private','/api/route',{'query':q,'router':'multi_objective','mode':'private'},200),
 ('sensitive-balanced','/api/route',{'query':'This is confidential proprietary information.','router':'multi_objective','mode':'balanced','sensitive':True},200),
 ('keyword-positive','/api/sensitivity',{'query':'This is confidential proprietary information.'},200),
 ('empty','/api/route',{'query':''},422),
 ('threshold-high','/api/route',{'query':q,'threshold':1.5},422),
 ('invalid-mode','/api/route',{'query':q,'router':'multi_objective','mode':'invalid'},422),
 ('threshold-low','/api/route',{'query':q,'threshold':0.49},422),
 ('quality-low','/api/route',{'query':q,'quality_floor':-0.1},422),
 ('quality-high','/api/route',{'query':q,'quality_floor':1.1},422),
 ('zero-latency','/api/route',{'query':q,'latency_budget_ms':0},422),
 ('too-long','/api/route',{'query':'x'*20001},422),
 ('missing-query','/api/route',{},422),
]
records=[]
for ident,path,body,expected in cases:
    req=urllib.request.Request(BASE+path,data=None if body is None else json.dumps(body).encode(),headers={'Content-Type':'application/json','Accept':'application/json'})
    stamp=datetime.now(timezone.utc).isoformat()
    try:
        with urllib.request.urlopen(req,timeout=25) as response:
            status=response.status; raw=response.read()
    except urllib.error.HTTPError as error:
        status=error.code; raw=error.read()
    except Exception as error:
        records.append(dict(id=ident,path=path,request=body,utc=stamp,transport_error=str(error),passed=False))
        print(ident,'TRANSPORT ERROR',flush=True); continue
    try: data=json.loads(raw)
    except ValueError: data={'raw_text':raw.decode(errors='replace')}
    records.append(dict(id=ident,path=path,request=body,utc=stamp,status=status,expected_status=expected,passed=status==expected,response=data,response_sha256=hashlib.sha256(raw).hexdigest()))
    print(ident,status,'PASS' if status==expected else 'FAIL',flush=True)
result={'base_url':BASE,'recorded_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'HTTP contract and returned selection only; no verified model execution, quality, cost, or inference latency.','records':records}
(OUT/'api_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('Saved',len(records),'observations to',OUT/'api_checks.json')
