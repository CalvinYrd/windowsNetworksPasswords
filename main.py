from subprocess import run as subprocess_run
from os import name as os_name, system
from colorama import Fore as color

# permet de récupérer le résultat d'une commande
def cmd(cmd):
	return subprocess_run(
		cmd, shell = True, capture_output = True, text = True, encoding="cp850"
	).stdout

# effacement de l'écran
if (os_name == "nt"): system("cls")
else: system("clear")

# si le système est windows
if (os_name == "nt"):
	# récupération des réseaux wifi
	networks = cmd("netsh wlan show profiles")
	networks = networks.split("-----")[-1]
	networks = networks.split("\n")[1:]

	# affichage des infos de chaque wifi
	for network in networks:
		# on récupère uniquement le nom seul du wifi
		network = network.split(":", 1)[-1].strip()

		# si le nom est vide (""), on ignore
		if (network == ""): continue

		# récupération des informations du réseau
		infos = cmd('netsh wlan show profiles name="' + network + '" key="clear"')
		infos = infos.replace("Authentification", "", 1)
		infos = infos.split("\n")

		# affichage des informations prioritaires
		for info in infos:
			info = info.split(":", 1)

			if (info[0].lower().strip() in ("nom du ssid", "contenu de la clé", "authentification")):
				print(info[0].strip() + " : " + color.GREEN + info[1] + color.RESET)

		print("\n" + color.LIGHTBLACK_EX + ("=" * 50) + color.RESET + "\n")

# sinon, on indique que le programme n'est pas compatible
else: print("Désolé, votre OS n'est pas compatible.")
