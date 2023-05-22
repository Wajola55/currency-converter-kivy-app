[app]
# (str) Title of your application
title = Currency Converter

# (str) Package name
package.name = currency_converter

# (str) Package domain (needed for android/ios packaging)
package.domain = org.currencyconverter

# (list) List of inclusions using pattern matching
source.include_patterns = images/*.png

# (str) Source code where the main.py live
source.dir = /home/wioletta/Desktop/currency-converter/src

# (str) The application version
version = 1.0




# (int) Android API to use
android.api = 29

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
# android.sdk = 25.2.0

# (int) Android NDK version to use
# android.ndk = /home/wioletta/Downloads/android-ndk-r20b-linux-x86_64/android-ndk-r20b






# (list) Permissions
android.permissions = INTERNET

# (str) Your application version code (used only for Android)
android.version_code = 1

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait


requirements = python3,kivy==2.0.0,requests,pillow==9.0.1

icon.filename = '/home/wioletta/Desktop/currency-converter/images/exchange.png'


[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0

