import shutil
import os

source_file = "cmake-build-debug/AudioPluginExample_artefacts/JuceLibraryCode/JuceHeader.h"
destination_file = "JuceHeader.h"

# Check if the destination file exists, if not, create it
if not os.path.exists(destination_file):
    with open(destination_file, 'w'):
        pass

# Copy contents of source file to destination file
shutil.copyfile(source_file, destination_file)

print("File copied successfully!")
