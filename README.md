# Vrk
Vrk supercharges your ubuntu desktop experience by "breaking it in" with settings, theming, wallpapers, apps, and more.

###### Environments
- Xfce (Xubuntu/UbuntuStudio) has the most support, with 1/4 window hotkey tiling and even the "Xfdashboard" window spread.
- GNOME & Budgie are well-supported provide a rather awesome experience already, so they have just a little less tweaking.
- MATE is semi-supported, but not much since it is a legacy by definition.
- Mint (Cinnamon, Xfce, and MATE) is supported, but already makes things "Minty", so it has few changes so as not to interfere.

###### Xubuntu/UbuntuStudio Hotkeys:
Win          opens the menu, finally.
Ctrl + Win + Up/Down/Right/Left tiles your window in 1/2 screen.
Shft + Win + Up/Down/Right/Left tiles your window in 1/4 screen on the top.
Alt  + Win + Up/Down/Right/Left tiles your window in 1/4 screen on the bottom.
Ctrl + Win + Alt shows your window spread & dashboard.
Scroll on the desktop to switch workspaces.

###### Other environments
- Unity does retain legacy support and is quite awesome with Vrk. Vrk "desktop" was originally written to make Unity 7 "less unbearable". In the end, Unity 7.5 with the Vrk Desktop scripts weren't only "less unbearable", but made a pretty awesome desktop experience. Unity legacy will remain as long as Ubuntu 16.04 LTS is supported, likely through 2021. Eventually, Vrk may put Unity 8 for tablets into the mix, cheers to the guys over at [http://UBports.com]! Shuttleworth, you weren't wrong, just busy changing the world where you were most needed.
- KDE/Kubuntu? No way. The roadmap for KDE is already awesome and doesn't need help, it's desktop preferences (viz no Ctrl+Alt+T terminal, abnormal Dolphin file manager actions, etc.) are too weird for "Vrkers", and it's too buggy and doesn't always boot up for development. KDE is anti-supported by the release of Vrk beta 0.4. That said, KDE has awesome ideas. IMHO, their talent is wasted on desktop; they need to focus on making their awesome apps awesomerer. The same could be said of MATE, but legacy GNOME is understandable, except they at least need easy-accessed search. We need fewer desktop environments to spend our developer energies on, not more.
- LXDE and others, sorry, really. If you want, write in the support and make a pull request.
- Manjaro/Arch support is coming. The code has already been written in anticipation of this so the pacman installers can just be dropped in.

##### BETA:
This has only been tested with Ubuntu: Xfce (Xubuntu), Unity (Ubuntu, legacy but still working for the 16.04 LTS), GNOME, KDE, Cinnamon, and Mate. Linuxmint has limited testing, but should theoretically work. Manjaro is a later goal.

##### ALL REPOS MUST WORK!!!
*If you get "E:" error messages after running* `sudo apt update` *then you need to go to Software & Updates > Other Software, and then remove whatever ppa repo is in the error message.*

*If you have errors in `sudo apt update` then Vrk will not install because your system just has too many loose bolts. Button up first, then "get to Vrk". (Did you see what I did there?)*

Read the README.md before reporting problems! !! Seriously.

# What is Vrk?
- inkVerb's Vrk app is a collection of simple scripts that sets up a useful configuration for main Ubuntu distros
- The installer adds many apps, settings, and special Vrk shell scripts, including scripts that make SSH, Git, and FileZilla easier to integrate.
- A hidden folder will be created in home: `.vrk`. It contains `.vrk/boards`, which has a list of files you can run...
- In `.vrk/boards`, all normal script files (green, from vrk/surf and vrk/droids) in `.vrk/boards` you can run from any working directory. Symlinked (light blue, linked from vrk/boss) require being in the`.vrk/boards` directory and using `sudo ./` these only show up for sudoers who ran `install-vrk` themselves.
- All these `boards` have their own purpose and instructions at the top of the files. READ THEM!
- HAVE FUN! !! Seriously.

## How to Install
- Breeze through this README.md first!!
- Put "vrk" in your home folder
- Download it lone it with this:

`git clone https://github.com/inkVerb/vrk`

- Open the terminal (Ctrl + Alt + T)

`cd /vrk/inst`

`chmod +x govrk`

`sudo ./govrk $DESKTOP_SESSION`

- Answer the two simple folder questions carefully
- The machine will reboot if you are installing the first time.

`cd ~/.vrk/boards`

`sudo ./install-vubuntu`

### Other Users
For other users on your system, you can run:

`cd ~/.vrk/boards`

`sudo ./install-vrk user`

However, if you want that user to have sudo privileges for Vrk "boss" tools, that user must run it himself.

After install, this is how to install Vrk for a second sudo user:

`cd /var/local/vrk/boss`

`sudo ./install-vrk`

Now, the user that ran this will have Vrk in his own system.

- You can run `install-vubuntu` for another user, but if you do that user won't have access to `bosses` that require sudo privileges.

