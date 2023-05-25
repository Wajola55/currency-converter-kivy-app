[app]
# (str) Title of your application
title = Currency Converter

# (str) Package name
package.name = currency_converter

# (str) Package domain (needed for android/ios packaging)
package.domain = org.currencyconverter

# (list) List of inclusions using pattern matching
source.include_patterns = images/*.png,libs/*.jar

# (str) Source code where the main.py live
source.dir = src

# (str) The application version
version = 1.0

android.sdk = 34
# (str) Android SDK Build-Tools version
android.build_tools = 34.0.0-rc4

android.ndk = 22
android.gradle_dependencies = 'com.android.support:support-v4:27.1.1'

# (int) Android API to use
android.api = 30

# (int) Minimum API required
android.minapi = 21

# (list) Permissions
android.permissions = INTERNET

# (str) Your application version code (used only for Android)
android.version_code = 1

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

requirements = python3,kivy==2.0.0,requests,pillow==9.0.1

icon.filename = 'images/exchange.png'


[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
