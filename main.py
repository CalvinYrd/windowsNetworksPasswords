import os

[os.system('cls') if os.name == "nt" else os.system('clear')]

if os.name == 'nt':
	if os.popen('netsh wlan show profiles').read().split('\n')[9:-2]:
		for network in os.popen('netsh wlan show profiles').read().split('\n')[9:-2]:
			network = network.split(': ')[-1]
			
			try:
				pwd = os.popen(f'netsh wlan show profiles name="{network}" key=clear').read().split('Contenu de la')[-1].split('    : ')[1].split('\n')[0]

				print(f"--------------------------------------------------------------------------------------\nNom          : {network}\nMot de passe : {pwd}")

			except IndexError:
				pass

		print("--------------------------------------------------------------------------------------\n\n\n\n")

	else:
		print("Aucun réseau(x) wifi trouvé(s), attention : il est possible qu'aucune carte wifi soit connectée à l'appareil.")

else:
	print("Désolé, votre système n'est pas supporté par ce programme.")
