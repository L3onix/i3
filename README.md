# Configuração de ambiente i3 no Arch Linux

1. **Pacotes básicos para modo gráfico**
    > Lista contém o servidor gráfico (*xorg*), além de um display manager (*lightdm*) e o ambiente gráfico i3wm.
    ```sh
    # pacman -S xorg lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings i3-gaps i3status i3blocks dmenu network-manager-applet ttf-ubuntu-font-family xfce4-terminal gnome-keyring
    ```    
    > ativando modo gráfico
    ```sh
    # systemctl enable lightdm.service
    ```

2. **Instalando YAY**
    ```sh
    # pacman -S git
    $ git clone https://aur.archlinux.org/yay.git
    $ cd yay && makepkg -si
    ```

3. **Instalando audio**
    ```sh
    # pacman -S pulseaudio pulseaudio-alsa pavucontrol
    ```

4. **Instalando codecs64**
    ```sh
    $ yay codecs64
    ```

5. **Criando pastas do usuário**
    ```sh
    # pacman -S xdg-user-dirs
    $ xdg-user-dirs-update
    ```

6. **Instalando compositor de telas**
    ```sh
    # pacman -S compton
    ```

7. **Instalando VIM**
    ```sh
    # pacman -S vim
    ```
    
8. **Instalando launcher rofi**
    ```sh
    # pacman -S rofi
    ```

9. **Instalando lxappearance**
    ```sh
    # pacman -S lxappearance
    ```

10. **Instalando visualizador de imagem e wallpaper**
    ```sh
    # pacman -S feh
    ```

11. **Instalando htop**
    ```sh
    # pacman -S htop
    ```

12. **Instalando navegador de pastas**
    ```sh
    # pacman -S ranger
    $ yay thunar
    # pacman -S gvfs
    ```

13.  **Instalando Firefox-Dev**
```sh
# pacman -S firefox-developer-edition firefox-developer-edition-i18n-pt-br    
```



14. **Instalando kernel lts**
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
