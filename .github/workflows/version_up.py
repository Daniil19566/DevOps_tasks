import argparse
import re
import datetime

VERSION_FILE = 'version'
VERSION_LOG_FILE = 'version_log'

def read_version():
    try:
        with open(VERSION_FILE, 'r') as f:
            version = f.read().strip()
            if not re.match(r'^\d+\.\d+\.\d+$', version):
                print(f"Version file contains invalid version format: {version}. Resetting to 1.0.0")
                version = '1.0.0'
                write_version(version)

    except FileNotFoundError:
        print("Version file not found. Creating new file with version 1.0.0")
        version = '1.0.0'
        write_version(version)
    return version


def write_version(version):
    with open(VERSION_FILE, 'w') as f:
        f.write(version)


def update_version(version, update_type):
    major, minor, patch = map(int, version.split('.'))

    if update_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif update_type == 'minor':
        minor += 1
        patch = 0
    elif update_type == 'patch':
        patch += 1
    else:
        raise ValueError("Invalid update type. Must be 'major', 'minor', or 'patch'.")

    return f"{major}.{minor}.{patch}"

def log_version_update(old_version, new_version, update_type):
    timestamp = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")[:-3]  #Remove last 3 microsecond digits for cleaner output
    log_entry = f"[{new_version}] < [{old_version}] [{timestamp}] {update_type} update\n"

    with open(VERSION_LOG_FILE, 'a') as f:
        f.write(log_entry)

def main():
    parser = argparse.ArgumentParser(description="Update version according to semantic versioning.")
    parser.add_argument("update_type", choices=['major', 'minor', 'patch'],
                        help="The type of update (major, minor, or patch).")

    args = parser.parse_args()

    old_version = read_version()
    new_version = update_version(old_version, args.update_type)
    write_version(new_version)
    log_version_update(old_version, new_version, args.update_type)

    print(f"Version updated from {old_version} to {new_version}")

if __name__ == "__main__":
    main()
