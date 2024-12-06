# This is the buildozer configuration file for the Kivy WebView app.
# It defines the settings and dependencies needed to build the APK.

[app]
title = TestGPT
package.name = testgpt
package.domain = com.mdselim
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = kivy
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1
