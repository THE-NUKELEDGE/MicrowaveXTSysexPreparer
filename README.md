# MicrowaveXTSysexPreparer
Changes the last patch in a Microwave I Arrangement Bank dump sysex to ones from a Bank dump sysex using user-specified hex offsets.

## Requirements

- Python 3.x installed on your system.

## Usage

### Step 1: Prepare your source and destination files

Make sure you have the following files ready:

- **Source File**: The file in which you want to replace the data.
- **Destination File(s)**: The file(s) containing the data you want to use for replacement.

### Step 2: Download the script

Download the Python script [write.py](#).

### Step 3: Open a terminal or command prompt

Open a terminal or command prompt on your system.

### Step 4: Run the script

Use the following command syntax to run the script:

```bash
python write.py source_file destination_folder_or_file output_folder source_offset destination_offset size [--incremental] [--chronological]
```

- **source_file**: Path to the source file.
- **destination_folder_or_file**: Path to the folder containing destination files or path to a single destination file.
- **output_folder**: Path to the folder where modified source files will be saved.
- **source_offset**: Offset in the source file where replacement starts (in hexadecimal).
- **destination_offset**: Offset in the destination file to replace data from (in hexadecimal).
- **size**: Size of the replacement data (in hexadecimal).
- **--incremental**: (Optional) Use incremental offset for replacement data.

Example usage:

```bash
python write.py Copy.bin waldorf-microwave-factory-sysex.bin out 667C 0005 B4 --incremental
```
667C(h) is the offset of the final sysex patch for the included Copy.bin that you'll want to use as a base for whatever other sysex you'll be importing patches from, so you probably don't want to change it.
0005(h) is the offset for when patch data starts in Microwave I Bank dumps.
B4(h) is the size of Microwave I sysex patch data and you'll pretty much never change this.
Use the --incremental argument if you want to create banks of all 
