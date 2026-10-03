import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]/"web/src/engine"
manifest=json.loads((root/"manifest.json").read_text())
assert manifest["api_version"]=="1"
assert len(manifest["revision"])==40
for name,digest in manifest["files"].items():
 assert Path(name).name==name
 assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest, f"Generated engine adapter drift: {name}"
print("Pinned engine adapter verified:",manifest["revision"])

repo=root.parents[2]
tools=json.loads((repo/"docs/engine-tools.json").read_text())
for name,digest in tools["files"].items():
 assert ".." not in Path(name).parts and not Path(name).is_absolute()
 assert hashlib.sha256((repo/name).read_bytes()).hexdigest()==digest, f"Generated engine tool drift: {name}"
provenance=json.loads((repo/"docs/asset-provenance.json").read_text())
for asset in provenance["assets"]:
 assert hashlib.sha256((repo/asset["shipped_path"]).read_bytes()).hexdigest()==asset["sha256"]
print("Engine deployment tools and supplied assets verified")
