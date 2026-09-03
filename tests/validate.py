"""Validate every data file against its schema. Run: python tests/validate.py"""
import json, sys, pathlib
try:
    import jsonschema
except ImportError:
    sys.exit("pip install jsonschema")
root = pathlib.Path(__file__).resolve().parents[1]
pairs = [("data/ideology_matrix.json","schemas/ideology_matrix.schema.json"),
         ("data/genealogy_edges.json","schemas/genealogy_edges.schema.json"),
         ("data/samples/fused_record.example.json","schemas/fused_record.schema.json")]
ok = True
for d, s in pairs:
    data = json.load(open(root/d, encoding="utf-8")); schema = json.load(open(root/s))
    try:
        jsonschema.Draft202012Validator(schema).validate(data); print("ok  ", d)
    except jsonschema.ValidationError as e:
        ok = False; print("FAIL", d, "->", e.message)
# normative firewall: no record may carry a normative field other than the sentinel
for p in (root/"data").rglob("*.json"):
    txt = open(p, encoding="utf-8").read()
    if '"normative_claims"' in txt and '"forbidden_here"' not in txt:
        ok = False; print("FAIL", p, "-> normative_claims must be the sentinel 'forbidden_here'")
sys.exit(0 if ok else 1)
