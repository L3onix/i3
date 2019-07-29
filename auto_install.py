import os

def exec_install(packages):
    os.system("pacman -Sy " + packages)

def install_audio():
    packages = "pulseaudio pulseaudio-alsa pavucontrol"
    exec_install(packages)

def install_xdg():
    packages = "xdg-user-dirs xdg-utils"
    exec_install(packages)

def install_appearance():
    packages = "compton feh lxappearance"
    exec_install(packages)

def install_navegador_de_pastas():
    packages = "ranger thunar gvfs"
    exec_install(packages)

def install_kernel_lts():
    packages = "linux-lts"
    exec_install(packages)
    os.system("grub-mkconfig -o /boot/grub/grub.cfg")

def install_video():
    packages = "xf86-video-intel xorg-xbacklight arandr"
    exec_install(packages)

def install_touchpad():
    packages = "xf86-input-synaptics"
    exec_install(packages)

def install_core():
    packages = "xorg lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings i3-gaps i3status i3blocks dmenu network-manager-applet ttf-ubuntu-font-family xfce4-terminal gnome-keyring"
    exec_install(packages)
    os.system("systemctl enable lightdm.service")
    install_audio()
    install_navegador_de_pastas()
    install_video()
    install_appearance()
    
def main():
    print('Executando instalação completa')
    install_core()
    pass

if __name__ == "__main__":
    main()