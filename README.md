# 🛠️ Tools Future

## Table of Contents

- [Features](#features)
- [Screenshot](#screenshot)
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)

## Features

- **File Dump**: Extract and save raw data from Facebook friends list.
- **Remove Duplicate IDs**: Eliminate duplicate entries from your ID list.
- **Remove Used IDs from File**: Filter out IDs that have already been processed.
- **Separate IDs**: Split a list of IDs into another file.
- **File Mixer**: Shuffle ids.
- **Divide File Equally**: Split a large file into equally sized smaller files.
- **Remove Stylish Names**: Clean up names by removing non-standard characters.

## Screenshot

![Tool Overview](IMG_20241021_212736.jpg)

## Getting Started

### Clone the Repository

To get started, run the following commands in your terminal:

```bash
cd $HOME
rm -rf DUMP
git clone --depth=1 https://github.com/JISAN-404/DUMP
cd DUMP
python3 FILE.py
