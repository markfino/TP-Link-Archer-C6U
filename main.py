from dotenv import load_dotenv
import yaml
import sys
from typing import List

from models.acl_entry import ACLEntry
from router import sync_acl_access

load_dotenv()

def print_usage():
    usage_doc = (   "Usage: py main.py [OPTION]\n"
                    "\n"
                    "  Options:\n"
                    "  --enabe, -e     Enable ACL mac addresses\n"
                    "  --disable, -d   Disable ACL mac addresses\n"
                )
    print(usage_doc)


def main():
    args = sys.argv[1:]

    enable: bool
    if '--enable' in args or '-e' in args:
        enable = True
    elif '--disable' in args or '-d' in args:
        enable = False
    else:
        print_usage()
        exit()

    with open("./config.yaml") as stream:
        try:

            config = yaml.safe_load(stream)

            # load typed ACL entries
            acl_entries = config['acl_entries']
            entries: List[ACLEntry] = []
            for acl_entry in acl_entries:
                entries.append(
                    ACLEntry(acl_entry['name'], acl_entry['mac'])
                )

            action = "enabled" if enable else "disabled"
            print(f"Syncing ACL mac addresses to be {action}...")
            sync_acl_access(entries, enable)
            print("Syncing completed successfully.")
            
        except yaml.YAMLError as ex:
            print(ex)


if __name__ == '__main__':
    main()