import hashlib,json,re
from pathlib import Path
repo=Path(__file__).resolve().parents[1]
release=json.loads((repo/"deploy/platform-release.json").read_text())
assert release["package"]=="@subcult/archive-viewer"
assert release["contract_version"]==release["configuration_version"]==1
assert "1" in release["api_versions"] and "video" in release["media"]
assert re.fullmatch(r"[0-9a-f]{40}",release["source_revision"])
assert re.fullmatch(r"git\.subcult\.tv/subculture-collective/archive-engine@sha256:[0-9a-f]{64}",release["engine_digest"])
assert (repo/"deploy/archive-engine.env").read_text()=="ARCHIVE_ENGINE_IMAGE="+release["engine_digest"]+"\n"
package=json.loads((repo/"web/package.json").read_text())
viewer=json.loads((repo/"deploy/viewer-release.json").read_text())
assert package["dependencies"][release["package"]]==viewer["version"]
assert viewer["package"]==release["package"]
assert not (repo/"web/src/engine").exists(),"Legacy adapter is still present"
print("Shared package and immutable engine pins verified:",release["version"],release["source_revision"])
tools=json.loads((repo/"docs/engine-tools.json").read_text())
for name,digest in tools["files"].items():
 assert ".." not in Path(name).parts and not Path(name).is_absolute()
 assert hashlib.sha256((repo/name).read_bytes()).hexdigest()==digest, f"Generated engine tool drift: {name}"
provenance=json.loads((repo/"docs/asset-provenance.json").read_text())
for asset in provenance["assets"]:
 assert hashlib.sha256((repo/asset["shipped_path"]).read_bytes()).hexdigest()==asset["sha256"]
print("Engine deployment tools and supplied assets verified")
