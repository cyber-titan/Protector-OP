from flask import Flask, render_template, request
app = Flask(__name__)
import random, base64

# ********* Index Page *********
@app.route("/")
def home():
    return render_template("index.html")

# ****************** Feature 1 ******************
@app.route('/caesar-cipher', methods=['GET', 'POST'])
def ceasar_algo():
    if request.method == 'GET':
        return render_template('caesar-cipher.html')
    
    if request.method == 'POST':
        encryption_radio = request.form.get("encryptionRadio")
        decryption_radio = request.form.get("decryptionRadio")
        
        if encryption_radio:
            # encryption code
            plaintext = str(request.form.get("plaintext"))
            shift_value = int(str(request.form.get("shiftValue")))

            ciphertext = ""
            for i in range(len(plaintext)):
                char = plaintext[i]
    
                if (char == ' '):
                    ciphertext += ' '
                    continue

                # Encrypt uppercase characters
                if (char.isupper()):
                    ciphertext += chr((ord(char) + shift_value - 65) % 26 + 65)
    
                # Encrypt lowercase characters
                else:
                    ciphertext += chr((ord(char) + shift_value - 97) % 26 + 97)

            return render_template('caesar-cipher.html', ciphertext=ciphertext)

        else:
            # decryption code
            ciphertext = str(request.form.get("plaintext"))
            shift_value = int(str(request.form.get("shiftValue")))
            plaintext = ""
            for i in range(len(ciphertext)):
                char = ciphertext[i]
                if (char == ' '):
                    plaintext += ' '
                    continue

                # Encrypt uppercase characters
                if (char.isupper()):
                    plaintext += chr((ord(char) - shift_value - 65) % 26 + 65)
    
                # Encrypt lowercase characters
                else:
                    plaintext += chr((ord(char) - shift_value - 97) % 26 + 97)

            return render_template('caesar-cipher.html', ciphertext=plaintext)

@app.route('/rot13', methods=['GET', 'POST'])
def rot13_algo():
    if request.method == 'GET':
        return render_template('rot13.html')
    
    if request.method == 'POST':
        encryption_radio = request.form.get("encryptionRadio")
        decryption_radio = request.form.get("decryptionRadio")
        
        if encryption_radio:
            # encryption code
            plaintext = str(request.form.get("plaintext"))
            shift_value = 13
            ciphertext = ""
            for i in range(len(plaintext)):
                char = plaintext[i]
    
                if (char == ' '):
                    ciphertext += ' '
                    continue

                # Encrypt uppercase characters
                if (char.isupper()):
                    ciphertext += chr((ord(char) + shift_value - 65) % 26 + 65)
    
                # Encrypt lowercase characters
                else:
                    ciphertext += chr((ord(char) + shift_value - 97) % 26 + 97)

            return render_template('rot13.html', ciphertext=ciphertext)

        else:
            # decryption code
            ciphertext = str(request.form.get("plaintext"))
            shift_value = 13
            plaintext = ""
            for i in range(len(ciphertext)):
                char = ciphertext[i]
                if (char == ' '):
                    plaintext += ' '
                    continue

                # Encrypt uppercase characters
                if (char.isupper()):
                    plaintext += chr((ord(char) - shift_value - 65) % 26 + 65)
    
                # Encrypt lowercase characters
                else:
                    plaintext += chr((ord(char) - shift_value - 97) % 26 + 97)


            return render_template('rot13.html', ciphertext=plaintext)


def base64Encrypt(sample_string):
    sample_string_bytes = sample_string.encode("ascii", errors='ignore')
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii", errors='ignore')
    return base64_string

def base64Decrypt(base64_string):
    base64_bytes = base64_string.encode("ascii", errors='ignore')
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii", errors='ignore')
    return sample_string

