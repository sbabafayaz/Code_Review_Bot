from git import Repo

def get_commit_diff(repo_path: str, pr_id: int):
    # 🔴 You need to clone the repo and provide correct path
    repo = Repo(repo_path)
    return repo.git.diff(f"origin/main...origin/pr/{pr_id}")

