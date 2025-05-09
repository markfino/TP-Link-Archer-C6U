from macaddress import EUI48
from ipaddress import IPv4Address
from dataclasses import dataclass
from datetime import datetime
from tplinkrouterc6u.common.package_enum import Connection
from typing import Optional

@dataclass
class Firmware:
    def __init__(self, hardware: str, model: str, firmware: str) -> None:
        self.hardware_version = hardware
        self.model = model
        self.firmware_version = firmware


@dataclass
class Device:
    def __init__(self, type: Connection, macaddr: EUI48, ipaddr: IPv4Address, hostname: str) -> None:
        self.type = type
        self._macaddr = macaddr
        self._ipaddr = ipaddr
        self.hostname = hostname
        self.packets_sent: Optional[int] = None
        self.packets_received: Optional[int] = None
        self.down_speed: Optional[int] = None
        self.up_speed: Optional[int] = None
        self.signal: Optional[int] = None
        self.active: bool = True

    @property
    def macaddr(self):
        return str(self._macaddr)

    @property
    def macaddress(self):
        return self._macaddr

    @property
    def ipaddr(self):
        return str(self._ipaddr)

    @property
    def ipaddress(self):
        return self._ipaddr


@dataclass
class Status:
    def __init__(self) -> None:
        self._wan_macaddr: Optional[EUI48] = None
        self._lan_macaddr: EUI48
        self._wan_ipv4_addr: Optional[IPv4Address] = None
        self._lan_ipv4_addr: Optional[IPv4Address] = None
        self._wan_ipv4_gateway: Optional[IPv4Address] = None
        self.wired_total: int = 0
        self.wifi_clients_total: int = 0
        self.guest_clients_total: int = 0
        self.iot_clients_total: Optional[int] = None
        self.clients_total: int = 0
        self.guest_2g_enable: bool
        self.guest_5g_enable: Optional[bool] = None
        self.guest_6g_enable: Optional[bool] = None
        self.iot_2g_enable: Optional[bool] = None
        self.iot_5g_enable: Optional[bool] = None
        self.iot_6g_enable: Optional[bool] = None
        self.wifi_2g_enable: bool
        self.wifi_5g_enable: Optional[bool] = None
        self.wifi_6g_enable: Optional[bool] = None
        self.wan_ipv4_uptime: Optional[int] = None
        self.mem_usage: Optional[float] = None
        self.cpu_usage: Optional[float] = None
        self.conn_type: Optional[str] = None
        self.devices: list[Device] = []

    @property
    def wan_macaddr(self) -> Optional[str]:
        return str(self._wan_macaddr) if self._wan_macaddr else None

    @property
    def wan_macaddress(self) -> Optional[EUI48]:
        return self._wan_macaddr

    @property
    def lan_macaddr(self):
        return str(self._lan_macaddr)

    @property
    def lan_macaddress(self):
        return self._lan_macaddr

    @property
    def wan_ipv4_addr(self) -> Optional[str]:
        return str(self._wan_ipv4_addr) if self._wan_ipv4_addr else None

    @property
    def wan_ipv4_address(self) -> Optional[IPv4Address]:
        return self._wan_ipv4_addr

    @property
    def lan_ipv4_addr(self) -> Optional[str]:
        return str(self._lan_ipv4_addr) if self._lan_ipv4_addr else None

    @property
    def lan_ipv4_address(self) -> Optional[IPv4Address]:
        return self._lan_ipv4_addr

    @property
    def wan_ipv4_gateway(self) -> Optional[str]:
        return str(self._wan_ipv4_gateway) if self._wan_ipv4_gateway else None

    @property
    def wan_ipv4_gateway_address(self) -> Optional[IPv4Address]:
        return self._wan_ipv4_gateway


@dataclass
class IPv4Reservation:
    def __init__(self, macaddr: EUI48, ipaddr: IPv4Address, hostname: str, enabled: bool) -> None:
        self._macaddr = macaddr
        self._ipaddr = ipaddr
        self.hostname = hostname
        self.enabled = enabled

    @property
    def macaddr(self):
        return str(self._macaddr)

    @property
    def macaddress(self):
        return self._macaddr

    @property
    def ipaddr(self):
        return str(self._ipaddr)

    @property
    def ipaddress(self):
        return self._ipaddr


