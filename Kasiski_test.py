import os

text="""ceaaa dadda badca dbacd ceade bdada becdc ecebc dedbd bcbdc ccdad accad ddccb ccced badbd ceddb aeaaa acabb bbaec dbcde cedca cdcbb eacdb aaacb aaaec bdbac addad aedba acadd edaec edbad bdead aadda bccee cddbd badbd caead edbbc beaba eacaa dcaaa ccbbd caace baadd bdbbc cbaac dacce cecce ebdba ccdca daaad dabcd edbad eabae accdd aacae adedb bcbad cebbd bcdcd baace cddeb cbadd cabda dddbb dcacd ebbca bdaba ccdda acdcd dbaca bcddb aadad addca ccdab caced bbcbb caaab dbccd cdbaa eccad ddbad adcdd bdccd baaed dccdc bbbab acddc badba debdb cadad cecbb cabcb dbaea daeaa caadc cabed dbced badac ecaba eaaaa cacca bbaad bcebb ddbad dadba dddba dcebb caaaa dbcba aaaac dacce aaaab cdadb aaedd ccdbc ddaad bccae dbcce aacba eadba deadc cddba aadad baeda cbdcc accec adacd dccaa acdba cdaac aacbc aaacc aabdd acadb cbdcd bacac adcbd baacc dacea cabdd ddcdd badcd acaaa bcbcb dbaed acbdb aceca dacdc cdbaa eccad ddbac dacea daedb cceaa cbaea dbadd bbdea ddbab cdacd bccdb adaac daadc cbcdb deadd badaa ddabc cbdba cecad acdaa caada aaedd baaac ecdba adada ddbac dacea deada acdbd acede ccadd baaca eaadd bcddb aceca addcc dbaca eddba dcaac ddbad aedba addbb baacb bcead dbcba dadad cbcaa caaca eacdb aeace caaad eadda aebdb cedaa daadb ccbac ccdde daeba dbadd baacc ddaaa caead accda bcaab cadad acbca cdaca eacae debba baead bdead bbdba cbbba bacdd ecccc aadba dadad adbac dbacd badea dadce bbded dbaaa cecda aaebc dbcdd aadbc cbcdb aeccb cacea eacdd badac dbead adade addaa dbada baada daece caaab edcbd baacc acdbc aaadb ccddb abaad dbadd baaec cadac eadea dadac accce dcaaa adbbb deaee dacae ddbaa acecb cdbaa dadac aacdd baddb addba cecec accda aaeba acdac adbaa ccdda aacaa dadae cecac aeada abcdd aadaa beada ccbed aaaed babaa ddbad ebacc adabc ddaad aadba adada ddbae eadaa ccbec ccbae ccada ceade bacdb dcebb ceddb abced caecc acbdb acbaa accda bcaaa ccdda aacae badaa badba aaabd bccac aecca ddacc abdcc aeddb addcc bdaca cacda deaca bdbbc cecee bccac bceab dacea dbcbd baded abcde cedda cbdcb ebccd abdab cbdcc ddcbc bcbbd bcdec eeaad acabd ebdbd badbc becad cedda decbd badce bbcaa bccad ebbca bacaa ddabc bccec eccbc adbad dccad bbcbc dbadd bacbe cdaca aecca ddead adbbd daaeb dbdba cabda dadca cacdd bbbca cedac badac cdddc abdaa dceba ddbad cbbbd baeaa aacaa ddbda cedea deaad dabbc dddac acada dbcba cebde eabae aeadd cbbca bccaa ebaac aadba dbadd cabda deadb cecce aabca ceaaa addbc cbbae addac dcace bcedd daded bcbdb abace dddcb aadbb cadeb dbcca caadb cdbbb dbcdc dbaca dedac bdbaa caded dbcce bbcab acded adbad dbaea ccdab cdbac aedcd bbdce ddade bddbc cbaea ccbcd bbbdb cdcbc eeacb bbdaa ddadd aacdb acbac ccdda abadd cbaad ecedc ecdbc ebbdd ccdbb dcadd adaca dbceb bbccc eecea daaed ebece caaab ecedc aadad ccaad ebdbc aadec edead eaadc badda cceac bacaa ecedd aaa"""

