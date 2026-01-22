#!/usr/bin/env python3
import sys
import os

TEMPLATE = """# Implementation Plan - {goal}

## User Review Required
> [!IMPORTANT]
> Critical items requiring user attention.

## Proposed Changes
### Component: {component}
#### [NEW] path/to/new_file.ext
#### [MODIFY] path/to/existing.ext

## Verification Plan
### Automated Tests
- [ ] `pytest tests/test_feature.py`

### Manual Verification
- [ ] Step 1...
"""

def main():
    if len(sys.argv) < 2:
        print("Usage: python plan.py 'Goal Description'")
        print("Example: python plan.py 'Add Login Feature'")
        sys.exit(1)

    goal = sys.argv[1]
    component = "Core" # Default
    
    content = TEMPLATE.format(goal=goal, component=component)
    
    filename = "implementation_plan.md"
    if os.path.exists(filename):
        print(f"Warning: {filename} already exists. Appending timestamp to new one.")
        import time
        filename = f"implementation_plan_{int(time.time())}.md"

    with open(filename, "w") as f:
        f.write(content)
    
    print(f"✅ Created {filename}")
    print("Action: Fill this file with concrete steps now.")

if __name__ == "__main__":
    main()
