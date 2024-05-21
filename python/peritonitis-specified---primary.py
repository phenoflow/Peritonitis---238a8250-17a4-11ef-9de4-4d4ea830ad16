# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"J512300","system":"readv2"},{"code":"J55yz00","system":"readv2"},{"code":"J13y200","system":"readv2"},{"code":"J14y200","system":"readv2"},{"code":"J12y300","system":"readv2"},{"code":"J11y200","system":"readv2"},{"code":"J13y300","system":"readv2"},{"code":"J512600","system":"readv2"},{"code":"J512y00","system":"readv2"},{"code":"J55y.00","system":"readv2"},{"code":"J12y200","system":"readv2"},{"code":"K28.5","system":"readv2"},{"code":"K25.6","system":"readv2"},{"code":"K26.6","system":"readv2"},{"code":"K57.8","system":"readv2"},{"code":"K27.5","system":"readv2"},{"code":"K27.6","system":"readv2"},{"code":"K26.5","system":"readv2"},{"code":"K27.1","system":"readv2"},{"code":"K27.2","system":"readv2"},{"code":"K28.6","system":"readv2"},{"code":"K25.5","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('peritonitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["peritonitis-specified---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["peritonitis-specified---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["peritonitis-specified---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
