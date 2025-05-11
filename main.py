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
                    "  --list, -l      List ACL mac addresses\n"
                )
    print(usage_doc)


def main():
    args = sys.argv[1:]

    action = ""
    if '--enable' in args or '-e' in args:
        action = "enable"
    elif '--disable' in args or '-d' in args:
        action = "disable"
    elif '--list' in args or '-l' in args:
        action = "list"
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

            print(f"Syncing ACL mac addresses for action: {action}")
            sync_acl_access(entries, action)
            print("Syncing completed successfully.")
            
        except yaml.YAMLError as ex:
            print(ex)


if __name__ == '__main__':
    main()