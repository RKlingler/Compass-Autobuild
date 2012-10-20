Compass Auto-Build-System for Sublime Text 2
=================

What is it?
--------

This might come handy if you are working with [Sublime Text 2](http://www.sublimetext.com/ "sublimetext.com") and [Compass](http://http://compass-style.org/ "compass-style.org"). It automatically compiles your SASS or SCSS files every time you save them. There's no need to have Compass watch running on a command line while you're working on a SASS project anymore.

How does it work?
--------

This auto-build-system consists of two parts, a plugin and a Compass build system configuration for Sublime Text 2. The build system allows you to compile SASS and SCSS files with Compass from within Sublime Text 2, while the plugin triggers the build process automatically when you save a file.

How do I use it?
--------

1. Copy both files to your Sublime Text 2 packages directory. If you don't know how to get there use "Preferences -> Browse Packages..."
2. Select the Compass build system through "Tools -> Build System -> Compass".
3. You should be good by now. If it doesn't work try restarting Sublime and try again.

Of course you don't have to use the auto-build plugin if you don't want the build-on-save functionality. Just throw it away and start the build system manually by hitting Ctrl+B or F7 every time you want to compile your files.