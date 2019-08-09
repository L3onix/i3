import os
import sys

def exec_install(packages):
    os.system("apt install -y " + packages)

def install_audio():
    packages = "pulseaudio pavucontrol"
    exec_install(packages)

def install_xdg():
    packages = "xdg-user-dirs xdg-utils"
    exec_install(packages)

def install_aparencia():
    packages = "compton feh lxappearance"
    exec_install(packages)

def install_navegador_de_pastas():
    packages = "ranger thunar thunar-archive-plugin thunar-media-tags-plugin thunar-volman gvfs"
    exec_install(packages)

def install_navegador_web():
    packages = "firefox-esr firefox-esr-l10n-pt-br"
    exec_install(packages)

# TODO: executar instalação e configuração de bumblebee
def install_video():
    packages = "xserver-xorg-video-intel xbacklight arandr"
    exec_install(packages)

# TODO: executar configuração de botões
def install_touchpad():
    packages = "xserver-xorg-input-synaptics"
    exec_install(packages)

def install_fonts():
    packages = "ttf-dejavu ttf-nonymous-pro fonts-noto fonts-roboto"
    exec_install(packages)

def install_flatpak():
    packages = "flatpak"
    exec_install(packages)

def install_desempacotadores():
    packages = "unzip unrar tar file-roller"
    exec_install(packages)

def install_core():
    packages = "xorg lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings \
        i3status i3blocks dmenu xfce4-terminal gnome-keyring \
        xserver-xorg-input-all"
    exec_install(packages)
    os.system("systemctl enable lightdm.service")

    install_audio()
    install_navegador_de_pastas()
    install_navegador_web()
    install_video()
    install_aparencia()
    install_fonts()
    install_xdg()
    install_touchpad()
    
def configure():
    os.system('cp ./config ~/.config/i3/')
    os.system('cp -r ./wallpapers ~/.config/i3/')
    os.system('cp ./i3blocks.conf ~/.config/i3/')
    os.system('i3 restart')

def main():
    #executa as configurações do i3
    if str(sys.argv[1]) == 'configure':
        print('Executando configurações')
        configure()
        pass
    #executa a instalação de pacotes "básicos"
    elif str(sys.argv[1]) == 'core':
        print('Executando instalação completa')
        install_core()
        pass

if __name__ == "__main__":
    main()