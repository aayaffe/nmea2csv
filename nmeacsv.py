import pynmea2
from pynmea2 import SentenceTypeError, ParseError

ignored_opcodes = ['9C', '10', '11', '82','50','51','52','53']
ignored_nmea = [pynmea2.MWV ,pynmea2.HDM ,pynmea2.RSA, pynmea2.GLL,pynmea2.TXT]
def is_valid_stalk(line):
    parts = line.split(',')
    if '$STALK' not in parts:
        return False
    return True
def get_opcode(line):
    if is_valid_stalk(line) is False:
        return None
    parts = line.split(',')
    return parts[1]

with open('nmealog.txt') as infile, open('output.csv',"w") as outfile:
    for line in infile:
        if '!AIVDM' in line:
            pass
            # outfile.write(line)
        # elif '$STALK' in line:
        #     if get_opcode(line) is None:
        #         continue
        #     if get_opcode(line) in ignored_opcodes:
        #         continue
        #     else:
        #         outfile.write(line)

        else:
            try:
                msg = pynmea2.parse(line)
                if msg.sentence_type == "ALK":
                    outfile.write(msg.command_name + ': ' +" ".join(str(x) for x in msg.data)+'\n')
                elif type(msg) in ignored_nmea:
                    pass
                else:
                    outfile.write(msg.sentence_type+','+" ".join(str(x) for x in msg.data)+'\n')
            except SentenceTypeError as e:
                outfile.write(line)
            except ParseError as e:
                # outfile.write(line)
                pass


