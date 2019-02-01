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

+ Instalando VIM
#pacman -S vim

+ Instalando launcher rofi
#pacman -S rofi

+ Instalando lxappearance
#pacman -S lxappearance

+ Instalando visualizador de imagem e wallpaper
#pacman -S feh

+ Instalando htop
#pacman -S htop

+ Instalando navegador de pastas
#pacman -S ranger
$yay thunar
#pacman -S gvfs

+ Instalando Firefox-Dev
#pacman -S firefox-developer-edition firefox-developer-edition-i18n-pt-br

+ Instalando kernel lts
#pacman -S linux-lts
#grub-mkconfig -o /boot/grub/grub.cfg
#reboot
#pacman -Rs linux

+ Removendo tempo de espera do grub
#vim /etc/default/grub

+ Instalando drivers de vídeo e bumblebee
#pacman -S xf86-video-intel
#pacman -S mesa-demos
#pacman -S nvidia-lts
#pacman -S bumblebee
#pacman -S primus
#gpasswd -a l3onix bumblebee
#systemctl enable bumblebee
#optirun glxspheres64	(para testar)

+ Controle de brilho
#pacman -S xorg-xbacklight
#vim /etc/X11/xorg.conf.d/20-intel.conf
----------------------------------------------
Section "Device"
    Identifier  "Intel Graphics" 
    Driver      "intel"
    Option      "Backlight"  "intel_backlight"
EndSection
----------------------------------------------
#reboot

+ Controle de monitor
#pacman -S arandr

+ Controle do touchpad
#pacman -S xf86-input-synaptics
#vim /usr/share/X11/xorg.conf.d/70-synaptics.conf
-----------------------------------
    Option	"TapButton1"	"1"
    Option	"TapButton2"	"3"
    Option	"TapButton3"	"2"
-----------------------------------

+ Configuração de programas padrões
#pacman -S xdg-utils

+ Sensores de temperatura 
#pacman -S lm_sensors
