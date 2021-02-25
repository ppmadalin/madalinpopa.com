---
Author: Madalin Popa
Title: How to install and configure neovim on windwos
Tags: neovim
Date: 2021-02-25
---

I’ve been a Visual Studio Code user for the last 2 years, but sometimes when I want to
quickly edit a text file I use vim. More specificly Neovim. 
In this series of posts I would like to document my Neovim configuration along with the
steps to install and configure for different tasks that you would perform with Neovim. 
Mostly I use Neovim for editing text files and work on small python projects, and in the next
posts I will describe each plugin and setup used to configure Neovim.

More details regarding Neovim can be found at https://neovim.io. Below I will enumerate the steps I use to install Neovim on Windwos. 

**Step 1: Install Neovim using chocolatey**

To install Neovim, I am using Chocolatey which is a great package manager for windows. Below I install the development release of Neovim. 

```bash
choco install neovim --pre
```
**Step 2: Create a init.vim file**

In step 2 we create a configuration file for Neovim. The Neovim configuration file is called `init.vim`, and on Windows it's location is in `C:\Users\<YOUR_USERNAME>\AppData\Local\nvim\init.vim`.

```bash
New-Item -Path 'C:\Users\madalin\AppData\Local\nvim\init.vim' -ItemType File
```
**Step 3: Install a plugin manager**

To enhance your experience with Neovim you will need to install some plugins, and to manage those plugins you will need a plugin manager. 
```bash
iwr -useb https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim |`
    ni "$(@($env:XDG_DATA_HOME, $env:LOCALAPPDATA)[$null -eq $env:XDG_DATA_HOME])/nvim-data/site/autoload/plug.vim" -Force
```
**Step 4: Add the plugin manager to your config file. 

```bash

# Create the folder
mkdir $HOME\.config\nvim\vim-plug\

# Create the plugins configuration file
New-Item -Path '$HOME\.config\nvim\vim-plug\plugins.vim' -ItemType File

# Edit the newly created file. 
nvim $HOME\.config\nvim\vim-plug\plugins.vim
```

Add the below text to plugins.vim
```bash
call plug#begin('~/.local/share/nvim/plugged')

call plug#end()
```

**Step 4: Install additional tools used by the plugins

Some plugins that you will install request to have installed some tools in order to work properly. These are optional but is good to have them. 
Assuming that you have Python and Node.js installed, with the below commands you can install the mentioned tools.
```bash
pip install pynvim
npm install -g neovim
```


At this point you should have Noevim installed and configured with a plugin manager which you will use to install different plugins which will help you in 
your daily use of Neovim. 




