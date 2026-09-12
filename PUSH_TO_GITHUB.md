# Pushing this to GitHub

The repository is already a git repo with its full history — two commits, nothing
to prepare. It only needs a remote and a push.

```bash
cd legal-eval
git remote add origin https://github.com/Ann-reva/legal-eval.git
git branch -M main
git push -u origin main
```

Git will ask for credentials:

- **Username:** `Ann-reva`
- **Password:** paste the fine-grained token (not the account password)

The token needs **Contents: Read and write** and must list `legal-eval` under its
repository access.

If `git` is missing on macOS, run `xcode-select --install` first.

After the push succeeds, delete the token at
<https://github.com/settings/personal-access-tokens>.
