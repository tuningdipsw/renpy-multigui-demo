# Switching GUI styles in Ren'Py

Here's a simple proof of concept for how to fluidly switch between two sets of GUI assets in Ren'Py.

<https://www.renpy.org/doc/html/gui.html#dialogue>  
Ren'Py's docs offer some easy ways to replace the default GUI assets with assets of your own,
but it seems to take a little more work if you want to implement more than one GUI style that you can switch between.

## It's possible that there are better ways to do this

But I didn't find them in the Ren'Py docs, and my web searches didn't turn up much.
It's possible I missed them.

<https://www.renpy.org/doc/html/dialogue.html#defining-character-objects>  
You might be able to try using the Character object's `screen`
and `who_`, `what_`, or `window_` arguments to apply some smaller GUI styles to a specific speaking character.

## Ren'Py version

Ren'Py version 8.1.1 at time of writing. Some changes may be required for Ren'Py 7.x, I have not tested on older versions.

## Usage

You can run the code in Ren'Py yourself by downloading the files for this demo
(on the page for this GitHub repository, click the green Code button -> Download ZIP),
then adding the folder to the same folder as `renpy.exe`.  
This should result in the appearance of a `guitest` project
when you run the Ren'Py Launcher.

This proof of concept is lumped together with the default Ren'Py boilerplate code to make it demoable,
but if you just want to check out the code differences between the default code and the demo,
open up this GitHub repository's commits page and select the "GUI changes" commit.

There are some other misc. changes attached
(eg. some number changes with reducing game window from 1280x720 to 1066x600)
that aren't related to the GUI switching POC, but I've decided to leave them in as a bonus.

## Misc. credits

Font files sourced from Google Fonts.
Photos taken by myself.
