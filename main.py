from dotenv import load_dotenv
import sys
from typing import List

from models.router_cmds import RouterCmds
from router import execute_action
from globals import Actions

load_dotenv()

def print_usage():
    usage_doc = (   "Usage: py main.py [OPTION]\n"
                    "\n"
                    "  Options:"
                )
    print(usage_doc)
    for cmd in cmd_list:
        cmd_str = f"{cmd.long} ({cmd.short})"
        print(f"    {cmd_str:20}: {cmd.desc}")

cmd_list: List[RouterCmds] = [
    RouterCmds("a", "acl_add", Actions.ACL_Add, "Add mac to Security ACL"),
    RouterCmds("r", "acl_remove", Actions.ACL_Remove, "Remove mac from Security ACL"),
    RouterCmds("l", "acl_get", Actions.ACL_Get, "Get list of macs in Security ACL"),
    RouterCmds("s", "wifi_status", Actions.Wifi_Status, "Get Wifi status"),
    RouterCmds("e", "wifi_enable", Actions.Wifi_Enable, "Enable Wifi"),
    RouterCmds("d", "wifi_disable", Actions.Wifi_Disable, "Disable Wifi"),
    RouterCmds("t", "wifi_restart", Actions.Wifi_Restart, "Restart Wifi")
]

def main():
    args = sys.argv[1:]
    
    try:
        for cmd in cmd_list:
            if args[0] == cmd.short or args[0] == cmd.long:
                print(f"Executing action: {cmd.desc}")
                execute_action(cmd.action)
                print("Completed successfully.")
                return
            
        raise RuntimeError("Action not found.")
    
    except Exception as err:
        print("Error:", err)
        print_usage()

if __name__ == '__main__':
    main()