from dotenv import load_dotenv
import sys
from typing import List
import argparse

import globals
from models.router_cmds import RouterCmds
from router import execute_action

load_dotenv()

def print_usage():
    usage_doc = (   "Usage: py main.py [-c config_file] \{action\}\n"
                    "\n"
                    "  Actions:"
                )
    print(usage_doc)
    for cmd in cmd_list:
        cmd_str = f"{cmd.long}"
        print(f"    {cmd_str:20}: {cmd.desc}")

cmd_list: List[RouterCmds] = [
    RouterCmds("a", "acl_add", globals.Actions.ACL_Add, "Add mac to Security ACL"),
    RouterCmds("r", "acl_remove", globals.Actions.ACL_Remove, "Remove mac from Security ACL"),
    RouterCmds("l", "acl_get", globals.Actions.ACL_Get, "Get list of macs in Security ACL"),
    RouterCmds("s", "wifi_status", globals.Actions.Wifi_Status, "Get Wifi status"),
    RouterCmds("e", "wifi_enable", globals.Actions.Wifi_Enable, "Enable Wifi"),
    RouterCmds("d", "wifi_disable", globals.Actions.Wifi_Disable, "Disable Wifi"),
    RouterCmds("t", "wifi_restart", globals.Actions.Wifi_Restart, "Restart Wifi")
]

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=[cmd.long for cmd in cmd_list])
    parser.add_argument('-c', '--config', action='store', help='Path to config file (default: ./config.yaml)', default='./config.yaml')
    args = parser.parse_args(sys.argv[1:])
    
    if args.config:
        globals.config_file = args.config
    
    try:
        for cmd in cmd_list:
            if args.action == cmd.long:
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