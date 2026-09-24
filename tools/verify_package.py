from __future__ import annotations
import hashlib, json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((ROOT/"REPOSITORY_MANIFEST.json").read_text(encoding="utf-8"))
errors=[]
for row in manifest["files"]:
 p=ROOT/row["path"]
 if not p.is_file(): errors.append("missing:"+row["path"]); continue
 if sha(p)!=row["sha256"]: errors.append("hash:"+row["path"])
source=json.loads((ROOT/"SOURCE_RELEASE.json").read_text(encoding="utf-8"))
pkg=json.loads((ROOT/"package.json").read_text(encoding="utf-8"))
if pkg.get("package_sha256")!=source.get("package_sha256"): errors.append("package_binding")
if pkg.get("developer_configures_not_redesigns") is not True: errors.append("configuration_boundary")
if pkg.get("custody_is_not_authority") is not True: errors.append("authority_boundary")
print(json.dumps({"valid":not errors,"repository":source.get("repository"),"domain":source.get("domain"),"files":len(manifest["files"]),"errors":errors},indent=2,sort_keys=True))
sys.exit(0 if not errors else 2)