@app.route('/base64', methods=['GET', 'POST'])
def base64_algo():
    if request.method == 'GET':
        return render_template('base64.html')
    
    if request.method == 'POST':
        encryption_radio = request.form.get("encryptionRadio")
        decryption_radio = request.form.get("decryptionRadio")
        
        if encryption_radio:
            # encryption code
            plaintext = str(request.form.get("plaintext"))
            ciphertext = ""
            ciphertext = base64Encrypt(plaintext)

            return render_template('base64.html', ciphertext=ciphertext)

        else:
            # decryption code
            ciphertext = str(request.form.get("plaintext"))
            plaintext = ""
            plaintext = base64Decrypt(ciphertext)

            return render_template('base64.html', ciphertext=plaintext)
        

def reverseEncrypt(message, dict):
    rev_message = message[::-1]
    for i in dict:
        rev_message = rev_message.replace(i, dict[i])
    return rev_message + "aca"

def reverseDecrypt(encMessage, dict):
    rev_message = encMessage[::-1]
    rev_message = rev_message[3:]
    for i in dict:
        rev_message = rev_message.replace(i, dict[i])
    return rev_message
        
@app.route('/reverse-cipher', methods=['GET', 'POST'])
def reverse_algo():
    if request.method == 'GET':
        return render_template('reverse-cipher.html')
    
    if request.method == 'POST':
        encryption_radio = request.form.get("encryptionRadio")
        decryption_radio = request.form.get("decryptionRadio")
        
        if encryption_radio:
            # encryption code
            plaintext = str(request.form.get("plaintext"))
            ciphertext = ""
            encDict = {"a" : "0", "e" : "1",
            "i" : "2", "o" : "3", 
            "u" : "4"} 
            ciphertext = reverseEncrypt(plaintext, encDict)

            return render_template('reverse-cipher.html', ciphertext=ciphertext)

        else:
            # decryption code
            ciphertext = str(request.form.get("plaintext"))
            plaintext = ""
            decDict = {"0" : "a", "1" : "e",
            "2" : "i", "3" : "o", 
            "4" : "u"}
            plaintext = reverseDecrypt(ciphertext, decDict)

            return render_template('reverse-cipher.html', ciphertext=plaintext)


def cipherText(plain, k):
    if(len(plain) != len(k)):
        k1 = k
        j = 0
        while(len(plain) != len(k1)):
            if(j == (len(k))):
                j = 0
                continue
            k1 += k[j]
            j += 1
        # k1 is same length key
    else:
        k1 = k
    cipher = ""
    for i in range(len(plain)):
        t = ord(plain[i]) - 97 + ord(k1[i]) - 97
        if (t >= 26):
            t -= 26
        cipher += chr(t + 97)
    return cipher

def originalText(cipher, k):
    if(len(cipher) != len(k)):
        k1 = k
        j = 0
        while(len(cipher) != len(k1)):
            if(j == (len(k))):
                j = 0
                continue
            k1 += k[j]
            j += 1
        # k1 is same length key
    else:
        k1 = k
    plain = ""
    for i in range(len(cipher)):
        t = (ord(cipher[i]) - 97) - (ord(k1[i]) - 97)
        if (t < 0):
            t += 26
        plain += chr(t + 97)
    return plain

@app.route('/one-time-pad', methods=['GET', 'POST'])
def one_time_pad_algo():
    if request.method == 'GET':
        return render_template('one-time-pad.html')
    
    if request.method == 'POST':
        encryption_radio = request.form.get("encryptionRadio")
        decryption_radio = request.form.get("decryptionRadio")
        
        if encryption_radio:
            # encryption code
            plaintext = str(request.form.get("plaintext"))
            key = str(request.form.get("key"))
            ciphertext = ""
            ciphertext = cipherText(plaintext, key)

            return render_template('one-time-pad.html', ciphertext=ciphertext)

        else:
            # decryption code
            ciphertext = str(request.form.get("plaintext"))
            key = str(request.form.get("key"))
            plaintext = ""
            plaintext = originalText(ciphertext, key)

            return render_template('one-time-pad.html', ciphertext=plaintext)
        

# ****************** Feature 2 ******************