`set-vrk-desktop` (each user must run this himself, can't sudo it for another user)

`cd ~/.vrk/boards`

`sudo ./install-nextcloud` or `sudo ./install-dropbox`

`sudo ./install-vrk-cloud` or `sudo ./install-vrk-cloud user` is another option for the Vrk cloud sync

- Done! :-)

### Updates
- If already installed, the same install procedure will update instead.
- Some specific features per user must be updated per user.
- This will update the core and all users:

`cd /vrk/inst`

`chmod +x upvrk`

`sudo ./upvrk $DESKTOP_SESSION`

Note: Update version numbers reference the framework. Ongoing updates continue for the surfer and boss, etc job scripts. Framework needs rated, sequential alteration, which is why "version" numbers apply to them. Any update will update job scripts, regardless of the current version number.

## Where stuff is
- Your "Work" folder (whatever you set in govrk) syncs your docs in your cloud folder (whatever you set in govrk).
- If you're a LinuxNOOB, you should know that `~/` is a universal wildcard for your "home" folder, literally at `/home/YOU/`. This is the folder you almost always open to in Ctrl + Alt + T = Terminal or the fild browser.
- In the hidden folder `~/.vrk` you'll see the goodie at your disposal:

1. `boards` has the "Surfers" you can use, tools to manage your system. Most of these are global and you can run them from any terminal.

   *Colorful linked files are "Bosses" that install and change things and require sudo. Run them with:*

   `cd .vrk/boards`
 
   `sudo ./WHATEVER-BOSS`

2. `configs` has stuff you only want to touch if you don't mind messing up everything and really want to learn how Vrk works.
3. `donjon` has stuff that Bosses need, generally don't mess. But, there are some hidden goodies in there if you aren't afraid of the dragons.
4. `go` has your quick scripts that let you SSH your way into remote servers very quickly and control them from the command line.
   *Add "Go Surfers" by following the instructions in the "Go Surfers" instructions.*

## Go Surfers
*Go Surfers are an awesome say to access FTP/FileZilla and SSH/Terminal access to web servers.*

- These are located in `.vrk/go` and also can be run from any working directory.

