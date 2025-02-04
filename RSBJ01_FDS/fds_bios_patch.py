import sys

def edit_binary(input_filename, output_filename):
    changes = [
        (0x0239, 0x42, 0x85),
        (0x0406, 0x42, 0x85),
        (0x073E, 0x4C, 0xA2),
        (0x073F, 0x43, 0xB2),
        (0x0740, 0xE7, 0xCA),
        (0x07A4, 0x42, 0x4C),
        (0x0EF4, 0x42, 0xA5),
    ]
    
    try:
        with open(input_filename, 'rb') as f:
            data = bytearray(f.read())
        
        for offset, before, after in changes:
            if data[offset] != before:
                print("Warning: Offset 0x%X expected 0x%X but found 0x%X" % (offset, before, data[offset]))
            data[offset] = after
        
        with open(output_filename, 'wb') as f:
            f.write(data)
        
        print("File saved as", output_filename)
    except IOError as e:
        print("Error: %s" % str(e))
    except IndexError:
        print("Error: File is too small to apply all changes.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fds_bios_patch.py \'<input_file>\' \'disksys.rom\'")
    else:
        edit_binary(sys.argv[1], sys.argv[2])