# ********* Needed Functions *********
# ********* Encryption *********
def str2bin(secret_message):
    """Formats secret message into a list of characters as binary strings
    Args: 
    secret_message: str
    Returns: 
    secret_message: str ==> a str of characters as binary strings
    """
    bin_list = []
    for index, i in enumerate(secret_message):
        ascii_value = ord(i)
        temp = bin(ascii_value)[2:]
        temp_val = len(temp)
        if temp_val != 7:
            for x in range(7 - temp_val): temp = '0' + temp
        # adding space b/w each binary form of characters
        if index != len(secret_message) - 1: temp += " "
        bin_list.append(temp)
    return ''.join(bin_list)

def bin2hidden(secret_message):
    """Convert str of secert_message into a string of zero-width characters
    Args: 
    secret_message: str
    Returns: 
    secret_message: str ==> a secret_message string after replacing 0's, 1's and spaces with zero-width-characters
    """
    temp = ""
    for i in secret_message:
        if i == ' ':
            temp += '\u2060'
        if i == '0':
            temp += '\u200B'
        if i == '1':
            temp += '\u200C'
    return temp

def wrap(secret_message):
    """Wraps/Adds boundaries at start & end
    Args: 
    secret_message: str
    Returns: 
    secret_message: str ==> public message with hidden secret message in it
    """
    return "\uFEFF" + secret_message + "\uFEFF"



# ********* Decryption *********
def unwrap(hidden_public_message):
    """Unwraps/Removes boundaries at start & end
    Args: 
    hidden_public_message: str
    Returns: 
    hidden_public_message: str ==> unwrapped message
    """
    temp = hidden_public_message.split('\uFEFF')
    if len(temp) == 1:
        return False
    else:
        return temp[1]

def hidden2bin(unwrapped):
    """Convert str of unwrapped into a string of binary representation of each character of secret_message seperated by a space
    Args: 
    unwrapped: str
    Returns: 
    temp: str ==> each secret_message in its binary form seperated by a space
    """
    temp = ""
    for i in unwrapped:
        if i == '\u2060':
            temp += ' '
        if i == '\u200B':
            temp += '0'
        if i == '\u200C':
            temp += '1'
    return temp

def bin2str(unwrapped):
    """Converts binary form of each character to form secret_message
    Args: 
    unwrapped: str
    Returns: 
    temp: str ==> a str which is the secret_message
    """
    temp = ""
    char_list = unwrapped.split(" ")
    for i in char_list:
        temp += chr(int(i, 2))
    return temp


@app.route("/zero-width-stego", methods=['GET', 'POST'])
def zero_width_stego():
    if request.method == 'GET':
        return render_template("zero-width-stego.html")
    
    if request.method == 'POST':
        # to konw which form was submitted
        form_type = request.form.get('form_type')

        if form_type == 'left_form':
            public_message = str(request.form.get('inputPublicMsg'))
            secret_message = str(request.form.get('inputSecretMsg'))
            # ********* "Hide It" code here/Encryption code *********
            # finding half-way point
            half = round(len(public_message) / 2)
            # gets str2bin list & store it
            secret_message = str2bin(secret_message)
            # gets bin2hidden string & store it
            secret_message = bin2hidden(secret_message)
            # gets wrapped secret_message & store it
            secret_message = wrap(secret_message)
            # Inject secret_message at half index of public_message
            hidden_public_message = public_message[:half + 1] + secret_message + public_message[half + 1:]
            return render_template("zero-width-stego.html", hidden_public_message=hidden_public_message)
        else:
            # below "Reveal It" variable
            hidden_public_message1 = str(request.form.get('inputPublicMsg1'))
            # ********* "Reveal It" code here/Decryption code *********
            # removes start & end boundaries
            unwrapped = unwrap(hidden_public_message1)
            toast_message = ""
            if not unwrapped:
                unwrapped = "NOTE: No private message was found in this public message. This is not a secret message."
                toast_message = "No secret message was found"
            else:
                # binary form of characters of secret_message
                unwrapped = hidden2bin(unwrapped)

                # gets secret_message
                unwrapped = bin2str(unwrapped)
                toast_message = ""  # Empty string if there is a private message

            return render_template("zero-width-stego.html", unwrapped=unwrapped, toast_message=toast_message)


# ****************** Feature 3 ******************

