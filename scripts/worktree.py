#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_cmd(cmd, cwd=None, exit_on_fail=True):
    try:
        result = subprocess.run(cmd, shell=True, check=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {cmd}")
        print(f"Error: {e.stderr}")
        if exit_on_fail:
            sys.exit(1)
        return None

def check_ignore(path):
    """Check if path is ignored by git."""
    cmd = f"git check-ignore -q {path}"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def setup_project(cwd):
    """Detect and run project setup."""
    print("📦 Detecting project type and installing dependencies...")
    
    if os.path.exists(os.path.join(cwd, 'package.json')):
        print("  - Node.js detected. Running npm install...")
        run_cmd("npm install", cwd=cwd, exit_on_fail=False)
        
    elif os.path.exists(os.path.join(cwd, 'Cargo.toml')):
        print("  - Rust detected. Running cargo build...")
        run_cmd("cargo build", cwd=cwd, exit_on_fail=False)
        
    elif os.path.exists(os.path.join(cwd, 'requirements.txt')):
        print("  - Python (requirements) detected. Running pip install...")
        run_cmd("pip install -r requirements.txt", cwd=cwd, exit_on_fail=False)
        
    elif os.path.exists(os.path.join(cwd, 'pyproject.toml')):
        print("  - Python (poetry) detected. Running poetry install...")
        run_cmd("poetry install", cwd=cwd, exit_on_fail=False)
        
    elif os.path.exists(os.path.join(cwd, 'go.mod')):
        print("  - Go detected. Running go mod download...")
        run_cmd("go mod download", cwd=cwd, exit_on_fail=False)
        
    else:
        print("  - No specific project type detected. Skipping install.")

def verify_baseline(cwd):
    """Run baseline tests."""
    print("🧪 Verifying clean baseline (running tests)...")
    
    cmd = None
    if os.path.exists(os.path.join(cwd, 'package.json')):
        cmd = "npm test"
    elif os.path.exists(os.path.join(cwd, 'Cargo.toml')):
        cmd = "cargo test"
    elif os.path.exists(os.path.join(cwd, 'pytest.ini')) or os.path.exists(os.path.join(cwd, 'conftest.py')): # Loose heuristic
        cmd = "pytest"
    
    if cmd:
        print(f"  - Running: {cmd}")
        try:
            run_cmd(cmd, cwd=cwd)
            print("✅ Baseline tests passed.")
        except SystemExit:
            print("⚠️ Baseline tests FAILED. Review output above.")
            # We don't exit here, we just warn, as per skill logic (ask user)
    else:
        print("  - No test command detected. Skipping baseline verification.")

def main():
    if len(sys.argv) < 3:
        print("Usage: worktree.py <branch_name> <base_dir_preference>")
        sys.exit(1)
        
    branch_name = sys.argv[1]
    pref_dir = sys.argv[2] # '.worktrees' or 'worktrees' or 'auto'
    
    # 1. Determine Worktree Directory
    worktree_parent = ".worktrees"
    if pref_dir in [".worktrees", "worktrees"]:
        worktree_parent = pref_dir
    elif os.path.exists(".worktrees"):
        worktree_parent = ".worktrees"
    elif os.path.exists("worktrees"):
        worktree_parent = "worktrees"
    
    print(f"📂 Target Parent Directory: {worktree_parent}")
    
    # 2. Safety Check (Git Ignore)
    if not check_ignore(worktree_parent):
        print(f"❌ VIOLATION: {worktree_parent} is NOT ignored by git.")
        print("Action: Add it to .gitignore first.")
        # Attempt to fix?
        with open(".gitignore", "a") as f:
            f.write(f"\n{worktree_parent}/\n")
        print(f"✅ Auto-fixed: Added {worktree_parent}/ to .gitignore")
        
    # 3. Create Worktree
    target_path = os.path.join(worktree_parent, branch_name)
    if os.path.exists(target_path):
        print(f"⚠️ Worktree already exists at {target_path}")
    else:
        print(f"🔨 Creating worktree for branch '{branch_name}'...")
        run_cmd(f"git worktree add {target_path} -b {branch_name}")
        
    # 4. Setup & Verify
    setup_project(target_path)
    verify_baseline(target_path)
    
    print(f"\n✅ Worktree Ready: {os.path.abspath(target_path)}")
    print(f"👉 To switch: cd {worktree_parent}/{branch_name}")

if __name__ == "__main__":
    main()
