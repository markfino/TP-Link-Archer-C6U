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

router = TplinkRouterProvider.get_client('<routeraddress>', '<routerpassword>')

try:
    router.authorize()  # authorizing

    print(router.__class__)
    # Get firmware info - returns Firmware
    firmware = router.get_firmware()
    print(firmware.firmware_version)

    # Get status info - returns Status
    status = router.get_status()
    print(status)

    # Get Address reservations, sort by ipaddr
    reservations = router.get_ipv4_reservations()
    reservations.sort(key=lambda a: a.ipaddr)
    for res in reservations:
        print(f"{res.macaddr} {res.ipaddr:16s} {res.hostname:36} {'Permanent':12}")

    # # Get DHCP leases, sort by ipaddr
    leases = router.get_ipv4_dhcp_leases()
    leases.sort(key=lambda a: a.ipaddr)
    for lease in leases:
        print(f"{lease.macaddr} {lease.ipaddr:16s} {lease.hostname:36} {lease.lease_time:12}")
finally:
    router.logout()  # always logout as TP-Link Web Interface only supports upto 1 user logged