### Here is the Go Surfer config hierarchy tree
*(These Surfers configure the Go Surfers)*
*(ssh-add-all runs all of them... except ssh-guake-on, which you probably don't want anyway.)*

     ssh-add-all                   # takes all SSH credentials and adds them everywhere, even creating an SSH key if it doesn't already exist

       ?ssh-craft-key              # creates an SSH key that can be uploaded to a server for no-password login; included in ssh-add-all  IF the key doesn't already exist

          ssh-add-goguake          # creates gosurfer and adds him to Guake-Indicator

            ssh-add-gosurfer       # creates a gosurfer

            ssh-add-guake          # adds gosurfer to Guake-Indicator menu

          ssh-filezilla-addkey     # adds gosurfer and SSH key to FileZilla

          ssh-add-key              # uses password to login and upload an SSH key to a server for future no-password login

       ssh-guake-indicator-on      # sets guake-indicator menu to load at startup

     ssh-guake-on                  # sets guake-indicator menu to stop loading at starup and guake instead

## Droids
- Droids are located in `/var/local/vrk/droids`.
- Droids are not changed or removed with an update and you can add them yourself.
- Droids can perform sudo tasks, but unlike bosses, they are included in your path. So, you can run them without ./ and sudo is optional.

## myWall
- Use mywall to add your own "favorite" wallpapers to the normal list you see for changing your desktop background.
- Your myWall pictures and config .xml file are in `.vrk/myWall`
- myWall is synced to your cloud if you use `install-vrk-cloud`

## Vrk Cloud
- This puts Work folder, Documents, Templates (not in Xfce), and your myWall additions to your cloud folder for sync.
- Install it from `.vrk/boards` with: `sudo ./install-vrk-cloud` or `sudo ./install-vrk-cloud user`

## Different installs
- govrk sets up Vrk for the machine (computer): folder and cloud structure, templates, and the ability for other Vrk tools to function
- govrk also runs the updater (upvrk) if Vrk is already installed. Run `sudo ./upvrk user` to complete small updates per user.
- install-vrk installs config files and structure for a specific user (automatically initiated by govrk, but only for that user)
- install-vubuntu installs apps and Vubuntu desktop settings & wallpapers
- install-vrk-cloud Vrk cloud (see above)

## More Info
### Ubuntu distros, "Vubuntu Desktop" and Vrk goals
- Vrk adds a special folder configuration: Documents becomes a folder synced in your choice cloud, along with the new "Work" folder.
- ...a simple collection of Templates most may find useful, which syncs to your choice cloud, except in Xfce.
- ...several small "Surfers" (bash scripts) that help connect your computer to a VPS via SSH, and works particularly well with a Verber™ server.
- Vubuntu Desktop is a kind of "should-be out-of-the-box" configuration for Ubuntu intermediate power-users. The purpose is to bring some continuity for common desktop settings across platforms, setting them up quickly and somewhat standardized so that people can get to work rather than spend hours configuring all the same settings at every fresh Ubuntu install, without interfering with settings or functions that users enjoy in different desktop environments. Eg. Kate is the default editor in KDE, Gedit in all others, but this can be changed either way with set-kate-edit and set-gedit-edit.
- Target distros include: GNOME, Mate, and Xubuntu (Xfce); Kubuntu (KDE) and Mint (incl Cinnamon, Mate, KDE, Xfce) are tested for compatability, but second priotiry since Kubuntu lacks command line control and stability. Lubuntu and Edubuntu aren't tested.
- Ubuntu Studio is intended for compatability, but not tested since install .iso images sometimes have trouble. That said, Ubuntu Studio integration is top priority. Wherever Vrk's roadmap finds a conflict with a distro and the ubuntustudio repo packages, Vrk adopts scripts to "trump" settings structures and "Make Ubuntu Studio Work Again."
- Arch and Red Hat (Fedora/CentOS) are not goals because they lack Debian, Arch is already labor intensive by definition and purpose and thus contrary to scope, and Red Hat already has their own thing going.
- Vrk works as close to Ubuntu and Debian cores as possible. The main difference is a GNOME/MATE/Xfce/Unity/KDE check for settings, such as dconf, gsettings, and xquery... or sed and cp for KDE.
- The purpose of Vrk was, initially, to bring a lite version of Ubuntu Studio to your choice of Ubuntu distro. Then it grew.

### Folder configuration
- Vrk makes used of Documents, the folder no one uses, by making it a synced folder accessible outside your cloud folder.
- Vrk creates a new "Work" folder for that misc. stuff we use all the time, but don't know where to put. You give it your own name, in this documentation it is called "Work".
- Vrk asks for your primary cloud folder name in which to sync Documents, Templates, and your Work folder; it can be anything.
- These three synced folders move to your cloud and link back to your home folder.
- Vrk installs a set of templates the first time, but won't if it detects a existing Templates folder in your cloud on future installs. Install original Vrk templates anytime via install-vrktemplates.
- Media and Public folders don't move to your cloud because those are usually intended to be local and manged by the user
- Vrk has back-end "machine names" such as VRK_DESKTOP_DIR to match XDG_DESKTOP_DIR, via ~/.vrk/configs/lang/stationuser-dirs_CURRENT
- Vrk vrk adds two machine names VRK_WORK_DIR (Work folder) and VRK_CLOUD_DIR (primary cloud folder) via ~/.vrk/configs/stationinfo
- Vrk changes all folders from whatever language into English, for programming ease.
- If the user's initially installed folders are non-English, Vrk creates ~/MyLang/ and with links to all home folders in the original language, for user reference. English folder names are easier for coding.

### Names
- Vrk's various scripts that do different jobs are called "Surfers". Surfers that require sudo are called "Bosses", but aren't available to non-sudoers.
- A machine with Vrk installed is called a "Vrk Station"
- In other areas of the inkVerb universe, you will see Knights, Serfs, Yoemen, Donjons, and even Dragons. Vrk Stations are for "Surfing" the cloud kingdom and are more relaxed. Verber and Inker from inkVerb are a little more serious as they manage castles in the cloud.

### Integration
- A Vrk Station is intended to do whatever work on your computer, but also effectively control cloud servers.
- Vrk has Surfers to create and add SSH credentials and keys to guake-indicator, FileZilla, a remote server, and Vrk's "gosurf" ssh script, fully via back-end command line.
  - Use: craft-sshkey, add-sshall
  - Surfers are copied to ~/.vrk/boards/
  - Bosses are linked to ~/.vrk/boards/ (only for sudoers) and so they appear as a different color when using "ls" in the terminal.
- A Vrk Station can control many clouds quickly and easily, but also has integration with OpenSource "Verber" servers, see the inkVerb GitHub project and http://verb.ink

### Back-end
- When you install, the vrk "core" folder will move to /var/local/, then creates a .vrk folder in your home withconfigs and links to the core.
- You will need to copy vrk to the home folder each time you want to install it for a user. It's somewhat a one-user-machine app, but can work for others.
- To update Vrk, run the updatevrk Surfer.

### Vubuntu
- Surfers can install different apps quickly and easily, such as install-vubuntu, a lite Ubuntu Studio with common extras, including editors, browsers, dekstop tools.
- installvubuntu runs apt-get install scripts in batches, just in case Internet is unstable. If you get cut-off, you should be able to start over and pick up close to where you lost Internet.
- If you want a full Ubuntu Studio install from the command line, using installvubuntu first will get those EULA and other interactive questions done first and make the rest of ubuntu-studio a lot faster.
- Included with installvubuntu is Docky with a rollup of several common apps and a transparent dock configuration, some normal settings for Guake, and the like.
- Vubuntu is a long-term plan as a possible distro, but aims to work as a seamless add-on for the main Ubuntu distro desktops. If ever a distro, it owuld aim for easy desktop environment changes.
- Note, installvubuntu includes Chris' Dynamic Compressor plugin for Audacity. We remember.


