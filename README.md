*Documentation of How to Use OBDII Sensor Information in Vuforia*

Requirements:

-   Raspberry Pi 2 Model B, with Raspbian installed

-   Battery Pack with Micro USB Cord

-   Plugable USB Bluetooth 4.0 Low Energy Micro Adapter

-   ELM327 Bluetooth Adapter

-   Raspberry Pi Compatible USB Wifi Adapter

-   Wifi Hotspot

-   Laptop computer

-   External monitor

-   HDMI cord

-   Keyboard

-   Mouse

Directions:

1.  Connect the Raspberry Pi to the USB wifi adapter, keyboard, mouse, and the external monitor with the HDMI cord.

2.  Plug the Raspberry Pi into battery pack to power it up. Then log in.

3.  In the shell, run the following command to power up the GUI:
    ```
    # startx
    ```
4.  In the GUI connect to your wifi hotspot.

5.  Open a new terminal window and run the command:
    ```
    # ifconfig
    ```
6.  From the printed output, find the wlan0 section, and note the inet addr for later use.

7.  In the terminal, run the following commands:
    ```
    # sudo apt-get update
    
    # sudo apt-get upgrade
    
    # sudo apt-get autoremove
    
    # sudo reboot
    ```
8.  After rebooting, run to following commands to install necessary components:
    ```
    # sudo apt-get install python-serial
    
    # sudo apt-get install bluetooth bluez-utils blueman
    
    # sudo apt-get install bluez bluez-tools
    
    # sudo apt-get install python-wxgtk2.8 python-wxtools wx2.8-i18n libwxgtk2.8-dev
    
    # sudo apt-get install git-core
    
    # sudo reboot
    ```
9.  Then, install the OBD\_Pi\_AR software, by running the following commands:
    ```
    # cd \~
    
    # git clone https://github.com/danniss10/OBD_Pi_AR.git
    ```
10. Shut down the Raspberry Pi:

    ```
    # sudo shutdown now
    ```
    
11. Once the Raspberry Pi has successfully shut down, disconnect the mouse, keyboard, HDMI cord, and battery pack from the Raspberry Pi.

12. Set aside the Raspberry Pi and set up ThingWorx in a browser on the laptop:

    a.	Launch Thingworx instance.
    
    b.	Select “Application Keys” under the Security tab on the home page. 
    
    c.	Select the green plus key to add a new application key.
    
    d.	Give the key a name as well as a username for the “User Name Reference” category.
    
    e.	Select save. The application key will be generated. Note this application key for future use.
    
    f.	On the home page, under modeling, select “Things”, and created a new thing by selecting the green plus sign.
    
    g.	Give the thing a name, and to the right of “Thing Template”, make the thing a “Generic Thing”.
    
    h.	Select save.
    
    i.	Select the name of your thing which should be one of the tabs at the top. Select edit and then select properties under “Entity Information”
    
    j.	Select the “Add my property button”
    
    k.  Create the following properties as “My property” and with the following “Base Type” and then select save

    -   Property: rpm   Base Type: #
        
    -   Property: load   Base Type: #
        
    -   Property: fuel_status   Base Type: -T-
        
    -   Property: speed   Base Type: #
        
    -   Property: throttle_pos  Base Type: #

13. Carry Raspberry Pi with Bluetooth and wifi adapters, battery pack, wifi hotspot, and laptop out to your car. Then, plug the battery pack back into the Raspberry Pi to start it up again.

14. On the laptop computer, open a terminal and run the following commands to remotely access Raspberry Pi shell:

    ```
    # ssh <username>@<inet addr>;
    ```
15. Plug ELM327 Bluetooth Adapter into OBDII port. Then, in the terminal window, use the following commands to connect to the Bluetooth adapter:

    ```
    # hcitool scan
    ```
-   This command scans for available Bluetooth devices and should display the name and Mac Address (XX:XX:XX:XX:XX:XX) of your ELM327 Bluetooth Adapter. Note the Mac Address.

    ```
    # bluez-simple-agent hci0 <Mac Address>
    ```
-   This command will prompt you to enter the pin for pairing the ELM327 Bluetooth Adapter. If the manufacturer did not provide the pin, it will likely be “0000,” “1234,” or “6789.”

16.  Create a serial connection between the ELM327 Bluetooth Adapter and the Raspberry Pi, by using the following commands:

    ```
    # sudo nano /etc/bluetooth/rfcomm.conf
    ```
    -   This command will open the nano file editor. Add the following script to the file:
        ```
        rfcomm0 {
            bind no;
            device <Mac Address>;
            channel 1;
            comment “Serial Port”;
        }
        ```
    
    -   Press ‘ctrl-x’, then ‘y’, followed by ‘enter’, to save the changes.
        ```
        # sudo rfcomm connect 0
        ```
    -   Now the Bluetooth serial connection should be running.

17.  On the laptop, open a new terminal window, and run the following commands to remotely access Raspberry Pi shell:

    ```
    # ssh <username>@<inet addr>
    ```
    
18.  Turn on the car.

19.  Run the thingxpi.py code to transmit data to ThingWorx, with arguments: thing name, URL, app key.

    ```
    # cd OBD\_Pi\_AR
    
    # sudo python thingxpi.py <thing name> <url> <app key>
    ```
    
    -   This should print live OBDII data in the terminal window, as well as a response code 200 indicating successful connection to ThingWorx.

20.  Under the same Vuforia Experience Server as the ThingWorx server, create a new experience.

    a.  Add a ThingMark to the canvas and associate it with the code assigned to the intended ThingMark.
    
    b.  Click the ‘Add +’ button under data and search the name of the thing created in ThingWorx. After selecting the thing, search for “GetPropertyValues” in Filter Services search bar, and click the ‘+’ button.
    
    c.  Under the 3D view add 5 3D Sensor widgets, and for each widget:
    -   Under Data, select the ‘Current Selected Item’ dropdown menu, and drag each of the properties over to the circle next to the Text field under Properties.
        
    d.  Under Data, select the Configuration dropdown menu, and check the boxes next to ‘Invoke On Startup,’ ‘Auto-select first row,’ and ‘Auto-Refresh.’
    -   Set the Auto-Refresh rate at ‘1’ for updates every second.

21.  Publish the experience.
