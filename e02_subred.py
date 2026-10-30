import ipaddress

entrada = input("Red en formato CIDR (ej. 192.168.10.0/26): ")
try:
    red = ipaddress.ip_network(entrada, strict=False)
except ValueError:
    print("Direccion no válida ")
    raise SystemExit(1)

print("Red:" , red.network_address)
print("Máscara:", red.netmask)
print("Prefijo: /"+ str(red.prefixlen))
print("Broadcast:", red.broadcast_address)

if red.num_addresses < 4:
    print("Sin hosts útiles")
else:
    print("Hosts útiles:", red.num_addresses - 2)
    print("Primer host:", red.network_address + 1)
    print("Último host:", red.broadcast_address - 1)

#Completar: si la red tiene menos de 4 direcciones mostrar "Sin hosts útiles";
#Si no, mostrar hosts útiles (num_addresses - 2), primer host (red + 1) y
#último host (broadcast - 1)
pass

