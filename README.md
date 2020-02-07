SW requirements:
1. Virtualbox 6.0.x: https://www.virtualbox.org/wiki/Download_Old_Builds_6_0
2. Vagrant: https://www.vagrantup.com/downloads.html
3. Git bash (if you're using Windows): https://gitforwindows.org/
4. Some text editor, VSCode (https://code.visualstudio.com/) , notepad++ (https://notepad-plus-plus.org/), something else than Notepad

Todo:

- Install first Virtualbox 6.0.x
- Install vagrant after Virtualbox
- And then run this command:

	    vagrant up

Based on Ubuntu 18.04 Bionic server with docker-ce, docker-compose and minikube preinstalled

Starting environment:

    vagrant up

Stopping environment:

    vagrant halt

Destroying environment:

    vagrant destroy -f

Destroying and rebuilding environment:

    vagrant destroy -f && vagrant up

