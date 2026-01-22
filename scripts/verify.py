#!/usr/bin/env python3
import sys
import re
import os

def parse_plan(plan_path="implementation_plan.md"):
    if not os.path.exists(plan_path):
        print(f"❌ Error: {plan_path} not found.")
        return None
    
    with open(plan_path, 'r') as f:
        content = f.read()
        
    # Extract file paths marked as [NEW] or [MODIFY]
    files = re.findall(r'\[(NEW|MODIFY)\]\s+([^\s]+)', content)
    return files

def check_tests_existence(files):
    missing_tests = []
    for mode, filepath in files:
        # Ignore non-code files
        if not filepath.endswith(('.py', '.js', '.ts', '.go', '.java')):
            continue
            
        # Basic heuristic: look for 'test' in the path or a corresponding test file
        # e.g. src/auth.py -> tests/test_auth.py
        
        filename = os.path.basename(filepath)
        name_root = os.path.splitext(filename)[0]
        
        # Check 1: Is it a test file itself?
        if 'test' in filename.lower() or 'spec' in filename.lower():
            continue
            
        # Check 2: Does a corresponding test file exist?
        # We search for *test_{name_root}* or *{name_root}_test* or *{name_root}.test*
        
        found_test = False
        # Walk to find tests (expensive but accurate)
        for root, dirs, filenames in os.walk("."):
            for f in filenames:
                if (f"test_{name_root}" in f) or (f"{name_root}_test" in f) or (f"{name_root}.test" in f):
                    found_test = True
                    break
            if found_test: break
            
        if not found_test:
            missing_tests.append(filepath)
            
    return missing_tests

def main():
    print("🔍 Superpower TDD Enforcer")
    print("==========================")
    
    files = parse_plan()
    if not files:
        print("No files found in plan or plan missing.")
        sys.exit(1)
        
    print(f"Checking {len(files)} files from plan...")
    
    missing = check_tests_existence(files)
    
    if missing:
        print("\n❌ VIOLATION: The following files strictly require tests before implementation:")
        for f in missing:
            print(f"  - {f}")
        print("\nRule: You MUST create a test file (e.g., tests/test_feature.py) covering these files.")
        print("Action: Create the test file first.")
        sys.exit(1)
    else:
        print("\n✅ TDD Check Passed: All planned files have corresponding tests.")
        sys.exit(0)

if __name__ == "__main__":
    main()
