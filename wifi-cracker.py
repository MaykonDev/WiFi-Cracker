try:
    import subprocess
except ImportError as e:
    print(e)

def wifi_cracker():
    print("""
------------------->[ WIFI-CRACKER ]<-------------------

            [1] - senhas de wifi salvas
            [2] - quebrar senha de wifi
            [3] - sair
    """)

    escolha = input("Sua escolha: ")

    if escolha == "1":
        print("""
        --------------[senhas de wifi salvas]--------------

                 [1] - mostrar todos os wifi salvos
              [2] - selecionar wifi para mostrar senha
                           [3] - voltar
                            [0] - sair
        """)
        nova_escolha = input("Sua escolha: ")
        if nova_escolha == "1":
            senhas = subprocess.check_output(["netsh", "wlan", "show", "profiles"], encoding='cp860')
            print(senhas)

        elif nova_escolha == "2":
            wifi = input("Nome do wifi: ")
            if wifi == "":
                print("favor digitar a porra de um wifi caralho, eu não sou magico fdp")
            else:
                password = senhas = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi, "key", "=", "clear"], encoding='cp860')
                for host in password.split("\n"):
                    if "Todos os Perfis de Usuários" in host:
                        pos = host.find(":")
                        senha = host[pos+2:]
                        print(senha)

        elif nova_escolha == "3":
            wifi_cracker()

        elif nova_escolha == "0":
            print("saindo...")

    elif escolha == "2":
        print("em breve! desculpe.")

    elif escolha == "3":
        print("saindo...")

wifi_cracker()