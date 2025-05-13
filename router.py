from models.acl_entry import ACLEntry
from tplinkrouterc6u import (
    TplinkRouterProvider,
    TplinkRouter,
    TplinkC1200Router,
    TplinkC5400XRouter,
    TPLinkMRClient,
    TPLinkVRClient,
    TPLinkEXClient,
    TPLinkXDRClient,
    TPLinkDecoClient,
    TplinkC80Router,
    TplinkWDRRouter,
    Connection
)
from logging import Logger
import os
from pathlib import Path
from typing import List

def sync_acl_access(entries: List[ACLEntry], action: str) -> bool:

    print("Establishing router connection...")
    router = TplinkRouterProvider.get_client(os.getenv("ROUTER_URL", ""), os.getenv("ROUTER_PWD", ""))
    result = False
    try:
        print("Authorizing...")
        router.authorize()  # authorizing

        print("Checking entries")
        print(entries)

        existing_entries = router.get_acl()

        if action == "list" :
            entry_names = []
            for entry in entries:
                entry_names.append(entry.name)

            for existing_entry in existing_entries:
                print(f"{existing_entry['name']:>30}: {existing_entry['mac']}", "***" if existing_entry["name"] in entry_names else "")
        else: 
            index = 0
            for entry in entries:
                print("Processing entry:", entry.name)
                found = False
                index = 0
                for existing_entry in existing_entries:
                    if entry.name == existing_entry["name"]:
                        print(f"Found existing entry:", existing_entry)
                        found = True
                        break
                    index += 1

                if action == "enable" and not found:
                    print("Inserting entry...", end="")
                    success = router.set_acl(entry.name, entry.mac, 0, True)
                    print("done." if success else "failed!")
                elif action == "disable" and found:
                    print("Removing entry")
                    success = router.set_acl(entry.name, entry.mac, index, False)
                    print("done." if success else "failed!")

    finally:
        router.logout()  # always logout as TP-Link Web Interface only supports upto 1 user logged

    return result