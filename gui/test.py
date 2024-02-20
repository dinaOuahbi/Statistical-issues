import subprocess
import sys
import os

env_name = "mon_env"
subprocess.check_call([sys.executable, '-m', 'venv', env_name])
if os.name == 'nt':
     activate_cmd = os.path.join(env_name, 'Scripts', 'activate')
else:
    activate_cmd = os.path.join(env_name, 'bin', 'activate')

if os.name == 'nt':
    subprocess.check_call(activate_cmd, shell=True)
else:
    subprocess.check_call(f"source {activate_cmd}", shell=True)
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'paramiko', 'scp','Pillow'])
print("Environnement virtuel créé, activé et packages installés avec succès.")

import tkinter as tk
import paramiko, os
from scp import SCPClient
from PIL import Image, ImageTk

def send_files(local_path, remote_path, local_to_serveur=False):
    '''
        Send directories with files inside from local to the server or from the server to the local
        If local_to_serveur=False

    '''
    try:
        # Création d'une instance de client SSH
        ssh_client = paramiko.SSHClient()
        # Accepter automatiquement les clés SSH du serveur
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Connexion au serveur
        ssh_client.connect(hostname, port, username, password)
        print("Connexion réussie.")
        # Création d'une instance SCPClient
        with SCPClient(ssh_client.get_transport()) as scp:
            # Chemin local du fichier à envoyer
            print(os.getcwd())
            # Chemin distant où le fichier sera placé sur le serveur

            # Transfert du fichier vers le serveur
            if local_to_serveur:
                scp.put(local_path, recursive=True,remote_path=remote_path)
            else:
                scp.get(remote_path, recursive=True, local_path=local_path)

            res=tk.Label(fenetre, text=f"Fichier envoyé avec succès depuis {hostname}:{remote_path}")
            res.pack()

    except paramiko.AuthenticationException:
        print("Échec de l'authentification. Vérifiez votre nom d'utilisateur et votre mot de passe.")
    except paramiko.SSHException as ssh_ex:
        print("Erreur SSH :", ssh_ex)
    except Exception as ex:
        print("Une erreur s'est produite :", ex)
    finally:
        # Fermeture de la connexion SSH
        ssh_client.close()

def sendfiles_wrapper():
    local_path = f'./'
    remote_path = "/shared/projects/cnn_pancreas/CNN_pancres_project/slide_annot"
    send_files(local_path, remote_path)


fenetre = tk.Tk()
hostname = 'core.cluster.france-bioinformatique.fr'
port = 22
username = 'dinaton'
password = '###'
size=500
bouton = tk.Button(fenetre, fg="#fcddb3",bg="#081c37",text="send files", command=sendfiles_wrapper)
bouton.pack(expand=True, padx=10, pady=10)
image = Image.open("histo.JPG")
image = image.resize((300, 300))
photo = ImageTk.PhotoImage(image)
frame_image = tk.Frame(fenetre)
frame_image.pack(expand=True)
label_image = tk.Label(fenetre, image=photo)
label_image.pack(expand=True, padx=10, pady=10)
fenetre.geometry(f"{size}x{size}")
fenetre.mainloop()
