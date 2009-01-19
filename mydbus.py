import dbus


session_bus = dbus.SessionBus()

system_bus = dbus.SystemBus()

eth0 = system_bus.get_object("org.freedesktop.NetworkManager",
	"/org/freedesktop/Networkmanager/Devices/eth0")

props = eth0.get_properties(dbus_interface="org.freedesktop.NetworkManager.Devices")

