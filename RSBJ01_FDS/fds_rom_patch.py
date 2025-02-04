import sys

if len(sys.argv) < 4:
    print("Usage: fds_rom_patch.py <output_file> <input1> <input2>")
    sys.exit(1)

output_file = sys.argv[1]
input_files = sys.argv[2:]

try:
    with open(output_file, "wb") as outfile:
        for i, input_file in enumerate(input_files):
            print("Merging:", input_file)
            with open(input_file, "rb") as infile:
                data = infile.read()

                if i > 0 and len(data) > 16:
                    data = data[16:]

                if len(data) > 4:
                    data = data[:4] + b'\x02' + data[5:]

                outfile.write(data)

    print("Merged file saved as:", output_file)

except IOError as e:
    print("Error:", str(e))
    sys.exit(1)