@app.route('/strong-pass', methods=['GET', 'POST'])
def strong_pass_generator():
    if request.method == 'GET':
        return render_template("strong-pass.html")
    
    if request.method == 'POST':
        # STRONG PASSWORD GENERATOR

        """
        Len = 25 ==> abcdefghijklmnopqrstuvwxyz
        Len = 25 ==> ABCDEFGHIJKLMNOPQRSTUVWXYZ
        Len = 10 ==> 0123456789
        Len = 32 ==> !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 
        """

        lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '\\']

        # input size of password needed
        password_size = str(request.form.get('inputLengthOfPass'))
        temp = int(password_size)

        strong_password = []
        while temp > 0:
            if temp == 0: break
            # 1. choose a lower letter & shuffle result
            strong_password += random.choice(lower_letters)
            random.shuffle(strong_password)
            temp -= 1

            if temp == 0: break
            # 2. choose a upper letter & shuffle result
            strong_password += random.choice(upper_letters)
            random.shuffle(strong_password)
            temp -= 1

            if temp == 0: break
            # 3. choose a digit & shuffle result
            strong_password += random.choice(digits)
            random.shuffle(strong_password)
            temp -= 1

            if temp == 0: break
            # 4. choose a symbol & shuffle result
            strong_password += random.choice(symbols)
            random.shuffle(strong_password)
            temp -= 1

        strong_password = ''.join(strong_password)
        return render_template('strong-pass.html', strong_password=strong_password)


# ****************** Feature 4 ******************

@app.route('/pass-strength', methods=['GET', 'POST'])
def pass_strength():
    if request.method == 'GET':
        return render_template('pass-strength.html')

    if request.method == 'POST':
        # PASSWORD STRENGTH TESTER
        """
        Very Weak: Passwords that do not meet any of the specified criteria. ==> " "
        Weak: Passwords that meet only one or two of the specified criteria. ==> "HelloWorld"
        Moderate: Passwords that meet three of the specified criteria. ==> "HelloWorld1"
        Strong: Passwords that meet four of the specified criteria. ==> "HelloWorld12"
        Very Strong: Passwords that meet all of the specified criteria. ==> "HelloWorld12@"

        Len = 25 ==> abcdefghijklmnopqrstuvwxyz
        Len = 25 ==> ABCDEFGHIJKLMNOPQRSTUVWXYZ
        Len = 10 ==> 0123456789
        Len = 32 ==> !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 
        """

        lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '\\']

        lc, uc, dc, sc = 0, 0, 0, 0
        # take input
        password = request.form.get('inputPass')

        # go through whole password
        for i in password:
            if i.islower(): lc += 1
            if i.isupper(): uc += 1
            if i.isdigit(): dc += 1
            if i in symbols: sc += 1

        # calculate final score out of 5
        score = 0
        if len(password) >= 12: score += 1
        if lc: score += 1
        if uc: score += 1
        if dc: score += 1
        if sc: score += 1

        # output
        result, strength_value, strength_percentage, progress_bar_color = "", 0, "", "bg-"
        if score == 0: 
            result = "Very Weak 😱"
            strength_value = 20
            progress_bar_color += "danger"
            strength_percentage = str(strength_value) + '%'
        if score == 1 or score == 2: 
            result = "Weak 😬"
            strength_value = 40
            progress_bar_color += "warning"
            strength_percentage = str(strength_value) + '%'
        if score == 3: 
            result = "Moderate 😐"
            strength_value = 60
            progress_bar_color += "info"
            strength_percentage = str(strength_value) + '%'
        if score == 4: 
            result = "Strong 🙂"
            strength_value = 80
            progress_bar_color += "primary"
            strength_percentage = str(strength_value) + '%'
        if score == 5: 
            result = "Very Strong 😎"
            strength_value = 100
            progress_bar_color += "success"         
            strength_percentage = str(strength_value) + '%'   

        return render_template('pass-strength.html', result=result, strength_value=strength_value, strength_percentage=strength_percentage, progress_bar_color=progress_bar_color)
        

@app.route('/tips', methods=['GET'])
def tips_function():
    if request.method == 'GET': 
        return render_template('tips.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)