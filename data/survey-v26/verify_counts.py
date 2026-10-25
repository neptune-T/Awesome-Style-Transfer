"""Check companion CSVs using only the Python standard library."""
from pathlib import Path
import csv,json,hashlib
def main():
 D=Path(__file__).resolve().parent
 get=lambda p:list(csv.DictReader((D/p).open(encoding='utf-8-sig',newline='')))
 c=get('catalogue.csv');s=get('evidence_selection.csv');e=get('evidence_register.csv')
 assert len(c)==136 and len({x['cite_key'] for x in c})==136
 assert sum(x['scope']=='core' for x in c)==108
 assert {x['cite_key'] for x in c}=={x['cite_key'] for x in s if x['catalogue_included']=='yes'}
 selected={x['cite_key'] for x in e};assert len(e)==192 and len(selected)==39
 assert selected=={x['cite_key'] for x in s if x['evidence_sample']=='yes'}
 assert all(x['paper_url'].startswith('https://') for x in c)
 assert all(x['source_url'] and x['locator'] and x['pdf_page'] for x in e)
 ids={x['record_id'] for x in e};assert len(ids)==192
 assert selected<={x['cite_key'] for x in get('source_manifest.csv')}
 reuse=get('protocol_reuse.csv');binding=get('protocol_binding.csv');cons=get('protocol_consistency.csv')
 for x in reuse+binding+cons:
  assert x['cite_key'] in selected
  assert set(x['records'].split(';'))<=ids,(x['cite_key'],x['records'])
 acquired=[x for x in reuse if x['per_style_acquisition']!='statistic_from_exemplar']
 out={'cross_family_state_portability':(sum('cross' in x['portability_evidence'] for x in acquired),len(acquired)),'direct_reference_only_leakage_metric':(sum(x['direct_leakage_metric']=='yes' for x in binding),len(binding)),'quantified_occlusion_reappearance':(sum(x['reappearance_quantified']=='yes' for x in cons),len(cons))}
 assert list(out.values())==[(0,26),(0,20),(0,16)]
 for name,digest in json.loads((D/'file_manifest.json').read_text()).items():assert hashlib.sha256((D/name).read_bytes()).hexdigest()==digest,name
 print('PASS: counts, selection crosswalk, source anchors, record joins and hashes')
 for name,(n,d) in out.items():print(f'{name}: {n}/{d}')
if __name__=='__main__':main()
