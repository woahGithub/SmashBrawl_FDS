import sys

if len(sys.argv) < 2:
    print("Usage: fds_rom.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_prefix = "output"

target_pattern = b"\x00\x00\x00\x01\x2A\x4E\x49\x4E\x54\x45\x4E\x44\x4F\x2D\x48\x56\x43\x2A\x01"
extract_length = 65539

try:
    with open(input_file, "rb") as infile:
        data = infile.read()

    position = 0
    index = 1

    while True:
        position = data.find(target_pattern, position)

        if position == -1:
            break

        print("Pattern found at:", position)

        extracted_data = data[position : position + extract_length]
        output_file = "{0}_{1}.bin".format(output_prefix, index)

        with open(output_file, "wb") as outfile:
            outfile.write(extracted_data)

        print("Extracted data saved to", output_file)

        position += 1
        index += 1

    if index == 1:
        print("Pattern not found in the file.")

except IOError:
    print("Error: Could not open or read file", input_file)
    sys.exit(1)
