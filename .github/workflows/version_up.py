import sys
from datetime import datetime

def read_version():
    with open('version', 'r') as f:
        return f.read().strip()

def write_version(version):
    with open('version', 'w') as f:
        f.write(version)

def append_log(old_version, new_version, update_type):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('version_log', 'a') as f:
        f.write(f"[{new_version}] <- [{old_version}] {update_type} up | {timestamp}\n")

def bump_version(version, update_type):
    major, minor, patch = map(int, version.split('.'))
    if update_type == 'minor':
        minor += 1
        patch = 0
    elif update_type == 'patch':
        patch += 1
    return f"{major}.{minor}.{patch}"

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ('minor', 'patch'):
        print("Usage: version_up.py [minor|patch]", file=sys.stderr)
        sys.exit(1)

    update_type = sys.argv[1]
    old_version = read_version()
    new_version = bump_version(old_version, update_type)

    write_version(new_version)
    append_log(old_version, new_version, update_type)

    # Только новая версия — для GitHub Actions
    print(new_version)

if __name__ == '__main__':
    main()
