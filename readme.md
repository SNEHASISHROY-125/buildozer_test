# Build and deploy an Android application using Buildozer
```buildozer -v android debug```

# Check connected devices using adb
```.\adb devices```

# Filter logcat output for Python-related logs
```.\adb logcat -s python```

# Install the generated APK file on the connected device
```.\adb install -r <apk_file_name>.apk```