@dataclass
class IPv4DHCPLease:
    def __init__(self, macaddr: EUI48, ipaddr: IPv4Address, hostname: str, lease_time: str) -> None:
        self._macaddr = macaddr
        self._ipaddr = ipaddr
        self.hostname = hostname
        self.lease_time = lease_time

    @property
    def macaddr(self):
        return str(self._macaddr)

    @property
    def macaddress(self):
        return self._macaddr

    @property
    def ipaddr(self):
        return str(self._ipaddr)

    @property
    def ipaddress(self):
        return self._ipaddr


@dataclass
class IPv4Status:
    def __init__(self) -> None:
        self._wan_macaddr: EUI48
        self._wan_ipv4_ipaddr: Optional[IPv4Address] = None
        self._wan_ipv4_gateway: Optional[IPv4Address] = None
        self._wan_ipv4_conntype: str
        self._wan_ipv4_netmask: Optional[IPv4Address] = None
        self._wan_ipv4_pridns: IPv4Address
        self._wan_ipv4_snddns: IPv4Address
        self._lan_macaddr: EUI48
        self._lan_ipv4_ipaddr: IPv4Address
        self.lan_ipv4_dhcp_enable: bool
        self._lan_ipv4_netmask: IPv4Address
        self.remote: Optional[bool] = None

    @property
    def wan_macaddr(self):
        return str(self._wan_macaddr)

    @property
    def wan_macaddress(self):
        return self._wan_macaddr

    @property
    def wan_ipv4_ipaddr(self):
        return str(self._wan_ipv4_ipaddr) if self._wan_ipv4_ipaddr else None

    @property
    def wan_ipv4_conntype(self):
        return self._wan_ipv4_conntype if hasattr(self, '_wan_ipv4_conntype') else ''

    @property
    def wan_ipv4_ipaddress(self):
        return self._wan_ipv4_ipaddr

    @property
    def wan_ipv4_gateway(self):
        return str(self._wan_ipv4_gateway) if self._wan_ipv4_gateway else None

    @property
    def wan_ipv4_gateway_address(self):
        return self._wan_ipv4_gateway

    @property
    def wan_ipv4_netmask(self):
        return str(self._wan_ipv4_netmask) if self._wan_ipv4_netmask else None

    @property
    def wan_ipv4_netmask_address(self):
        return self._wan_ipv4_netmask

    @property
    def wan_ipv4_pridns(self):
        return str(self._wan_ipv4_pridns)

    @property
    def wan_ipv4_pridns_address(self):
        return self._wan_ipv4_pridns

    @property
    def wan_ipv4_snddns(self):
        return str(self._wan_ipv4_snddns)

    @property
    def wan_ipv4_snddns_address(self):
        return self._wan_ipv4_snddns

    @property
    def lan_macaddr(self):
        return str(self._lan_macaddr)

    @property
    def lan_macaddress(self):
        return self._lan_macaddr

    @property
    def lan_ipv4_ipaddr(self):
        return str(self._lan_ipv4_ipaddr)

    @property
    def lan_ipv4_ipaddress(self):
        return self._lan_ipv4_ipaddr

    @property
    def lan_ipv4_netmask(self):
        return str(self._lan_ipv4_netmask)

    @property
    def lan_ipv4_netmask_address(self):
        return self._lan_ipv4_netmask


@dataclass
class SMS:
    def __init__(self, index: int, sender: str, content: str, received_at: datetime, unread: bool) -> None:
        self.id = index
        self.sender = sender
        self.content = content
        self.received_at = received_at
        self.unread = unread


@dataclass
class LTEStatus:
    def __init__(self) -> None:
        self.enable: int
        self.connect_status: int
        self.network_type: int
        self.sim_status: int
        self.total_statistics: int
        self.cur_rx_speed: int
        self.cur_tx_speed: int
        self.sms_unread_count: int
        self.sig_level: int
        self.rsrp: int
        self.rsrq: int
        self.snr: int
        self.isp_name: str


@dataclass
class VPNStatus:
    def __init__(self) -> None:
        self.openvpn_enable: bool
        self.pptpvpn_enable: bool
        self.openvpn_clients_total: int = 0
        self.pptpvpn_clients_total: int = 0
