import os
import sys

def exec_install(packages):
    os.system("pacman -Sy --noconfirm " + packages)

def install_audio():
    packages = "pulseaudio pulseaudio-alsa pavucontrol"
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
    packages = "firefox-developer-edition firefox-developer-edition-i18n-pt-br"
    exec_install(packages)

def install_kernel_lts():
    packages = "linux-lts"
    exec_install(packages)
    os.system("grub-mkconfig -o /boot/grub/grub.cfg")

# TODO: executar instalação e configuração de bumblebee
def install_video():
    packages = "xf86-video-intel xorg-xbacklight arandr"
    exec_install(packages)

# TODO: executar configuração de botões
def install_touchpad():
    packages = "xf86-input-synaptics"
    exec_install(packages)

def install_fonts():
    packages = "ttf-dejavu ttf-liberation ttf-droid noto-fonts"
    exec_install(packages)

def install_flatpak():
    packages = "flatpak"
    exec_install(packages)

def install_desempacotadores():
    packages = "unzip unrar tar file-roller"
    exec_install(packages)

def install_core():
    packages = "xorg lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings i3-gaps i3status i3blocks dmenu network-manager-applet ttf-ubuntu-font-family xfce4-terminal gnome-keyring"
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
    os.system('cp ./* ~/.config/i3/')
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