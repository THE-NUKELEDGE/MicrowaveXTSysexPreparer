import os
import argparse

def replace_hex_in_file(source_file, destination_file, source_offset, destination_offset, size, output_folder, output_number):
    with open(source_file, 'rb') as source:
        source_data = source.read()

    with open(destination_file, 'rb') as destination:
        destination_data = destination.read()

    source_offset = int(source_offset, 16)
    destination_offset = int(destination_offset, 16)
    size = int(size, 16)

    replaced_data = (source_data[:source_offset] +
                     destination_data[destination_offset:destination_offset+size] +
                     source_data[source_offset+size:])

    output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(source_file))[0] + "_" + str(output_number) + ".bin")

    with open(output_file, 'wb') as output:
        output.write(replaced_data)

def replace_hex_in_file_incremental(source_file, destination_file, source_offset, destination_offset, size, output_folder):
    with open(source_file, 'rb') as source:
        source_data = source.read()

    with open(destination_file, 'rb') as destination:
        destination_data = destination.read()

    source_offset = int(source_offset, 16)
    destination_offset = int(destination_offset, 16)
    size = int(size, 16)

    source_data_length = len(source_data)
    destination_data_length = len(destination_data)

    output_number = 0
    while destination_offset + size <= destination_data_length:
        replaced_data = (source_data[:source_offset] +
                         destination_data[destination_offset:destination_offset+size] +
                         source_data[source_offset+size:])

        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(source_file))[0] + "_" + str(output_number) + ".bin")

        with open(output_file, 'wb') as output:
            output.write(replaced_data)

        destination_offset += size
        output_number += 1

def main():
    parser = argparse.ArgumentParser(description="Replace hex values in a file with hex values from multiple files in a folder.")
    parser.add_argument("source_file", help="Path to the source file")
    parser.add_argument("destination_folder_or_file", help="Path to the folder containing destination files or path to a single destination file")
    parser.add_argument("output_folder", help="Path to the folder where modified source files will be saved")
    parser.add_argument("source_offset", help="Offset in the source file where replacement starts (in hex)")
    parser.add_argument("destination_offset", help="Offset in the destination file to replace data from (in hex)")
    parser.add_argument("size", help="Size of the replacement data (in hex)")
    parser.add_argument("--incremental", action="store_true", help="Use incremental offset for replacement data")

    args = parser.parse_args()
    source_file = args.source_file
    destination_folder_or_file = args.destination_folder_or_file
    output_folder = args.output_folder
    source_offset = args.source_offset
    destination_offset = args.destination_offset
    size = args.size
    incremental = args.incremental

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if incremental:
        replace_hex_in_file_incremental(source_file, destination_folder_or_file, source_offset, destination_offset, size, output_folder)
    else:
        if os.path.isdir(destination_folder_or_file):
            output_number = 0
            for filename in os.listdir(destination_folder_or_file):
                if filename.endswith(".bin"):
                    destination_file = os.path.join(destination_folder_or_file, filename)
                    replace_hex_in_file(source_file, destination_file, source_offset, destination_offset, size, output_folder, output_number)
                    print(f"Hex replaced successfully for {filename}")
                    output_number += 1
        else:
            replace_hex_in_file(source_file, destination_folder_or_file, source_offset, destination_offset, size, output_folder, 0)
            print(f"Hex replaced successfully.")

if __name__ == "__main__":
    main()
