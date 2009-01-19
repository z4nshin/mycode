
string = "0123456789:;<=>?@abcdefghijklmnopqrstuvwxyz"
decrypt = "6e3eff:l"
pos=0
for a in decrypt:
	index = string.index(a)
	index -= pos
	print string[index]
	pos = pos + 1


