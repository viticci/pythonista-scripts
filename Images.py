import clipboard
import console

image = clipboard.get()

alts = console.input_alert("Image Alt", "Type alt below")
title = console.input_alert("Image Title", "Type title below")

final = "<img src=" + '"' + image + '"' + " " + "alt=" + '"' + alts + '"' + " " + "title=" + '"' + title + '"' + " " + "class=\"aligncenter\" />"

print final
clipboard.set(final)