numbers="""35 45135 45331 32544 13452 53523 15511 25555 11533 34544 25525 34112 35345 54414 53531 54531 45312 52554 44114 31251 53551 55454 52425 45354 52431 35515 35315 55321 54314 14413 55515 31545 31435 35144 25353 53535 34415 25355 34423 53125 25134 54354 14335 43515 13445 34414 31455 22551 45334 53353 12555 35351 44555 31535 31254 55455 45253 55344 22351 23544 55535 35145 35443 53311 44534 43413 54533 42545 44445 54553 15444 22515 35353 31554 55354 51441 45534 42441 44454 54555 35212 25545 35351 53513 53535 31455 34511 43412 45525 53533 45311 55453 41444 44243 12535 25125 45535 51453 53531 53512 43125 25544 54543 14535 12355 31515 33114 53543 12225 43132 53142 55435 35254 25153 55353 14553 44441 53545 42154 45325 24525 53153 14455 53531 45535 14551 35314 41353 12455 21252 53534 55354 24151 35435 45352 15442 55535 41354 51535 35311 45144 45413 51345 55314 45335 44253 51455 15354 13531 24545 35212 25545 35345 22542 15445 32524 52553 15534 43145 35445 54545 45353 51235 14541 53453 14531 53535 14451 53541 35312 43142 53514 11444 54534 53533 15545 35345 22543 53554 54352 54533 55343 12543 51515 35354 13253 45453 53215 53153 51455 31525 53513 54143 55144 25354 42331 55444 45144 52525 45355 35124 25431 11543 45351 54555 35454 41345 54135 33553 53535 35453 12144 31435 45144 54443 31554 44553 52525 42153 34335 25345 31441 53551 14341 24413 35454 53153 31555 35453 55535 33142 35123 51144 45453 43514 51534 44153 54544 45351 42415 25525 45531 52553 35353 52154 55453 54115 33155 35124 25113 44435 45425 53533 14454 45351 13553 15535 21225 52545 43535 31445 32512 13543 42353 15111 44114 44545 34445 35331 55351 45531 55355 34313 51244 55255 24454 51445 35354 53121 44331 55351 24452 53254 44153 55443 14354 11454 25535 11355 31533 54115 54441 53554 53533 15545 35535 35122 11225 12122 55254 54335 45335 12351 55355 51345 55455 15353 31435 45144 54354 53121 44335 35444 53514 44545 41221 22554 35351 35321 55315 55544 52535 45135 14445 34415 51342 25455 54443 52534 42535 31451 53551 34521 45434 22351 31441 35341 54244 24515 35513 51352 51534 53535 44421 21335 45535 51535 43122 25425 54433 42541 33535 14444 35534 34445 31545 35534 42553 53531 42144 14421 22554 35354 34115 43453 53511 44531 33135 45441 44435 45211 51254 45544 43534 33155 31534 23531 25255 44541 45551 32535 25455 11535 41441 15544 42541 45535 31255 55551 44425 54524 45435 53153 53311 44533 14442 52254 44145 45351 54544 31254 15453 14535 13415 31444 25355 14141 35553 51425 43453 45325 13444 42354 45553 54151 35515 35543 35154 54334 25413 41355 31553 55354 51445 35155 55534 43545 53544 54223 12545 44442 35445 53533 53423 52545 15513 15353 41335 45512 53553 51355 13534 53512 35454 53443 15553 14453 51234 14535 51135 21454 35124 25255 11251 45553 55534 53351 55513 25355 13245 45354 25445 43555 13414 1"""


