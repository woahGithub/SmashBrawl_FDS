import sys

if len(sys.argv) < 3:
    print("Usage: fds_bios.py <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

target_pattern = b"\x00\x38\x4C\xC6\xC6\xC6\x64\x38\x00\x18\x38\x18\x18\x18"
extract_length = 8192

with open(input_file, "rb") as infile:
    data = infile.read()

position = data.find(target_pattern)

if position != -1:
    print("Pattern found at:", position)

    extracted_data = data[position : position + extract_length]

    with open(output_file, "wb") as outfile:
        outfile.write(extracted_data)

    print("Extracted data saved to", output_file)
else:
    print("Pattern not found in the file.")