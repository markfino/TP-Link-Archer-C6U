from models.acl_entry import ACLEntry
from tplinkrouterc6u import (
    TplinkRouterProvider,
    Connection
)
import os
from typing import List
import yaml
import time

from globals import Actions
from tplinkrouterc6u.client_abstract import AbstractRouter
from tplinkrouterc6u.common.dataclass import Status

def execute_action(action: Actions) -> bool:

    print("Establishing router connection...")
    router = TplinkRouterProvider.get_client(os.getenv("ROUTER_URL", ""), os.getenv("ROUTER_PWD", ""))
    result = False
    try:
        print("Authorizing...")
        router.authorize()  # authorizing
 
        if action == Actions.ACL_Get:
            ACL_Get(router)
        elif action == Actions.ACL_Add or action == Actions.ACL_Remove:
            ACL_Set(router, action)
        elif action == Actions.Wifi_Status:
            Wifi_Status(router)
        elif action == Actions.Wifi_Enable or action == Actions.Wifi_Disable:
            Wifi_Set(router, action == Actions.Wifi_Enable)
        elif action == Actions.Wifi_Restart:
            Wifi_Restart(router)
        else:
            raise RuntimeError("Action has not been implemented")
        
    except Exception as err:
        print(f"Unexpected error {err=}, {type(err)=}")

    finally:
        router.logout()  # always logout as TP-Link Web Interface only supports upto 1 user logged

    return result

def _load_ACL_Entries() -> List[ACLEntry]:
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

            return entries

        except yaml.YAMLError as ex:
            print(ex)

    return []

def ACL_Get(router: AbstractRouter):
    
    print("Checking entries")
    entries = _load_ACL_Entries()
    print(entries)

    existing_entries = router.get_acl()
    entry_names = []
    for entry in entries:
        entry_names.append(entry.name)

    for existing_entry in existing_entries:
        print(f"{existing_entry['name']:>30}: {existing_entry['mac']}", "***" if existing_entry["name"] in entry_names else "")

def ACL_Set(router: AbstractRouter, action: Actions):
    print("Checking entries")
    entries = _load_ACL_Entries()
    print(entries)

    existing_entries = router.get_acl()
    entry_names = []
    for entry in entries:
        entry_names.append(entry.name)

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

        if action == Actions.ACL_Add and not found:
            print("Inserting entry...", end="")
            success = router.set_acl(entry.name, entry.mac, 0, True)
            print("done." if success else "failed!")
        elif action == Actions.ACL_Remove and found:
            print("Removing entry")
            success = router.set_acl(entry.name, entry.mac, index, False)
            print("done." if success else "failed!")

def Wifi_Status(router: AbstractRouter):
    status: Status = router.get_status()
    print("Wifi Enable 2G/5G/6G", status.wifi_2g_enable, status.wifi_5g_enable, status.wifi_6g_enable)
    
def Wifi_Set(router: AbstractRouter, enable: bool):
    router.set_wifi(Connection.HOST_2G, enable)
    router.set_wifi(Connection.HOST_5G, enable)

def Wifi_Restart(router: AbstractRouter):
    print("Disabling Wifi")
    Wifi_Set(router, False)
    sleep_time = 10
    print(f"Waiting {sleep_time}s")
    time.sleep(10)
    print(f"Enabling Wifi")
    Wifi_Set(router, True)