the_alphabet="abcdefghijklmnopqrstuvwxyz"
alphabets = {
    # "alphabet": "abcdefghijklmnopqrstuvwxyz",
    # alphabet merging c with k, ie remove c to make 25 letters
    "alphabet_ck": "abcdefghijklmnopqrstuvwxyz".replace('c',''),
    "alphabet_kc": "abcdefghijklmnopqrstuvwxyz".replace('k',''),
    "alphabet_ij": "abcdefghijklmnopqrstuvwxyz".replace('i',''),
    "alphabet_ji": "abcdefghijklmnopqrstuvwxyz".replace('j',''),
    "alphabet_uv": "abcdefghijklmnopqrstuvwxyz".replace('u',''),
    "alphabet_vu": "abcdefghijklmnopqrstuvwxyz".replace('v',''),
    "alphabet_z": "abcdefghijklmnopqrstuvwxyz".replace('z',''),
    "salem_ck": "salembcdfghijknopqrstuvwxyz".replace('c',''),
    "salem_kc": "salembcdfghijknopqrstuvwxyz".replace('k',''),
    "salem_ij": "salembcdfghijknopqrstuvwxyz".replace('i',''),
    "salem_ji": "salembcdfghijknopqrstuvwxyz".replace('j',''),
    "salem_uv": "salembcdfghijknopqrstuvwxyz".replace('u',''),
    "salem_vu": "salembcdfghijknopqrstuvwxyz".replace('v',''),
    "salem_z": "salembcdfghijknopqrstuvwxyz".replace('z',''),
    "janus_ck": "janusbcdefghiklmopqrtvwxyz".replace('c',''),
    "janus_kc": "janusbcdefghiklmopqrtvwxyz".replace('k',''),
    "janus_ij": "janusbcdefghiklmopqrtvwxyz".replace('i',''),
    "janus_ji": "janusbcdefghiklmopqrtvwxyz".replace('j',''),
    "janus_uv": "janusbcdefghiklmopqrtvwxyz".replace('u',''),
    "janus_vu": "janusbcdefghiklmopqrtvwxyz".replace('v',''),
    "janus_z": "janusbcdefghiklmopqrtvwxyz".replace('z','')
}

orders = ["rows", "columns"]

def generate_alphabets(option="alphabet_ck", order="rows"):
    print(option, order)
    base_alphabet = alphabets[option]
    grid = [base_alphabet[i:i+5] for i in range(0, 25, 5)] if order == "rows" else [
        ''.join(base_alphabet[i::5]) for i in range(5)
    ]
    encode_alphabet = {}
    decode_alphabet = {}
    for row_idx, row in enumerate(grid):
        for col_idx, letter in enumerate(row):
            address = f"{row_idx+1}{col_idx+1}"
            encode_alphabet[letter] = address
            decode_alphabet[address] = letter
    return {"encode": encode_alphabet, "decode": decode_alphabet}

def decode(encoded_message, decode_alphabet):
    addresses=[encoded_message[i:i+2] for i in range(0, len(encoded_message), 2)]
    decoded_message=[]
    for address in addresses:
        letter = decode_alphabet[address]
        decoded_message.append(letter)
    return "".join(decoded_message)

def read_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return None

def write_text(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file '{file_path}': {e}")

def write_ciphertext_files(text, numbers):
    text_to_write = text.replace(' ','').replace('a','1').replace('b','2').replace('c','3').replace('d','4').replace('e','5')
    write_text("text_file.txt", text_to_write)

    numbers_to_write = numbers.replace(' ','')
    write_text("number_file.txt", numbers_to_write)

if __name__ == "__main__":

    directory = "./texts"  
    input_filename = "example.txt"  
    output_filename = "results.txt"
    input_file = os.path.join(directory, input_filename)
    output_file = os.path.join(directory, output_filename)

    message = read_text(input_file)

    decoded_messages=[]
    for order in orders:
        for alphabet in alphabets.keys():
            decode_alphabets = generate_alphabets(alphabet, order) 
            decoded_message = decode(message, decode_alphabets["decode"])
            decoded_messages.append(decoded_message[:150])

            # print(str(decode_alphabets["decode"]).replace("'","")[1:-1])
            # print(" -- ",decoded_message[:50])    

    # print(len(text), len(numbers))
    
    shift_index = 0
    shifted_messages = []
    for message in decoded_messages:
        for characters in message:
            shifted_message = message[shift_index:] + message[:shift_index]
            shifted_messages.append((message, shifted_message))
            shift_index=(shift_index + 1) % 26

    for message,shifted_message in shifted_messages:
        print(f"{message}\n{shifted_message}")
        diff_message=[]
        for index in range(len(message)):
            char=message[index]
            shift=shifted_message[index]
            char_index=the_alphabet.index(char)
            shifted_inded=the_alphabet.index(shift)
            result=(char_index-shifted_inded)%26
            diff_message.append(the_alphabet[result])
        difference=''.join(diff_message)
        print(difference)
        
        key_words = ['babbage','ada','lovelace','warne', 'janus']
        if any(word in key_words for word in difference):
            print('found')
            break
        print('not found')
        print('\n')
