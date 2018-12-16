2018-12-15

+ Pacotes para modo gráfico
#pacman -S xorg lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings i3-gaps i3status dmenu network-manager-applet ttf-ubuntu-font-family xfce4-terminal gnome-keyring

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

