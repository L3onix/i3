2018-12-15

+ Pacotes para modo gráfico
#pacman -S xorg lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings i3-gaps i3status i3blocks dmenu network-manager-applet ttf-ubuntu-font-family xfce4-terminal gnome-keyring

ativando modo gráfico
#systemctl enable lightdm.service

+ Instalando YAY
#pacman -S git
$git clone https://aur.archlinux.org/yay.git
$cd yay && makepkg -si


+ Instalando audio
#pacman -S pulseaudio pulseaudio-alsa pavucontrol

+ Instalando codecs64
$yay codecs64

+ Criando pastas do usuário
#pacman -S xdg-user-dirs
$xdg-user-dirs-update

+ Instalando compositor de telas
#pacman -S compton

+ Instalando launcher rofi
#pacman -S rofi

+ Instalando visualizador de imagem e wallpaper
#pacman -S feh

+ Instalando htop
#pacman -S htop

+ Instalando navegador de pastas
#pacman -S ranger

+ Instalando Firefox-Dev
#pacman -S firefox-developer-edition firefox-developer-edition-i18n-pt-br

+ Instalando kernel lts
#pacman -S linux-lts
#grub-mkconfig -o /boot/grub/grub.cfg
#reboot
#pacman -Rs linux

+ Removendo tempo de espera do grub
#vim /etc/default/grub
