from huggingface_hub import snapshot_download

path = snapshot_download(
    repo_id="yujieq/MolScribe",
    local_dir="models/molscribe",
    local_dir_use_symlinks=False
)

print("Downloaded to:", path)
