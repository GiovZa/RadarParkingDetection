Open Anaconda Powershell:

cd C:\Users\vox_m\Downloads\CS437_IoT\Labs\lab4\lab4\lab4_prelab_final\Industrial_Visualizer

conda activate cs437

cd ..\boot

Turn all switches OFF on radar
Plug Radar into right USB port

python arprog_cmdline.py -p COM4 -f motion_and_presence_detection_demo.release.appimage -s SFLASH -t META_IMAGE1

Unplug radar
Turn leftmost switch into ON state
Plug Radar into right USB port

Make a new Anaconda Powershell:

cd C:\Users\vox_m\Downloads\CS437_IoT\Labs\lab4\lab4\lab4_prelab_final\Industrial_Visualizer

conda activate cs437

python gui_main.py

In GUI:
CLI COM -> COM4
Check Save UART

Select Configuration -> C:\Users\vox_m\Downloads\CS437_IoT\Labs\lab4\lab4\Lab 4 Prelab Files\profiles\xwrL64xx-evm\PresenceDetectDemo

Click Start and Send Configuration

Pray