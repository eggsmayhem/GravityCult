# GravityCult

## What is Gravity Cult?

!['test'](https://github.com/eggsmayhem/GravityCult/blob/main/promotional/GCstonesnobacksmall.png)

GC is an outdoor, International art-sharing app. Artists from around the world paint a rock, then place it and another rock with a QR code/link, and deploy these rocks respecfully in a public area--perhaps their favorite park!

People who stumble upon and scan these rocks will be taken to the online home of Gravity Cult: an international artist collective that enables you to post art, poetry, or link to your online music or art, and state where you are from!

GC also includes a map of all portals, so we can watch the global experience grow in real time!

---

### Future Goals

GC is currently a small app lovingly deployed on heroku. Here are some areas for growth:

#### Translation

Google's translate widget is an incredible and reasonably simple-to-implement feature that would make GC accessible accross languages, which is a primary goal here.

However, incorporating Google translate in this way also exposes user data to more sources of extraction. I would love for us to work together to create a language solution that is as respectful of user data as possible.

Some options:
* Setting up our server so that pings to translate our sent to us first, then from us to Google, so that user IPs stay with us.
* Utilizing Djano app internationalization/localization in a way that protects user data

#### Map
Currently, I am updating a simple SVG map by hand every time a new portal is deployed. I would love to automate this process (and perhaps automate the ability to take down a portal).

Incorporating a robust graphical globe application would be even better, keeping in mind that our goal is to protect our users' privacy as much as possible. See http://radio.garden/ for one of the most beautiful map-based art apps in existence
