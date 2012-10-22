pythonista-scripts
==================

Python scripts to use in [Pythonista](http://omz-software.com/pythonista/ "Pythonista - omz:software") for iOS. Mostly Markdown-related.

Thanks to Pythonista developer [Ole Zorn](https://twitter.com/olemoritz "Ole Zorn (olemoritz) on Twitter") for feedback and input.

#### ConvertMarkdown

A simple Markdown converter for the clipboard contents.


#### ConvertTwitter

Converts twitter.com URLs (either with http or https, mobile.twitter.com or regular format) to "single status" links for Tweetbot.


#### CopyWebpageTitle

Copy a URL's page title and return title + link format. Example: Tweetbot for Mac Review http://www.macstories.net/news/tweetbot-for-mac-review/

#### Encode HTML

A simple HTML encoder for clipboard contents.

#### ImagesHTML

Uses direct link to image in clipboard to generate HTML code suitable for a center-aligned image with Title and Alt attributes.

#### MarkdownCallback

Same as ConvertMarkdown, but also pastes output into a new Byword document using Byword's URL scheme.

#### ScreenshotsClipboard

Imports two screenshots (iPhone 5) from the iOS clipboard and creates a single image. Based on: http://www.macstories.net/tutorials/a-better-way-to-combine-iphone-screenshots-with-keyboard-maestro/

#### ScreenshotsControl

Takes two iPhone 5 screenshots, places them side-by-side in a single image set to the clipboard. Unlike ScreenshotsClipboard, this script lets you set the placement of screenshots in the final image.

#### ScreenshotsSimple

Same as ScreenshotsClipboard, but images are fetched from Pythonista's image manager.

